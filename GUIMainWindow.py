# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1320, 775)
        MainWindow.setMinimumSize(QtCore.QSize(1320, 775))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_canvas = QtWidgets.QVBoxLayout()
        self.verticalLayout_canvas.setObjectName("verticalLayout_canvas")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_canvas.addItem(spacerItem)
        self.horizontalLayout_10.addLayout(self.verticalLayout_canvas)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_grid = QtWidgets.QCheckBox(self.widget)
        self.checkBox_grid.setChecked(True)
        self.checkBox_grid.setObjectName("checkBox_grid")
        self.horizontalLayout_3.addWidget(self.checkBox_grid)
        self.checkBox_history = QtWidgets.QCheckBox(self.widget)
        self.checkBox_history.setChecked(True)
        self.checkBox_history.setObjectName("checkBox_history")
        self.horizontalLayout_3.addWidget(self.checkBox_history)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.combo_switch_surface = QtWidgets.QComboBox(self.widget)
        self.combo_switch_surface.setObjectName("combo_switch_surface")
        self.combo_switch_surface.addItem("")
        self.combo_switch_surface.addItem("")
        self.horizontalLayout_9.addWidget(self.combo_switch_surface)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.btn_start_edits = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_start_edits.setFont(font)
        self.btn_start_edits.setStyleSheet("")
        self.btn_start_edits.setObjectName("btn_start_edits")
        self.verticalLayout.addWidget(self.btn_start_edits)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.btn_cancel = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_8.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.btn_apply_edits = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_apply_edits.setFont(font)
        self.btn_apply_edits.setObjectName("btn_apply_edits")
        self.verticalLayout.addWidget(self.btn_apply_edits)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.btn_undo = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_undo.setFont(font)
        self.btn_undo.setObjectName("btn_undo")
        self.horizontalLayout_6.addWidget(self.btn_undo)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.btn_plot_from_file = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_plot_from_file.setFont(font)
        self.btn_plot_from_file.setObjectName("btn_plot_from_file")
        self.verticalLayout.addWidget(self.btn_plot_from_file)
        self.btn_run_profoil = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_run_profoil.setFont(font)
        self.btn_run_profoil.setStyleSheet("background-color:yellowgreen;")
        self.btn_run_profoil.setObjectName("btn_run_profoil")
        self.verticalLayout.addWidget(self.btn_run_profoil)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.btn_revert = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_revert.setFont(font)
        self.btn_revert.setObjectName("btn_revert")
        self.horizontalLayout_7.addWidget(self.btn_revert)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.lbl_summary = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        self.lbl_summary.setFont(font)
        self.lbl_summary.setWordWrap(True)
        self.lbl_summary.setObjectName("lbl_summary")
        self.verticalLayout.addWidget(self.lbl_summary)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        self.horizontalLayout_10.setStretch(0, 6)
        self.horizontalLayout_10.setStretch(1, 1)
        self.tabWidget.addTab(self.widget, "")
        self.widget1 = QtWidgets.QWidget()
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit_profoil_log = QtWidgets.QPlainTextEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        self.plainTextEdit_profoil_log.setFont(font)
        self.plainTextEdit_profoil_log.setReadOnly(True)
        self.plainTextEdit_profoil_log.setPlainText("")
        self.plainTextEdit_profoil_log.setObjectName("plainTextEdit_profoil_log")
        self.gridLayout.addWidget(self.plainTextEdit_profoil_log, 1, 1, 1, 1)
        self.plainTextEdit_profoil_in = QtWidgets.QPlainTextEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(8)
        self.plainTextEdit_profoil_in.setFont(font)
        self.plainTextEdit_profoil_in.setPlainText("")
        self.plainTextEdit_profoil_in.setObjectName("plainTextEdit_profoil_in")
        self.gridLayout.addWidget(self.plainTextEdit_profoil_in, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.btn_save_profoil_in = QtWidgets.QPushButton(self.widget1)
        self.btn_save_profoil_in.setObjectName("btn_save_profoil_in")
        self.horizontalLayout_2.addWidget(self.btn_save_profoil_in)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.widget1, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.setStretch(0, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1320, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOverlay = QtWidgets.QMenu(self.menubar)
        self.menuOverlay.setObjectName("menuOverlay")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionProfoil_dat_File = QtWidgets.QAction(MainWindow)
        self.actionProfoil_dat_File.setObjectName("actionProfoil_dat_File")
        self.actionClear_Overlay = QtWidgets.QAction(MainWindow)
        self.actionClear_Overlay.setObjectName("actionClear_Overlay")
        self.actionXFoil_dat_File = QtWidgets.QAction(MainWindow)
        self.actionXFoil_dat_File.setObjectName("actionXFoil_dat_File")
        self.actionMSES_dat_File = QtWidgets.QAction(MainWindow)
        self.actionMSES_dat_File.setObjectName("actionMSES_dat_File")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuOverlay.addAction(self.actionProfoil_dat_File)
        self.menuOverlay.addAction(self.actionXFoil_dat_File)
        self.menuOverlay.addAction(self.actionClear_Overlay)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOverlay.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PROFOIL-UI"))
        self.checkBox_grid.setText(_translate("MainWindow", "Grid"))
        self.checkBox_history.setText(_translate("MainWindow", "History"))
        self.label_4.setText(_translate("MainWindow", "Surface"))
        self.combo_switch_surface.setItemText(0, _translate("MainWindow", "Upper"))
        self.combo_switch_surface.setItemText(1, _translate("MainWindow", "Lower"))
        self.btn_start_edits.setText(_translate("MainWindow", "Start Edits"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
        self.btn_apply_edits.setText(_translate("MainWindow", "Apply Edits"))
        self.btn_undo.setText(_translate("MainWindow", "Undo"))
        self.btn_plot_from_file.setText(_translate("MainWindow", "Plot From File"))
        self.btn_run_profoil.setText(_translate("MainWindow", "Run Profoil"))
        self.btn_revert.setText(_translate("MainWindow", "Revert"))
        self.lbl_summary.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "Design View"))
        self.btn_save_profoil_in.setText(_translate("MainWindow", "Save"))
        self.label.setText(_translate("MainWindow", "Profoil.in"))
        self.label_2.setText(_translate("MainWindow", "Profoil.log"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget1), _translate("MainWindow", "File View"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOverlay.setTitle(_translate("MainWindow", "Overlay"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionProfoil_dat_File.setText(_translate("MainWindow", "Geometry from *.xy file (no header line)"))
        self.actionClear_Overlay.setText(_translate("MainWindow", "Clear Overlay"))
        self.actionXFoil_dat_File.setText(_translate("MainWindow", "Geometry from *.dat file (1 header line)"))
        self.actionMSES_dat_File.setText(_translate("MainWindow", "MSES *.dat File"))
