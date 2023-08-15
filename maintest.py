import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from mainUI import Ui_MainWindow
from settingUI import Ui_SettingWindow
from startUI import Ui_StartWindow

class mainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.startBtn.clicked.connect(self.hide)
class settingWindow(QtWidgets.QMainWindow, Ui_SettingWindow):
    def __init__(self, parent=None):
        super(settingWindow, self).__init__(parent)
        self.setupUi(self)
        self.okBtn.clicked.connect(self.hide)
class Manager:
    def __init__(self):
        self.main = mainWindow()
        self.setting = settingWindow()
        self.main.startBtn.clicked.connect(self.setting.show)
        self.setting.okBtn.clicked.connect(self.main.show)
        self.main.show()
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())
