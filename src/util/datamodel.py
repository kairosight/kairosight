from math import pi, floor, ceil, sqrt
import numpy as np


def model_transients(model_type='Vm', t=100, t0=0, fps=1000, f_0=200, f_amp=100, noise=0, num=1, cl=100):
    """Create a 2-D array of model 16-bit optical data of either
    murine action potentials (OAP) or a murine calcium transients (OCT).

       Parameters
       ----------
       model_type : str
            The type of transient: 'Vm' or 'Ca', default is 'Vm'
       t : int, float
            Length of array in milliseconds (ms), default is 100
       t0 : int or float
            Start time (ms) of first transient, default is 0
       fps : int
            Frame rate (frames per second) of optical data acquisition, default is 1000, min is 200
       f_0 : int
            Baseline fluorescence value in counts, default is 100
       f_amp : int
            Amplitude of the transient in counts, default is 100.
            Can be negative, e.g. cell depolarization with fast voltage dyes
       noise : int
            Magnitude of gaussian noise, as a percentage of f_peak, default is 0
       num : int or str
            Number of transients to generate, default is 1. If 'full', calculate max num to fill array
       cl : int
            Time (ms) between transients aka Cycle Length, default is 100

       Returns
       -------
       model_time : ndarray
            An array of timestamps (ms) corresponding to the model_data
       model_data : ndarray
            An array of model data, dtype is int
       """
    # Constants
    MIN_TOTAL_T = 100   # Minimum transient length (ms)
    # Check parameters
    if model_type not in ['Vm', 'Ca']:
        if type(model_type) not in [str]:
            raise TypeError('Model type must be a string, "Vm" or "Ca" ')
        raise ValueError("The model type must either be 'Vm' or 'Ca'")
    if (type(t) or type(t0)) not in [int]:
        raise TypeError('All time parameters must be ints')
    if (type(fps) or type(f_0) or type(f_amp)) not in [int]:
        raise TypeError('All fps and fluorescent parameters must be ints')
    if type(num) not in [int, str]:
        raise TypeError('Number of transients must be an int or "full"')
    if type(cl) not in [int]:
        raise TypeError('Cycle Lenth must be an int')

    if t < MIN_TOTAL_T:
        raise ValueError('The time length (t) must be longer than {} ms '.format(MIN_TOTAL_T))
    if t0 >= t:
        raise ValueError('The start time (t0) must be less than the time length (t)')
    if fps <= 200 or fps > 1000:
        raise ValueError('The fps must be > 200 or <= 1000')
    if f_amp < 0:
        raise ValueError('The amplitude must >=0')
    if model_type is 'Vm' and (f_0 - f_amp < 0):
        raise ValueError('Effective Vm amplitude is too negative')
    if type(num) not in [str]:
        if num <= 0:
            raise ValueError('The number of transients must be > 0')
        if num * MIN_TOTAL_T > t - t0:
            raise ValueError('Too many transients, {}, for the total time, {} ms with start time {} ms'
                             .format(num, t, t0))
    else:
        if num is not 'full':
            raise ValueError('If not an int, number of transients must be ""full""')

    if cl < 50:
        raise ValueError('The Cycle Length must be > 50 ms')

    # Calculate important constants
    FPMS = fps / 1000
    FRAMES = floor(FPMS * t)
    FRAME_T = 1 / FPMS
    FRAME_T0 = round(t0 / FRAME_T)
    FINAL_T = t - FRAME_T
    if num is 'full':
        num = ceil(FINAL_T / cl)

    FL_COUNT_MAX = 2**16 - 1
    if f_0 > FL_COUNT_MAX:
        raise ValueError('The baseline fluorescence (f0) must be less than 2^16 - 1 (65535)')
    if abs(f_amp) > FL_COUNT_MAX:
        raise ValueError('The amplitude (f_peak) must be less than 2^16 - 1 (65535)')

    # Initialize full model arrays
    model_time = np.linspace(start=0, stop=FINAL_T, num=FRAMES)     # time array
    model_data = np.full(int(FPMS * t), f_0, dtype=np.uint16)      # data array, default value is f_0
    if not np.equal(model_time.size, model_data.size):
        raise ArithmeticError('Lengths of time and data arrays not equal!')

    if model_type is 'Vm':
        # With voltage dyes, depolarization transients have a negative deflection and return to baseline
        # Initialize a single OAP array (50 ms) + 50 ms to sync with Ca
        vm_amp = -f_amp
        # Depolarization phase
        model_dep_period = 5  # XX ms long
        model_dep_frames = floor(model_dep_period / FRAME_T)
        # Generate high-fidelity data
        model_dep_full = np.full(model_dep_period, f_0)
        for i in range(0, model_dep_period):
            model_dep_full[i] = f_0 + (vm_amp * np.exp(-(((i - model_dep_period) / 3) ** 2)))  # a simplified Gaussian
        # Under-sample the high-fidelity data
        model_dep = model_dep_full[::floor(model_dep_period/model_dep_frames)][:model_dep_frames]

        # Early repolarization phase (from peak to APD 20, aka 80% of peak)
        model_rep1_period = 5  # XX ms long
        model_rep1_frames = floor(model_rep1_period / FRAME_T)
        apd_ratio = 0.8
        m_rep1 = -(vm_amp - (vm_amp * apd_ratio)) / model_rep1_period     # slope of this phase
        model_rep1 = np.full(model_rep1_frames, f_0)
        for i in range(0, model_rep1_frames):
            model_rep1[i] = ((m_rep1 * i) + vm_amp + f_0)    # linear

        # Late repolarization phase
        model_rep2_period = 50 - model_dep_period - model_rep1_period  # remaining OAP time
        model_rep2_frames = floor(model_rep2_period / FRAME_T)
        model_rep2_t = np.linspace(0, 50, model_rep2_frames)
        A, B, C = vm_amp * 0.8, (5 / m_rep1), f_0     # exponential decay parameters
        # model_rep2 = A * np.exp(-B * model_rep2_t) + C    # exponential decay, concave down
        tauFall = 10
        model_rep2 = A * np.exp(-model_rep2_t / tauFall) + C    # exponential decay, concave down, using tauFall
        model_rep2 = model_rep2.astype(np.uint16, copy=False)
        # Pad the end with 50 ms of baseline
        model_rep2Pad_frames = floor(50 / FRAME_T)
        model_rep2Pad = np.full(model_rep2Pad_frames, f_0, dtype=np.uint16)
        model_rep2 = np.concatenate((model_rep2, model_rep2Pad), axis=None)

    else:
        # With calcium dyes, depolarization transients have a positive deflection and return to baseline
        # Initialize a single OCT array (100 ms)
        # Depolarization phase
        model_dep_period = 10  # XX ms long
        model_dep_frames = floor(model_dep_period / FRAME_T)
        # Generate high-fidelity data
        model_dep_full = np.full(model_dep_period, f_0)
        for i in range(0, model_dep_period):
            model_dep_full[i] = f_0 + (f_amp * np.exp(-(((i - model_dep_period) / 6) ** 2)))  # a simplified Gaussian
        # Under-sample the high-fidelity data
        model_dep = model_dep_full[::floor(model_dep_period/model_dep_frames)][:model_dep_frames]

        # Early repolarization phase (from peak to CAD 40, aka 60% of peak)
        model_rep1_period = 15  # XX ms long
        model_rep1_frames = floor(model_rep1_period / FRAME_T)
        cad_ratio = 0.6
        m_rep1 = -(f_amp - (f_amp * cad_ratio)) / model_rep1_period     # slope of this phase
        model_rep1_full = np.full(model_rep1_period, f_0)
        # Generate high-fidelity data
        for i in range(0, model_rep1_period):
            model_rep1_full[i] = ((m_rep1 * i) + f_amp + f_0)    # linear
        # Under-sample the high-fidelity data
        model_rep1 = model_rep1_full[::floor(model_rep1_period/model_rep1_frames)][:model_rep1_frames]

        # Late repolarization phase
        model_rep2_period = 100 - model_dep_period - model_rep1_period  # remaining OCT time
        model_rep2_frames = floor(model_rep2_period / FRAME_T)
        model_rep2_t = np.linspace(0, 100, model_rep2_frames)
        A, B, C = f_amp * cad_ratio, (0.8 / m_rep1), f_0     # exponential decay parameters
        # model_rep2 = A * np.exp(B * model_rep2_t) + C    # exponential decay, concave up
        tauFall = 30
        model_rep2 = A * np.exp(-model_rep2_t / tauFall) + C    # exponential decay, concave up, using tauFall
        model_rep2 = model_rep2.astype(np.uint16, copy=False)

    # Assemble the transient
    model_tran = np.concatenate((model_dep, model_rep1, model_rep2), axis=None)

    # Assemble the start time and transient(s) into the full array
    cl_frames = floor(cl / FRAME_T)
    if cl_frames < floor(100 / FRAME_T):
        # Shorten the transient array
        model_tran = model_tran[:cl]
    else:
        # Pad the transient array
        tranPad_frames = floor((cl - 100) / FRAME_T)
        tranPad = np.full(tranPad_frames, f_0, dtype=np.uint16)
        model_tran = np.concatenate((model_tran, tranPad), axis=None)

    # Assemble the train of transients
    model_tran_train = np.tile(model_tran, num)
    if model_tran_train.size > model_data.size - FRAME_T0:
        # Shorten train array to fit into final data array
        model_tran_train = model_tran_train[:model_data.size - FRAME_T0]

    model_data[FRAME_T0:FRAME_T0 + model_tran_train.size] = model_tran_train

    # Add gaussian noise, mean: 0, standard deviation: 10% of peak, length
    model_noise = np.random.normal(0, (noise/100) * f_amp, model_data.size)
    model_data = model_data + np.round(model_noise)

    return model_time, model_data.astype(int)


