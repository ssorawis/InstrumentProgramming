
import test as test_ui

import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QApplication, QMainWindow, QStatusBar
import pyqtgraph as pg


def my_excepthook(type, value, tback):
    sys.__excepthook__(type, value, tback)


sys.excepthook = my_excepthook


class MyTestGUI(QtWidgets.QMainWindow, test_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.setupUi(self)

        self.btn_ai_stop.clicked.connect(self.myfunction)

    def myfunction(self):
        print('do something')


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QWidget{font-size:10px}")
    app.lastWindowClosed.connect(app.quit)
    form = MyTestGUI()
    form.show()

    app.exec()


main()
