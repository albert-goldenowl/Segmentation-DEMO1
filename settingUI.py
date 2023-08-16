# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PIL import ImageColor




class Ui_SettingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        with open('colors.txt', 'r') as f:
            self.colors = f.readlines()
        self.square = self.colors[0].replace('(','').replace(')','').split(',')
        self.circle = self.colors[1].replace('(','').replace(')','').split(',')
        self.triangle = self.colors[2].replace('(','').replace(')','').split(',')
        self.star = self.colors[3].replace('(','').replace(')','').split(',')
        self.square_setting = f'({int(self.square[0])}, {int(self.square[1])}, {int(self.square[2])})'
        self.circle_setting = f'({int(self.circle[0])}, {int(self.circle[1])}, {int(self.circle[2])})'
        self.triangle_setting = f'({int(self.triangle[0])}, {int(self.triangle[1])}, {int(self.triangle[2])})'
        self.star_setting = f'({int(self.star[0])}, {int(self.star[1])}, {int(self.star[2])})'
        self.setupUi()
    def setupUi(self):
        
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.setStyleSheet("background-color:rgb(101, 40, 247);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.squareFrame = QtWidgets.QFrame(self.centralwidget)
        self.squareFrame.setGeometry(QtCore.QRect(190, 110, 120, 80))
        self.squareFrame.setStyleSheet("background-color:rgb%s;\n" 
"" % self.square_setting)

        self.squareFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.squareFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.squareFrame.setObjectName("squareFrame")
        self.circleFrame = QtWidgets.QFrame(self.centralwidget)
        self.circleFrame.setGeometry(QtCore.QRect(190, 230, 120, 80))
        self.circleFrame.setStyleSheet("background-color:rgb%s\n"
"" % self.circle_setting)
        self.circleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.circleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circleFrame.setObjectName("circleFrame")
        self.triangleFrame = QtWidgets.QFrame(self.centralwidget)
        self.triangleFrame.setGeometry(QtCore.QRect(190, 350, 120, 80))
        self.triangleFrame.setStyleSheet("background-color:rgb%s\n"
"" % self.triangle_setting)
        self.triangleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.triangleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.triangleFrame.setObjectName("triangleFrame")
        self.starFrame = QtWidgets.QFrame(self.centralwidget)
        self.starFrame.setGeometry(QtCore.QRect(190, 470, 120, 80))
        self.starFrame.setStyleSheet("background-color:rgb%s" % self.star_setting)
        self.starFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.starFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.starFrame.setObjectName("starFrame")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 80, 71, 21))
        self.label.setStyleSheet("font: italic 16pt \"Ubuntu\";\n"
"color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 200, 66, 17))
        self.label_2.setStyleSheet("font: italic 16pt \"Ubuntu\";\n"
"color:white;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 310, 81, 31))
        self.label_3.setStyleSheet("font: italic 16pt \"Ubuntu\";\n"
"color:white;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 440, 66, 17))
        self.label_4.setStyleSheet("font: italic 16pt \"Ubuntu\";\n"
"color:white;")
        self.label_4.setObjectName("label_4")
        self.squareBtn = QtWidgets.QPushButton(self.centralwidget)
        self.squareBtn.setGeometry(QtCore.QRect(390, 110, 191, 71))
        self.squareBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.squareBtn.setStyleSheet("QPushButton {\n"
"font: 18pt \"Bahnschrift Condensed\";\n"
"background-color:rgb(80, 64, 153);\n"
"color:white;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(160, 118, 249);\n"
"}\n"
"")
        self.squareBtn.setObjectName("squareBtn")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 10, 511, 61))
        self.label_5.setStyleSheet("font: 75 24pt \"Bahnschrift\";\n"
"color:white;")
        self.label_5.setObjectName("label_5")
        self.circleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.circleBtn.setGeometry(QtCore.QRect(390, 230, 191, 71))
        self.circleBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.circleBtn.setStyleSheet("QPushButton {\n"
"font: 18pt \"Bahnschrift Condensed\";\n"
"background-color:rgb(80, 64, 153);\n"
"color:white;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(160, 118, 249);\n"
"}\n"
"")
        self.circleBtn.setObjectName("circleBtn")
        self.triangleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.triangleBtn.setGeometry(QtCore.QRect(390, 350, 191, 71))
        self.triangleBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.triangleBtn.setStyleSheet("QPushButton {\n"
"font: 18pt \"Bahnschrift Condensed\";\n"
"background-color:rgb(80, 64, 153);\n"
"color:white;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(160, 118, 249);\n"
"}\n"
"")
        self.triangleBtn.setObjectName("triangleBtn")
        self.starBtn = QtWidgets.QPushButton(self.centralwidget)
        self.starBtn.setGeometry(QtCore.QRect(390, 470, 191, 71))
        self.starBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.starBtn.setStyleSheet("QPushButton {\n"
"font: 18pt \"Bahnschrift Condensed\";\n"
"background-color:rgb(80, 64, 153);\n"
"color:white;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(160, 118, 249);\n"
"}\n"
"")
        self.starBtn.setObjectName("starBtn")
        self.okBtn = QtWidgets.QPushButton(self.centralwidget)
        self.okBtn.setGeometry(QtCore.QRect(680, 540, 101, 41))
        self.okBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.okBtn.setStyleSheet("QPushButton {\n"
"font: 18pt \"Bahnschrift Condensed\";\n"
"background-color:rgb(80, 64, 153);\n"
"color:white;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(160, 118, 249);\n"
"}\n"
"")
        self.okBtn.setObjectName("okBtn")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.okBtn.clicked.connect(self.close) # type: ignore
        self.squareBtn.clicked.connect(self.colorpicker_square)
        self.circleBtn.clicked.connect(self.colorpicker_circle)
        self.triangleBtn.clicked.connect(self.colorpicker_triangle)
        self.starBtn.clicked.connect(self.colorpicker_star)
        QtCore.QMetaObject.connectSlotsByName(self)
    def colorpicker_square(self):
        col = QColorDialog.getColor()
        if col.isValid():
            rgb_square = ImageColor.getcolor(col.name(), "RGB")
            self.colors[0] = str(rgb_square) + '\n'
            with open('colors.txt', 'w') as f:
                f.writelines(self.colors)
            self.squareFrame.setStyleSheet("background-color: %s;\n" % col.name())
    def colorpicker_circle(self):
        col = QColorDialog.getColor()
        if col.isValid():
            rgb_circle = ImageColor.getcolor(col.name(), "RGB")
            self.colors[1] = str(rgb_circle) + '\n'
            with open('colors.txt', 'w') as f:
                f.writelines(self.colors)
            self.circleFrame.setStyleSheet("background-color: %s;\n" % col.name())
    def colorpicker_triangle(self):
        col = QColorDialog.getColor()
        if col.isValid():
            rgb_triangle = ImageColor.getcolor(col.name(), "RGB")
            self.colors[2] = str(rgb_triangle) + '\n'
            with open('colors.txt', 'w') as f:
                f.writelines(self.colors)
            self.triangleFrame.setStyleSheet("background-color: %s;\n" % col.name())
    def colorpicker_star(self):
        col = QColorDialog.getColor()
        if col.isValid():
            rgb_star = ImageColor.getcolor(col.name(), "RGB")
            self.colors[3] = str(rgb_star) + '\n'
            with open('colors.txt', 'w') as f:
                f.writelines(self.colors)
            self.starFrame.setStyleSheet("background-color: %s;\n" % col.name())
    

        

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Setting"))
        self.label.setText(_translate("MainWindow", "Square"))
        self.label_2.setText(_translate("MainWindow", "Circle"))
        self.label_3.setText(_translate("MainWindow", "Triangle"))
        self.label_4.setText(_translate("MainWindow", "Star"))
        self.squareBtn.setText(_translate("MainWindow", "Change color"))
        self.label_5.setText(_translate("MainWindow", "SETTING COLORS FOR SHAPES"))
        self.circleBtn.setText(_translate("MainWindow", "Change color"))
        self.triangleBtn.setText(_translate("MainWindow", "Change color"))
        self.starBtn.setText(_translate("MainWindow", "Change color"))
        self.okBtn.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    ui = Ui_SettingWindow()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