def model_stack(size=(100, 50), **kwargs):
    """Create a stack (3-D array, TYX) of model 16-bit optical data of either a
    murine action potential (OAP) or a murine calcium transient (OCT).

       Parameters
       ----------
       size : tuple
            The height and width of the optical data. default is (100, 50)

       Other Parameters
       ----------------
       **kwargs : `.model_transients`. parameter, optional
            All parameters supported by `.model_transients`.

       Returns
       -------
       model_time : ndarray
            An array of timestamps corresponding to model_data
       model_data : ndarray
            A 3-D array (T, Y, X) of model 16-bit data, dtype is int
       """
    # Constants
    MIN_SIZE = (10, 10)   # Minimum stack size (Height, Width)
    # Check parameters
    if type(size) not in [tuple]:
        raise TypeError('Image size must be a tuple, e.g. (20, 20)')
    if (size[0] < MIN_SIZE[0]) or (size[1] < MIN_SIZE[1]):
        raise ValueError('The size (H, W) must be larger than {}'.format(MIN_SIZE))

    # Create a model transient array for each pixel
    pixel_time, pixel_data = model_transients(**kwargs)

    # Initialize full model arrays
    FRAMES = pixel_data.size
    model_time = pixel_time
    model_size = (FRAMES, size[0], size[1])
    model_data = np.empty(model_size, dtype=np.uint16)      # data array, default value is f_0
    for i_frame in range(0, FRAMES):
        # Set every pixel value in that of the model transient
        model_data[i_frame, :, :] = np.full(size, pixel_data[i_frame])

    return model_time, model_data


