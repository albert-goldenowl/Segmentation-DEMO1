# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startUI_updated.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import typing
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import cv2
from PyQt5 import QtCore
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import time
import onnxruntime as ort

frame_shape = (640, 481)
target_shape = (256, 256, 3)
half_width = target_shape[0] // 2
half_height = target_shape[1] // 2
x0 = frame_shape[0] // 2 - half_width
y0 = frame_shape[1] // 2 - half_height
x1 = frame_shape[0] // 2 + half_width
y1 = frame_shape[1] // 2 + half_height

background = -1
ort_session = ort.InferenceSession('model.onnx')
input_name = ort_session.get_inputs()[0].name
output_name = ort_session.get_outputs()[0].name
def create_img(mask_output, square, circle, triangle, star):
    r = np.zeros((256, 256), dtype=np.uint8)
    g = np.zeros((256, 256), dtype=np.uint8)
    b = np.zeros((256, 256), dtype=np.uint8)
    r[mask_output == 1] = int(square[0])
    r[mask_output == 2] = int(circle[0])
    r[mask_output == 3] = int(triangle[0])
    r[mask_output == 4] = int(star[0])

    g[mask_output == 1] = int(square[1])
    g[mask_output == 2] = int(circle[1])
    g[mask_output == 3] = int(triangle[1])
    g[mask_output == 4] = int(star[1])

    b[mask_output == 1] = int(square[2])
    b[mask_output == 2] = int(circle[2])
    b[mask_output == 3] = int(triangle[2])
    b[mask_output == 4] = int(star[2])

    output = np.stack([b, g, r], axis=-1)
    return output
def create_img_bg(roi, mask_output, square, circle, triangle, star):
    b, g, r = cv2.split(roi)
    r[mask_output == 1] = int(square[0])
    r[mask_output == 2] = int(circle[0])
    r[mask_output == 3] = int(triangle[0])
    r[mask_output == 4] = int(star[0])

    g[mask_output == 1] = int(square[1])
    g[mask_output == 2] = int(circle[1])
    g[mask_output == 3] = int(triangle[1])
    g[mask_output == 4] = int(star[1])

    b[mask_output == 1] = int(square[2])
    b[mask_output == 2] = int(circle[2])
    b[mask_output == 3] = int(triangle[2])
    b[mask_output == 4] = int(star[2])

    output = np.stack([b, g, r], axis=-1)
    return output
class Ui_StartWindow(QMainWindow):
    backSignal = pyqtSignal()
    def __init__(self):
        super().__init__()
    # def openmainwindow(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_MainWindow()
    #     self.ui.setupUi(self.window)
    #     MainWindow.hide()
    #     self.window.show()
        self.setupUi()
    def closeEvent(self,  event):
        self.goBack()
    def goBack(self):
        self.hide()
        self.close_webcam()
        self.backSignal.emit()
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(728, 669)
        self.setStyleSheet("background-color:rgb(101, 40, 247);")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(589, 580, 121, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
"font: 18pt \"Bahnschrift Condensed\";\n"
"background-color:rgb(80, 64, 153);\n"
"color:white;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(160, 118, 249);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 640, 481))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(3)
        self.label.setMidLineWidth(3)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(429, 580, 141, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"font: 10pt \"Bahnschrift Condensed\";\n"
"background-color:rgb(80, 64, 153);\n"
"color:white;\n"
"border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(160, 118, 249);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.camera = Camera()  
        self.camera.image.connect(self.update_image)
        self.camera.start()
        self.pushButton_2.clicked.connect(self.toggle_background)
        self.retranslateUi()
        self.pushButton.clicked.connect(self.goBack) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)
    def close_webcam(self):
        self.close()
        self.camera.stop()
    def toggle_background(self):
        self.camera.background = -self.camera.background
    def update_image(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(image))

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Webcam"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton_2.setText(_translate("MainWindow", "Toggle background/\n"
"black"))
class Camera(QThread):
    image = pyqtSignal(np.ndarray)
    background = -1
    def __init__(self):
        super().__init__()
        self.flag = True
        with open('colors.txt', 'r') as f:
            self.colors = f.readlines()
        self.square = self.colors[0].replace('(','').replace(')','').split(',')
        self.circle = self.colors[1].replace('(','').replace(')','').split(',')
        self.triangle = self.colors[2].replace('(','').replace(')','').split(',')
        self.star = self.colors[3].replace('(','').replace(')','').split(',')
    def run(self):
        prev_time = 0 
        new_time = 0
        self.capture = cv2.VideoCapture(0)
        while self.flag == True:
            ret, frame = self.capture.read()
            if ret:
                sample_window = frame[y0:y0+target_shape[1], x0:x0+target_shape[0]].copy()
                
                input_to_model = cv2.cvtColor(sample_window, cv2.COLOR_BGR2RGB)
                input_to_model = input_to_model.astype(np.float32) / 255.0
                input_to_model = np.expand_dims(input_to_model, axis=0)
                y_pred = ort_session.run([output_name], {input_name: input_to_model})
                res = np.argmax(y_pred[0][0], axis=-1)
                mask_output = create_img(res, self.square, self.circle, self.triangle, self.star)
                cv2.rectangle(frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
                if self.background == -1:
                    pass
                    # cv2.putText(frame, 'Black mode', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
                    
                else:
                    # cv2.putText(frame, 'Background mode', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
                    mask_output = create_img_bg(sample_window, res, self.square, self.circle, self.triangle, self.star)
                frame[y0:y0+target_shape[1], x0:x0+target_shape[0]] = mask_output
                frame = cv2.flip(frame, 1)
                new_time = time.time()
                fps = str(int(1 / (new_time - prev_time)))
                cv2.putText(frame, str(int(fps)), (5, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 1)
                prev_time = new_time
                k = cv2.waitKey(1)
                self.image.emit(frame)
            else:
                break
    def stop(self):
        self.flag = False
        self.capture.release()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui =  Ui_StartWindow()
    ui.show()
    sys.exit(app.exec_())
