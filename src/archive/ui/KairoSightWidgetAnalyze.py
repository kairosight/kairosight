# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KairoSightWidgetAnalyze.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WidgetAnalyze(object):
    def setupUi(self, WidgetAnalyze):
        WidgetAnalyze.setObjectName("WidgetAnalyze")
        WidgetAnalyze.resize(348, 528)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WidgetAnalyze.sizePolicy().hasHeightForWidth())
        WidgetAnalyze.setSizePolicy(sizePolicy)
        WidgetAnalyze.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(WidgetAnalyze)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_Source = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Source.setObjectName("horizontalLayout_Source")
        self.labelSource = QtWidgets.QLabel(WidgetAnalyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSource.sizePolicy().hasHeightForWidth())
        self.labelSource.setSizePolicy(sizePolicy)
        self.labelSource.setTextFormat(QtCore.Qt.PlainText)
        self.labelSource.setObjectName("labelSource")
        self.horizontalLayout_Source.addWidget(self.labelSource)
        self.comboBoxSource = QtWidgets.QComboBox(WidgetAnalyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSource.sizePolicy().hasHeightForWidth())
        self.comboBoxSource.setSizePolicy(sizePolicy)
        self.comboBoxSource.setObjectName("comboBoxSource")
        self.horizontalLayout_Source.addWidget(self.comboBoxSource)
        self.verticalLayout_2.addLayout(self.horizontalLayout_Source)
        self.horizontalLayout_ROI = QtWidgets.QHBoxLayout()
        self.horizontalLayout_ROI.setObjectName("horizontalLayout_ROI")
        self.labelROIs = QtWidgets.QLabel(WidgetAnalyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelROIs.sizePolicy().hasHeightForWidth())
        self.labelROIs.setSizePolicy(sizePolicy)
        self.labelROIs.setTextFormat(QtCore.Qt.PlainText)
        self.labelROIs.setObjectName("labelROIs")
        self.horizontalLayout_ROI.addWidget(self.labelROIs)
        self.comboBoxROIs = QtWidgets.QComboBox(WidgetAnalyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxROIs.sizePolicy().hasHeightForWidth())
        self.comboBoxROIs.setSizePolicy(sizePolicy)
        self.comboBoxROIs.setCurrentText("")
        self.comboBoxROIs.setObjectName("comboBoxROIs")
        self.horizontalLayout_ROI.addWidget(self.comboBoxROIs)
        self.verticalLayout_2.addLayout(self.horizontalLayout_ROI)
        self.horizontalLayout_Signal = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Signal.setObjectName("horizontalLayout_Signal")
        self.labelSignal = QtWidgets.QLabel(WidgetAnalyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSignal.sizePolicy().hasHeightForWidth())
        self.labelSignal.setSizePolicy(sizePolicy)
        self.labelSignal.setTextFormat(QtCore.Qt.PlainText)
        self.labelSignal.setObjectName("labelSignal")
        self.horizontalLayout_Signal.addWidget(self.labelSignal)
        self.comboBoxSignal = QtWidgets.QComboBox(WidgetAnalyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxSignal.sizePolicy().hasHeightForWidth())
        self.comboBoxSignal.setSizePolicy(sizePolicy)
        self.comboBoxSignal.setObjectName("comboBoxSignal")
        self.horizontalLayout_Signal.addWidget(self.comboBoxSignal)
        self.verticalLayout_2.addLayout(self.horizontalLayout_Signal)
        self.horizontalLayout_Analysis = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Analysis.setObjectName("horizontalLayout_Analysis")
        self.labelAnalysis = QtWidgets.QLabel(WidgetAnalyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelAnalysis.sizePolicy().hasHeightForWidth())
        self.labelAnalysis.setSizePolicy(sizePolicy)
        self.labelAnalysis.setTextFormat(QtCore.Qt.PlainText)
        self.labelAnalysis.setObjectName("labelAnalysis")
        self.horizontalLayout_Analysis.addWidget(self.labelAnalysis)
        self.comboBoxAnalysis = QtWidgets.QComboBox(WidgetAnalyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxAnalysis.sizePolicy().hasHeightForWidth())
        self.comboBoxAnalysis.setSizePolicy(sizePolicy)
        self.comboBoxAnalysis.setObjectName("comboBoxAnalysis")
        self.comboBoxAnalysis.addItem("")
        self.horizontalLayout_Analysis.addWidget(self.comboBoxAnalysis)
        self.verticalLayout_2.addLayout(self.horizontalLayout_Analysis)
        self.splitter = QtWidgets.QSplitter(WidgetAnalyze)
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidgetAnalysisSteps = QtWidgets.QTabWidget(self.splitter)
        self.tabWidgetAnalysisSteps.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidgetAnalysisSteps.sizePolicy().hasHeightForWidth())
        self.tabWidgetAnalysisSteps.setSizePolicy(sizePolicy)
        self.tabWidgetAnalysisSteps.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidgetAnalysisSteps.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidgetAnalysisSteps.setDocumentMode(False)
        self.tabWidgetAnalysisSteps.setTabBarAutoHide(False)
        self.tabWidgetAnalysisSteps.setObjectName("tabWidgetAnalysisSteps")
        self.tabTimeSlice = QtWidgets.QWidget()
        self.tabTimeSlice.setEnabled(True)
        self.tabTimeSlice.setObjectName("tabTimeSlice")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabTimeSlice)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBoxTimeAll = QtWidgets.QCheckBox(self.tabTimeSlice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxTimeAll.sizePolicy().hasHeightForWidth())
        self.checkBoxTimeAll.setSizePolicy(sizePolicy)
        self.checkBoxTimeAll.setChecked(False)
        self.checkBoxTimeAll.setObjectName("checkBoxTimeAll")
        self.horizontalLayout_7.addWidget(self.checkBoxTimeAll)
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setObjectName("formLayout_4")
        self.startLabel = QtWidgets.QLabel(self.tabTimeSlice)
        self.startLabel.setObjectName("startLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.startLabel)
        self.startSpinBox = QtWidgets.QSpinBox(self.tabTimeSlice)
        self.startSpinBox.setEnabled(True)
        self.startSpinBox.setMinimumSize(QtCore.QSize(60, 0))
        self.startSpinBox.setMinimum(1)
        self.startSpinBox.setMaximum(999999)
        self.startSpinBox.setObjectName("startSpinBox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.startSpinBox)
        self.endSpinBox = QtWidgets.QSpinBox(self.tabTimeSlice)
        self.endSpinBox.setMinimumSize(QtCore.QSize(60, 0))
        self.endSpinBox.setMinimum(1)
        self.endSpinBox.setMaximum(999999)
        self.endSpinBox.setObjectName("endSpinBox")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.endSpinBox)
        self.endLabel = QtWidgets.QLabel(self.tabTimeSlice)
        self.endLabel.setObjectName("endLabel")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.endLabel)
        self.horizontalLayout_7.addLayout(self.formLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.buttonBoxTimeSlice = QtWidgets.QDialogButtonBox(self.tabTimeSlice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBoxTimeSlice.sizePolicy().hasHeightForWidth())
        self.buttonBoxTimeSlice.setSizePolicy(sizePolicy)
        self.buttonBoxTimeSlice.setStandardButtons(QtWidgets.QDialogButtonBox.Apply)
        self.buttonBoxTimeSlice.setObjectName("buttonBoxTimeSlice")
        self.verticalLayout_3.addWidget(self.buttonBoxTimeSlice)
        self.tabWidgetAnalysisSteps.addTab(self.tabTimeSlice, "")
        self.tabCondition = QtWidgets.QWidget()
        self.tabCondition.setObjectName("tabCondition")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabCondition)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayoutCondition = QtWidgets.QFormLayout()
        self.formLayoutCondition.setObjectName("formLayoutCondition")
        self.signalTypeLabel = QtWidgets.QLabel(self.tabCondition)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signalTypeLabel.sizePolicy().hasHeightForWidth())
        self.signalTypeLabel.setSizePolicy(sizePolicy)
        self.signalTypeLabel.setObjectName("signalTypeLabel")
        self.formLayoutCondition.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.signalTypeLabel)
        self.signalTypeComboBox = QtWidgets.QComboBox(self.tabCondition)
        self.signalTypeComboBox.setObjectName("signalTypeComboBox")
        self.signalTypeComboBox.addItem("")
        self.signalTypeComboBox.addItem("")
        self.formLayoutCondition.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.signalTypeComboBox)
        self.roiCalculationLabel = QtWidgets.QLabel(self.tabCondition)
        self.roiCalculationLabel.setObjectName("roiCalculationLabel")
        self.formLayoutCondition.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.roiCalculationLabel)
        self.roiCalculationComboBox = QtWidgets.QComboBox(self.tabCondition)
        self.roiCalculationComboBox.setObjectName("roiCalculationComboBox")
        self.roiCalculationComboBox.addItem("")
        self.formLayoutCondition.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.roiCalculationComboBox)
        self.horizontalLayout_4.addLayout(self.formLayoutCondition)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBoxFilter = QtWidgets.QGroupBox(self.tabCondition)
        self.groupBoxFilter.setCheckable(True)
        self.groupBoxFilter.setObjectName("groupBoxFilter")
        self.formLayout = QtWidgets.QFormLayout(self.groupBoxFilter)
        self.formLayout.setObjectName("formLayout")
        self.filterFreqLabel = QtWidgets.QLabel(self.groupBoxFilter)
        self.filterFreqLabel.setWordWrap(True)
        self.filterFreqLabel.setObjectName("filterFreqLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.filterFreqLabel)
        self.filterFreqSpinBox = QtWidgets.QSpinBox(self.groupBoxFilter)
        self.filterFreqSpinBox.setMinimum(1)
        self.filterFreqSpinBox.setMaximum(200)
        self.filterFreqSpinBox.setProperty("value", 50)
        self.filterFreqSpinBox.setObjectName("filterFreqSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.filterFreqSpinBox)
        self.verticalLayout_5.addWidget(self.groupBoxFilter)
        self.groupBoxDetrend = QtWidgets.QGroupBox(self.tabCondition)
        self.groupBoxDetrend.setCheckable(True)
        self.groupBoxDetrend.setObjectName("groupBoxDetrend")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBoxDetrend)
        self.formLayout_2.setObjectName("formLayout_2")
        self.detrendDegreeLabel = QtWidgets.QLabel(self.groupBoxDetrend)
        self.detrendDegreeLabel.setWordWrap(True)
        self.detrendDegreeLabel.setObjectName("detrendDegreeLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.detrendDegreeLabel)
        self.detrendDegreeSpinBox = QtWidgets.QSpinBox(self.groupBoxDetrend)
        self.detrendDegreeSpinBox.setMinimum(1)
        self.detrendDegreeSpinBox.setMaximum(4)
        self.detrendDegreeSpinBox.setProperty("value", 2)
        self.detrendDegreeSpinBox.setObjectName("detrendDegreeSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.detrendDegreeSpinBox)
        self.verticalLayout_5.addWidget(self.groupBoxDetrend)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.buttonBoxCondition = QtWidgets.QDialogButtonBox(self.tabCondition)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBoxCondition.sizePolicy().hasHeightForWidth())
        self.buttonBoxCondition.setSizePolicy(sizePolicy)
        self.buttonBoxCondition.setStandardButtons(QtWidgets.QDialogButtonBox.Apply)
        self.buttonBoxCondition.setObjectName("buttonBoxCondition")
        self.verticalLayout_6.addWidget(self.buttonBoxCondition)
        self.tabWidgetAnalysisSteps.addTab(self.tabCondition, "")
        self.tabPeakDetect = QtWidgets.QWidget()
        self.tabPeakDetect.setObjectName("tabPeakDetect")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabPeakDetect)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayoutPeakDetect = QtWidgets.QFormLayout()
        self.formLayoutPeakDetect.setObjectName("formLayoutPeakDetect")
        self.thresholdLabel = QtWidgets.QLabel(self.tabPeakDetect)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thresholdLabel.sizePolicy().hasHeightForWidth())
        self.thresholdLabel.setSizePolicy(sizePolicy)
        self.thresholdLabel.setObjectName("thresholdLabel")
        self.formLayoutPeakDetect.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.thresholdLabel)
        self.thresholdDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.tabPeakDetect)
        self.thresholdDoubleSpinBox.setMinimum(0.01)
        self.thresholdDoubleSpinBox.setMaximum(0.99)
        self.thresholdDoubleSpinBox.setSingleStep(0.01)
        self.thresholdDoubleSpinBox.setProperty("value", 0.72)
        self.thresholdDoubleSpinBox.setObjectName("thresholdDoubleSpinBox")
        self.formLayoutPeakDetect.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.thresholdDoubleSpinBox)
        self.lockoutTimeLabel = QtWidgets.QLabel(self.tabPeakDetect)
        self.lockoutTimeLabel.setObjectName("lockoutTimeLabel")
        self.formLayoutPeakDetect.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lockoutTimeLabel)
        self.lockoutTimeSpinBox = QtWidgets.QSpinBox(self.tabPeakDetect)
        self.lockoutTimeSpinBox.setMinimum(1)
        self.lockoutTimeSpinBox.setMaximum(3000)
        self.lockoutTimeSpinBox.setProperty("value", 172)
        self.lockoutTimeSpinBox.setObjectName("lockoutTimeSpinBox")
        self.formLayoutPeakDetect.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lockoutTimeSpinBox)
        self.verticalLayout.addLayout(self.formLayoutPeakDetect)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonExportTrace = QtWidgets.QPushButton(self.tabPeakDetect)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonExportTrace.sizePolicy().hasHeightForWidth())
        self.pushButtonExportTrace.setSizePolicy(sizePolicy)
        self.pushButtonExportTrace.setObjectName("pushButtonExportTrace")
        self.horizontalLayout_3.addWidget(self.pushButtonExportTrace)
        self.buttonBoxPeakDetect = QtWidgets.QDialogButtonBox(self.tabPeakDetect)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBoxPeakDetect.sizePolicy().hasHeightForWidth())
        self.buttonBoxPeakDetect.setSizePolicy(sizePolicy)
        self.buttonBoxPeakDetect.setStandardButtons(QtWidgets.QDialogButtonBox.Apply)
        self.buttonBoxPeakDetect.setObjectName("buttonBoxPeakDetect")
        self.horizontalLayout_3.addWidget(self.buttonBoxPeakDetect)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tabWidgetAnalysisSteps.addTab(self.tabPeakDetect, "")
        self.tabProcess = QtWidgets.QWidget()
        self.tabProcess.setObjectName("tabProcess")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabProcess)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.processTableView = QtWidgets.QTableView(self.tabProcess)
        self.processTableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.processTableView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.processTableView.setObjectName("processTableView")
        self.verticalLayout_4.addWidget(self.processTableView)
        self.buttonBoxProcess = QtWidgets.QDialogButtonBox(self.tabProcess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBoxProcess.sizePolicy().hasHeightForWidth())
        self.buttonBoxProcess.setSizePolicy(sizePolicy)
        self.buttonBoxProcess.setStandardButtons(QtWidgets.QDialogButtonBox.Apply)
        self.buttonBoxProcess.setObjectName("buttonBoxProcess")
        self.verticalLayout_4.addWidget(self.buttonBoxProcess)
        self.tabWidgetAnalysisSteps.addTab(self.tabProcess, "")
        self.widgetPreview = GraphicsLayoutWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetPreview.sizePolicy().hasHeightForWidth())
        self.widgetPreview.setSizePolicy(sizePolicy)
        self.widgetPreview.setMinimumSize(QtCore.QSize(70, 200))
        self.widgetPreview.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widgetPreview.setObjectName("widgetPreview")
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(WidgetAnalyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(10, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonBoxAnalyze = QtWidgets.QDialogButtonBox(WidgetAnalyze)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBoxAnalyze.sizePolicy().hasHeightForWidth())
        self.buttonBoxAnalyze.setSizePolicy(sizePolicy)
        self.buttonBoxAnalyze.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBoxAnalyze.setStandardButtons(QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBoxAnalyze.setCenterButtons(False)
        self.buttonBoxAnalyze.setObjectName("buttonBoxAnalyze")
        self.horizontalLayout.addWidget(self.buttonBoxAnalyze)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(WidgetAnalyze)
        self.comboBoxROIs.setCurrentIndex(-1)
        self.comboBoxSignal.setCurrentIndex(-1)
        self.tabWidgetAnalysisSteps.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(WidgetAnalyze)

    def retranslateUi(self, WidgetAnalyze):
        _translate = QtCore.QCoreApplication.translate
        WidgetAnalyze.setWindowTitle(_translate("WidgetAnalyze", "Analyze"))
        self.labelSource.setText(_translate("WidgetAnalyze", "Source:"))
        self.labelROIs.setText(_translate("WidgetAnalyze", "ROI:"))
        self.labelSignal.setText(_translate("WidgetAnalyze", "Signal:"))
        self.labelAnalysis.setText(_translate("WidgetAnalyze", "Analysis:"))
        self.comboBoxAnalysis.setItemText(0, _translate("WidgetAnalyze", "*New*"))
        self.checkBoxTimeAll.setText(_translate("WidgetAnalyze", "Use All"))
        self.startLabel.setText(_translate("WidgetAnalyze", "Start"))
        self.endLabel.setText(_translate("WidgetAnalyze", "End"))
        self.tabWidgetAnalysisSteps.setTabText(self.tabWidgetAnalysisSteps.indexOf(self.tabTimeSlice), _translate("WidgetAnalyze", "Time Slice"))
        self.signalTypeLabel.setText(_translate("WidgetAnalyze", "Signal Type:"))
        self.signalTypeComboBox.setItemText(0, _translate("WidgetAnalyze", "Voltage (Vm)"))
        self.signalTypeComboBox.setItemText(1, _translate("WidgetAnalyze", "Calcium (Ca)"))
        self.roiCalculationLabel.setText(_translate("WidgetAnalyze", "Calculation:"))
        self.roiCalculationComboBox.setItemText(0, _translate("WidgetAnalyze", "Mean"))
        self.groupBoxFilter.setTitle(_translate("WidgetAnalyze", "Low Pass Filter"))
        self.filterFreqLabel.setText(_translate("WidgetAnalyze", "Cutoff (Hz)"))
        self.groupBoxDetrend.setTitle(_translate("WidgetAnalyze", "Detrend (Polynomial)"))
        self.detrendDegreeLabel.setText(_translate("WidgetAnalyze", "Degree"))
        self.tabWidgetAnalysisSteps.setTabText(self.tabWidgetAnalysisSteps.indexOf(self.tabCondition), _translate("WidgetAnalyze", "Condition"))
        self.thresholdLabel.setText(_translate("WidgetAnalyze", "Threshold (0 - 1)"))
        self.lockoutTimeLabel.setText(_translate("WidgetAnalyze", "Lockout Time (frames)"))
        self.pushButtonExportTrace.setText(_translate("WidgetAnalyze", "Export Trace (.csv)"))
        self.tabWidgetAnalysisSteps.setTabText(self.tabWidgetAnalysisSteps.indexOf(self.tabPeakDetect), _translate("WidgetAnalyze", "Peak Detect"))
        self.tabWidgetAnalysisSteps.setTabText(self.tabWidgetAnalysisSteps.indexOf(self.tabProcess), _translate("WidgetAnalyze", "Process"))

from pyqtgraph.widgets.GraphicsLayoutWidget import GraphicsLayoutWidget