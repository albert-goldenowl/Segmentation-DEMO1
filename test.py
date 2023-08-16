import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
    def closeEvent(self, event):
        print('closed')
if __name__ == '__main__':
    app =  QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())