def model_stack_propagation(size=(100, 50), cv=10, **kwargs):
    """Create a stack (3-D array, TYX) of propagating model 16-bit optical data of either a
    murine action potential (OAP) or a murine calcium transient (OCT).

       Parameters
       ----------
       size : tuple
            The height and width (px) of the optical data. default is (100, 50)
       cv : int
            Conduction velocity (cm/s) of propagating OAPs/OCTs, default is 10

       Other Parameters
       ----------------
       **kwargs : `.model_transients`. parameter, optional
            All parameters supported by `.model_transients`.

       Returns
       -------
       model_time : ndarray
            An array of timestamps corresponding to model_data
       model_data : ndarray
            A 3-D array (T, Y, X) of model 16-bit data, dtype is int
       """
    # Constants
    # MIN_TOTAL_T = 500   # Minimum stack length (ms)
    MIN_SIZE = (10, 10)   # Minimum stack size (Height, Width)
    MIN_CV = 5   # Minimum cv (cm/s)
    # Check parameters
    if type(size) not in [tuple]:
        raise TypeError('Image size must be a tuple, e.g. (20, 20)')
    if (size[0] < MIN_SIZE[0]) or (size[1] < MIN_SIZE[1]):
        raise ValueError('The size (H, W) must be larger than {}'.format(MIN_SIZE))
    if cv < MIN_CV:
        raise ValueError('The Conduction Velocity must be larger than {}'.format(MIN_CV))

    # Create a model transient array
    pixel_time, pixel_data = model_transients(**kwargs)

    # Initialize full model arrays
    FRAMES = pixel_data.size
    model_time = pixel_time
    model_size = (FRAMES, size[0], size[1])
    model_data = np.empty(model_size, dtype=np.uint16)      # data array, default value is f_0

    # Calculations for propagation timing
    # Dimensions of model data (px)
    HEIGHT, WIDTH = size
    # Allocate space for the Activation Map
    act_map = np.zeros(shape=(HEIGHT, WIDTH))
    # Spatial resolution (cm/px)
    resolution = 0.005  # 4 cm / 200 px
    # resolution = 0.0149  # pig video resolution

    # Convert conduction velocity from cm/s to px/s
    conduction_v_px = cv / resolution
    # # Convert dimensions to cm
    # HEIGHT = HEIGHT * resolution
    # WIDTH = WIDTH * resolution

    # Generate an isotropic activation map, radiating from the center
    origin_x, origin_y = WIDTH / 2, HEIGHT / 2
    # Assign an activation time to each pixel
    for iy, ix in np.ndindex(act_map.shape):
        # Compute the distance from the center (cm)
        d = sqrt((abs(origin_x - ix) ** 2 + abs((origin_y - iy) ** 2)))
        # Calculate the time associated with that distance from the point of activation
        act_time = d / conduction_v_px
        # Convert time from s to ms
        act_time = act_time * 1000
        prop_offset = floor(act_time)
        # Create a model transient array for each pixel
        pixel_time, pixel_data = model_transients(t0=prop_offset, **kwargs)
        # Set every pixel's values to those of the offset model transient
        model_data[:, iy, ix] = pixel_data

    return model_time, model_data


# Code for example tests
def circle_area(r):
    if r < 0:
        raise ValueError('The radius cannot be negative')

    if type(r) not in [int, float]:
        raise TypeError('The radius must be a non-negative real number')

    return pi * (r**2)
