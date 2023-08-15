# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from startUI import Ui_StartWindow
from settingUI import Ui_SettingWindow


class Ui_MainWindow(object):
    def __init__(self):
        self.window = QtWidgets.QMainWindow()

    def openstartwindow(self):
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def opensettingwindow(self):
        self.settingui = Ui_SettingWindow()
        self.settingui.setupUi(self.window)
        self.settingui.backSignal.connect(self.show)
        
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 543)
        MainWindow.setStyleSheet("background-color:rgb(101, 40, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 80, 531, 151))

        self.label.setStyleSheet("font: 75 24pt \"Bahnschrift\";\n"
"color:white;")
        self.label.setObjectName("label")
        self.settingBtn = QtWidgets.QPushButton(self.centralwidget)
        self.settingBtn.setGeometry(QtCore.QRect(260, 330, 181, 71))
        self.settingBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.settingBtn.setStyleSheet("QPushButton {\n"
"font: 18pt \"Bahnschrift Condensed\";\n"
"background-color:rgb(80, 64, 153);\n"
"color:white;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(160, 118, 249);\n"
"}\n"
"")
        self.settingBtn.setObjectName("settingBtn")
        self.settingBtn.clicked.connect(self.opensettingwindow)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(260, 250, 181, 71))
        self.startBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.startBtn.setStyleSheet("QPushButton {\n"
"font: 18pt \"Bahnschrift Condensed\";\n"
"background-color:rgb(80, 64, 153);\n"
"color:white;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(160, 118, 249);\n"
"}\n"
"")
        self.startBtn.setObjectName("startBtn")
        self.startBtn.clicked.connect(self.openstartwindow)
        self.quitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.quitBtn.setGeometry(QtCore.QRect(260, 410, 181, 71))
        self.quitBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.quitBtn.setStyleSheet("QPushButton {\n"
"font: 18pt \"Bahnschrift Condensed\";\n"
"background-color:rgb(80, 64, 153);\n"
"color:white;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(160, 118, 249);\n"
"}\n"
"")
        self.quitBtn.setObjectName("quitBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.quitBtn.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SHAPE SEGMENTATION"))
        self.settingBtn.setText(_translate("MainWindow", "Setting"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.quitBtn.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())