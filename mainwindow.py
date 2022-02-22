# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\PermOne\Desktop\dev\PlugStat\plugstat.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QSize


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 522)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1022, 522))
        MainWindow.setMaximumSize(QSize(1022, 522))
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(16, 20, 432, 384))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lab_selectfolder = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setKerning(False)
        self.lab_selectfolder.setFont(font)
        self.lab_selectfolder.setStyleSheet("color: rgb(255, 255, 255);")
        self.lab_selectfolder.setObjectName("lab_selectfolder")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lab_selectfolder)
        self.btn_filedialog = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy ExtraBold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_filedialog.setFont(font)
        self.btn_filedialog.setStyleSheet("color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(255, 170, 0);")
        self.btn_filedialog.setAutoDefault(False)
        self.btn_filedialog.setDefault(False)
        self.btn_filedialog.setFlat(False)
        self.btn_filedialog.setObjectName("btn_filedialog")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.btn_filedialog)
        self.lab_rppdir = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setKerning(False)
        self.lab_rppdir.setFont(font)
        self.lab_rppdir.setStyleSheet("color: rgb(255, 255, 255);")
        self.lab_rppdir.setObjectName("lab_rppdir")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lab_rppdir)
        self.le_rppdir = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setBold(True)
        font.setWeight(75)
        self.le_rppdir.setFont(font)
        self.le_rppdir.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                     "color: rgb(255, 170, 0);")
        self.le_rppdir.setFrame(False)
        self.le_rppdir.setReadOnly(True)
        self.le_rppdir.setObjectName("le_rppdir")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_rppdir)
        self.lab_startdate = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setKerning(False)
        self.lab_startdate.setFont(font)
        self.lab_startdate.setStyleSheet("color: rgb(255, 255, 255);")
        self.lab_startdate.setObjectName("lab_startdate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lab_startdate)
        self.cal_startdate = QtWidgets.QCalendarWidget(self.widget)
        self.cal_startdate.setStyleSheet("color: rgb(255, 255, 255);")
        self.cal_startdate.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.cal_startdate.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.cal_startdate.setGridVisible(False)
        self.cal_startdate.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.NoHorizontalHeader)
        self.cal_startdate.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.cal_startdate.setObjectName("cal_startdate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cal_startdate)
        self.lab_selecteddate = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setKerning(False)
        self.lab_selecteddate.setFont(font)
        self.lab_selecteddate.setStyleSheet("color: rgb(255, 255, 255);")
        self.lab_selecteddate.setObjectName("lab_selecteddate")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lab_selecteddate)
        self.le_selecteddate = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_selecteddate.sizePolicy().hasHeightForWidth())
        self.le_selecteddate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setBold(True)
        font.setWeight(75)
        self.le_selecteddate.setFont(font)
        self.le_selecteddate.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                           "color: rgb(255, 170, 0);")
        self.le_selecteddate.setFrame(False)
        self.le_selecteddate.setReadOnly(True)
        self.le_selecteddate.setObjectName("le_selecteddate")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.le_selecteddate)
        self.btn_bar = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_bar.sizePolicy().hasHeightForWidth())
        self.btn_bar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setBold(True)
        font.setWeight(75)
        self.btn_bar.setFont(font)
        self.btn_bar.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_bar.setObjectName("btn_bar")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.btn_bar)
        self.btn_copyfiles = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_copyfiles.sizePolicy().hasHeightForWidth())
        self.btn_copyfiles.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setBold(True)
        font.setWeight(75)
        self.btn_copyfiles.setFont(font)
        self.btn_copyfiles.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_copyfiles.setObjectName("btn_copyfiles")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.btn_copyfiles)
        self.btn_createtxt = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setBold(True)
        font.setWeight(75)
        self.btn_createtxt.setFont(font)
        self.btn_createtxt.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_createtxt.setObjectName("btn_createtxt")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.btn_createtxt)
        self.btn_td = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_td.sizePolicy().hasHeightForWidth())
        self.btn_td.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setBold(True)
        font.setWeight(75)
        self.btn_td.setFont(font)
        self.btn_td.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_td.setObjectName("btn_td")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.btn_td)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(460, 20, 551, 471))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.dsb_threshold = QtWidgets.QDoubleSpinBox(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsb_threshold.sizePolicy().hasHeightForWidth())
        self.dsb_threshold.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        self.dsb_threshold.setFont(font)
        self.dsb_threshold.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "color: rgb(0, 0, 0);")
        self.dsb_threshold.setFrame(False)
        self.dsb_threshold.setSingleStep(0.1)
        self.dsb_threshold.setProperty("value", 0.5)
        self.dsb_threshold.setObjectName("dsb_threshold")
        self.gridLayout.addWidget(self.dsb_threshold, 2, 1, 1, 1)
        self.lab_nbrpp = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setKerning(False)
        self.lab_nbrpp.setFont(font)
        self.lab_nbrpp.setStyleSheet("color: rgb(255, 255, 255);")
        self.lab_nbrpp.setObjectName("lab_nbrpp")
        self.gridLayout.addWidget(self.lab_nbrpp, 1, 0, 1, 1)
        self.lab_search = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setKerning(False)
        self.lab_search.setFont(font)
        self.lab_search.setStyleSheet("color: rgb(255, 255, 255);")
        self.lab_search.setObjectName("lab_search")
        self.gridLayout.addWidget(self.lab_search, 3, 0, 1, 1)
        self.le_nbrpp = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setBold(True)
        font.setWeight(75)
        self.le_nbrpp.setFont(font)
        self.le_nbrpp.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                    "color: rgb(255, 170, 0);")
        self.le_nbrpp.setFrame(False)
        self.le_nbrpp.setReadOnly(True)
        self.le_nbrpp.setObjectName("le_nbrpp")
        self.gridLayout.addWidget(self.le_nbrpp, 1, 1, 1, 1)
        self.lab_threshold = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setKerning(False)
        self.lab_threshold.setFont(font)
        self.lab_threshold.setStyleSheet("color: rgb(255, 255, 255);")
        self.lab_threshold.setObjectName("lab_threshold")
        self.gridLayout.addWidget(self.lab_threshold, 2, 0, 1, 1)
        self.le_search = QtWidgets.QLineEdit(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        self.le_search.setFont(font)
        self.le_search.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(0, 0, 0);")
        self.le_search.setFrame(False)
        self.le_search.setObjectName("le_search")
        self.gridLayout.addWidget(self.le_search, 3, 1, 1, 1)
        self.btn_search = QtWidgets.QPushButton(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Gilroy")
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_search.setObjectName("btn_search")
        self.gridLayout.addWidget(self.btn_search, 3, 2, 1, 1)
        self.lab_image = QtWidgets.QLabel(self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(5000)
        sizePolicy.setVerticalStretch(5000)
        sizePolicy.setHeightForWidth(self.lab_image.sizePolicy().hasHeightForWidth())
        self.lab_image.setSizePolicy(sizePolicy)
        self.lab_image.setStyleSheet("color: rgb(0, 0, 0);")
        self.lab_image.setScaledContents(True)
        self.lab_image.setObjectName("CLICK BAR GRAPH BUTTON")
        self.gridLayout.addWidget(self.lab_image, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PlugStat"))
        self.lab_selectfolder.setText(_translate("MainWindow", "Select Reaper Project Folder :"))
        self.btn_filedialog.setText(_translate("MainWindow", "SELECT FOLDER"))
        self.lab_rppdir.setText(_translate("MainWindow", "Selected .rpp folder :"))
        self.lab_startdate.setText(_translate("MainWindow", "Select start date :"))
        self.lab_selecteddate.setText(_translate("MainWindow", "Selected start date :"))
        self.btn_bar.setText(_translate("MainWindow", "BAR GRAPH"))
        self.btn_copyfiles.setText(_translate("MainWindow", "ANALYZE"))
        self.btn_createtxt.setText(_translate("MainWindow", "PLUGINS LIST"))
        self.btn_td.setText(_translate("MainWindow", "TEMP FOLDER"))
        self.lab_nbrpp.setText(_translate("MainWindow", "Projects number :"))
        self.lab_search.setText(_translate("MainWindow", "Search Plugin :"))
        self.lab_threshold.setText(_translate("MainWindow", "Set threshold :"))
        self.btn_search.setText(_translate("MainWindow", "SEARCH"))
        self.lab_image.setText(_translate("MainWindow", "lab_image"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
