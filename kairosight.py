#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import traceback
import numpy as np
from pathlib import PurePath
from skimage import io
from PyQt5 import QtCore
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QFileSystemModel, QDialogButtonBox
import pyqtgraph as pg
from ui.KairoSightMainMDI import Ui_MDIMainWindow
from ui.KairoSightWidgetTIFFpyqtgraph import Ui_WidgetTiff
from ui.KairoSightWidgetFolderTree import Ui_WidgetFolderTree
from ui.KairoSightWidgetImageProcess import Ui_WidgetImageProcess
from ui.KairoSightWidgetIsolate import Ui_WidgetIsolate
from algorithms import tifopen


class DesignerMainWindow(QMainWindow, Ui_MDIMainWindow):
    """Customization for Qt Designer created window"""

    def __init__(self, parent=None):
        # initialization of the superclass
        super(DesignerMainWindow, self).__init__(parent)
        # setup the GUI --> function generated by pyuic4
        self.setupUi(self)
        # connect the signals with the slots
        # self.actionLoad.triggered.connect(self.open_tiff)
        # self.actionClose.triggered.connect(self.close)
        self.actionTIFF.triggered.connect(self.open_tiff)
        self.actionFolder.triggered.connect(self.open_folder)
        self.actionStart_ImageProcess.triggered.connect(self.image_process)
        self.actionStart_Isolate.triggered.connect(self.isolate)

    def open_tiff(self, file=None):
        """Open a SubWindow with a TIFF stack in the main MDI area"""
        if file:
            print('Opening tiff with passed filepath: ' + file)
        else:
            # Use a QFileDialog to get filepath if none provided
            file, mask = QFileDialog.getOpenFileName(self, 'Open a .tif/.tiff stack')

        if file:
            self.statusBar().showMessage('Opening ' + file + ' ...')
            f_purepath = PurePath(file)
            f_path = str(f_purepath.parent) + '\\'
            f_name = f_purepath.stem
            f_ext = f_purepath.suffix
            f_display = f_path + ' ' + f_name + ' ' + f_ext
            print('file (path name ext): ' + f_display)
            if f_ext is '.tif' or '.tiff':
                print('TIFF chosen')
                # Create QMdiSubWindow with Ui_WidgetTiff
                try:
                    sub = DesignerSubWindowTiff(f_path=f_path, f_name=f_name, f_ext=f_ext)
                    print('DesignerSubWindowTiff "sub" created')
                    sub.setObjectName(str(file))
                    sub.setWindowTitle('TIFF View: ' + f_display)
                    # Add and connect QMdiSubWindow to MDI
                    self.mdiArea.addSubWindow(sub)
                    print('"sub" added to MDI')
                    sub.show()
                    self.statusBar().showMessage('Opened ' + file)
                except Exception:
                    traceback.print_exc()
                    self.statusBar().showMessage('Failed to open, ' + file)
        else:
            print('path is None')
            self.statusBar().showMessage('Open cancelled')

    def open_folder(self):
        """Open a SubWindow with a folder tree view in the main MDI area"""
        folder_path = QFileDialog.getExistingDirectory(self, 'Choose a folder to view')
        print('Folder chosen! path: ' + folder_path)
        # Create QMdiSubWindow with Ui_WidgetTiff
        sub = DesignerSubWindowFolder(root=folder_path)
        print('DesignerSubWindowFolder "sub" created')
        print('Set "sub" widget to "Ui_WidgetFolderTree"')
        sub.setWindowTitle('Folder View: ' + folder_path)
        # Add and connect QMdiSubWindow to MDI
        self.mdiArea.addSubWindow(sub)
        sub.pushButtonOpen.released.connect(lambda: self.open_tiff(sub.currentFilePath))
        print('"sub" added to MDI')
        sub.show()

    def image_process(self):
        """Open the Image Process SubWindow"""
        windows_object_names = []
        # Create a list of all open TIFF subwindows
        for sub in self.mdiArea.subWindowList():
            # print('**' + str(type(sub.widget())) + ', ' + sub.widget().objectName() + ' is a tiff? ')
            if type(sub.widget()) is DesignerSubWindowTiff:
                windows_object_names.append(sub.widget().objectName())
        sub_process = DesignerSubWindowImageProcess(w_list=windows_object_names)
        self.mdiArea.addSubWindow(sub_process)
        sub_process.show()

    def isolate(self):
        """Open the Isolate SubWindow"""
        windows_object_names = []
        # Create a list of all open TIFF subwindows
        for sub in self.mdiArea.subWindowList():
            # print('**' + str(type(sub.widget())) + ', ' + sub.widget().objectName() + ' is a tiff? ')
            if type(sub.widget()) is DesignerSubWindowTiff:
                windows_object_names.append(sub)
        sub_iso = DesignerSubWindowIsolate(w_list=windows_object_names)
        self.mdiArea.addSubWindow(sub_iso)
        sub_iso.show()


class DesignerSubWindowTiff(QWidget, Ui_WidgetTiff):
    """Customization for WidgetTiff subwindow for an MDI"""

    def __init__(self, parent=None, f_path=None, f_name=None, f_ext=None):
        # Initialization of the superclass
        super(DesignerSubWindowTiff, self).__init__(parent)
        # Setup the GUI
        self.setupUi(self)
        pg.setConfigOptions(background=pg.mkColor(0.1))
        pg.setConfigOptions(foreground=pg.mkColor(0.3))
        # Preserve plot area's aspect ration so image always scales correctly
        self.graphicsView.p1.setAspectLocked(True)
        # Connect the scrollbar's value signal to trigger a video update
        self.horizontalScrollBar.valueChanged['int'].connect(self.update_video)
        # Load the video file
        self.video_path = f_path
        self.video_name = f_name
        self.video_ext = f_ext
        self.video_file, self.dt = tifopen.tifopen(self.video_path, self.video_name + self.video_ext)
        print('tifopen finished')
        # get video properties
        self.video_shape = self.video_file.shape
        if len(self.video_shape) < 3:
            raise Exception('TIFF has less than 3 dimensions')
        self.frames = self.video_shape[0]

        # Transpose second and third axes (y, x) to correct orientation (x, y)
        self.video_data = np.transpose(self.video_file, (0, 2, 1))
        # Flip each frame in the left/right direction, expected to be up/down
        for i in range(self.frames):
            self.video_data[i] = np.fliplr(self.video_data[i])

        # TODO revise UI to show dt
        self.fps = 1000 / self.dt
        self.duration = self.fps * (self.frames + 1)
        self.width, self.height = self.video_shape[2], self.video_shape[1]
        print('video shape: ', self.video_shape)
        print('Width x Height: ', self.width, self.height)
        self.SizeLabelEdit.setText(str(self.width) + ' X ' + str(self.height))
        print('# of Frames: ', self.frames)
        print('FPS: ', self.fps)
        print('Duration (ms): ', self.duration)
        if not np.isnan(self.fps):
            self.frameRateLineEdit.setText(str(self.fps))
            self.frameRateLineEdit.setEnabled(False)
            self.durationMsLineEdit.setText(str(self.duration))
            self.durationMsLineEdit.setEnabled(False)
        # set scroll bar maximum to number of frames
        self.horizontalScrollBar.setMinimum(1)
        self.horizontalScrollBar.setMaximum(self.frames)
        # self.update_video(1)
        self.graphicsView.hist.setLevels(self.video_data.min(), self.video_data.max())
        self.ROIs = []
        print('WidgetTiff ready')

    def update_video(self, frame=0):
        """Updates the video frame drawn to the canvas"""
        print('Updating video plot in a subWindow with:')
        print('***' + self.video_name + '[' + str(frame) + ']')
        # Update ImageItem with a frame in stack
        self.graphicsView.img.setImage(self.video_data[frame - 1])
        # Notify histogram item of image change
        self.graphicsView.hist.regionChanged()


class DesignerSubWindowFolder(QWidget, Ui_WidgetFolderTree):
    """Customization for WidgetFolderTree subwindow for an MDI"""

    def __init__(self, parent=None, root=None):
        # initialization of the superclass
        super(DesignerSubWindowFolder, self).__init__(parent)
        self.dir = QDir(root)
        self.currentFileName = ''
        self.currentFilePath = ''
        # setup the GUI
        self.setupUi(self)
        print('WidgetFolderTree UI setup')
        self.model = QFileSystemModel()
        self.model.setRootPath(root)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(root))
        print('treeView ready')

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def on_treeView_clicked(self, index):
        index_item = self.model.index(index.row(), 0, index.parent())
        self.currentFileName = self.model.fileName(index_item)
        self.currentFilePath = self.model.filePath(index_item)
        print('Clicked: ' + self.currentFilePath + ' ' + self.currentFileName)


class DesignerSubWindowImageProcess(QWidget, Ui_WidgetImageProcess):
    """Customization for WidgetFolderTree subwindow for an MDI"""

    def __init__(self, parent=None, w_list=None):
        # initialization of the superclass
        super(DesignerSubWindowImageProcess, self).__init__(parent)
        self.windowListNames = w_list
        self.currentFileName = ''
        self.currentFilePath = ''
        # setup the GUI
        self.setupUi(self)
        print('WidgetImageProcess UI setup')
        self.listWidgetOpenTiffs.addItems(self.windowListNames)
        print('WidgetImageProcess ready')


class DesignerSubWindowIsolate(QWidget, Ui_WidgetIsolate):
    """Customization for WidgetFolderTree subwindow for an MDI"""

    def __init__(self, parent=None, w_list=None):
        # initialization of the superclass
        super(DesignerSubWindowIsolate, self).__init__(parent)
        self.windowList = w_list
        self.windowDict = {}    # Dictionary with structure "window_name_short": "window"
        self.windowListNamesShort = []  # List of shortened window names for display in combo box
        name_limit = 50
        for w in self.windowList:
            w_name = w.widget().objectName()
            w_name_short = '..' + w_name[-name_limit:] if len(w_name) > name_limit else w_name
            # self.windowListNamesShort.append(w_name_short)
            # Populate dictionary
            self.windowDict[w_name_short] = w.widget()
        self.currentROIs = []
        self.currentWindow = None
        self.currentPlot = None
        self.roi_preview = None
        # setup the GUI
        self.setupUi(self)
        print('WidgetIsolate UI setup')
        self.comboBoxSource.addItems(self.windowDict.keys())
        self.comboBoxSource.highlighted['int'].connect(self.selectionMade)
        self.buttonBox.button(QDialogButtonBox.RestoreDefaults).clicked.connect(self.loadDefaults)
        self.checkBoxPreview.stateChanged.connect(self.previewChanged)
        self.selectionMade(0)
        print('WidgetIsolate ready')

    def selectionMade(self, i):
        print('** selectrion made in a ', type(self))
        print('*Current: ', self.comboBoxSource.currentText())
        print('*Loading tiff dimensions and ROIs')
        self.currentWindow = self.windowDict[self.comboBoxSource.currentText()]
        self.currentPlot = self.currentWindow.graphicsView.p1
        self.currentROIs = self.currentWindow.ROIs
        print('*Window: ', str(self.currentWindow), 'ROIs: ', str(self.currentROIs))
        print('*W x H: ', str(self.currentWindow.width), ' X ', str(self.currentWindow.height),
              'ROIs: ', str(self.currentROIs))

    def loadDefaults(self):
        default_r = 15
        if self.currentWindow:
            try:
                # Populate fields with default values
                self.originXLineEdit.setText(str(int(self.currentWindow.width / 2)))
                self.originYLineEdit.setText(str(int(self.currentWindow.height / 2)))
                self.radiusLineEdit.setValue(default_r)
            except Exception:
                traceback.print_exc()
        else:
            print('No tiff windows available')

    def updateParameters(self, state):
        x, y = str(int(state['pos'].x())), str(int(state['pos'].y()))
        r = int(state['size'][0])
        print("Updating region with: ", x, ' ', y, ' ', r)
        # Populate fields with passed values
        self.originXLineEdit.setText(x)
        self.originYLineEdit.setText(y)
        self.radiusLineEdit.setValue(r)

    def previewChanged(self):
        print('*Preview checkbox changed: ', self.checkBoxPreview.isChecked())
        x, y = int(self.originXLineEdit.text()), int(self.originYLineEdit.text())
        r = self.radiusLineEdit.value()
        try:
            if not self.roi_preview:
                self.roi_preview = pg.CircleROI([x, y], [r, r], pen=(2, 9), scaleSnap=True, translateSnap=True)
                self.roi_preview.sigRegionChanged.connect(lambda: self.updateParameters(self.roi_preview.getState()))
                self.roi_preview.sigRegionChanged.connect(lambda: self.updateParameters(self.roi_preview.getState()))

            if self.checkBoxPreview.isChecked():
                # print('Adding roi_preview')
                # Draw region on current window's plot
                self.currentPlot.addItem(self.roi_preview)
                # self.currentROIs.append()
            else:
                # print('Removing roi_preview')
                self.currentPlot.removeItem(self.roi_preview)
                self.roi_preview = None

        except Exception:
            traceback.print_exc()

# create the GUI application
app = QApplication(sys.argv)
# instantiate the main window
dmw = DesignerMainWindow()
# show it
dmw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code as the Qt application
sys.exit(app.exec_())
