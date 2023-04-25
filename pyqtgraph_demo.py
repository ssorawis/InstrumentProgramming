"""Plotting Demo with pyqtgraph"""

import sys
import numpy as np
import pyqtgraph as pg
import time

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
DISPLAY_WIDTH = 500

class QtGraphWindow(QMainWindow):
    """main window (GUI or view)."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQtGraph Demo")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.generalLayout = QHBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()
        self._connect_signals()

    def _createDisplay(self):
        self.display = pg.GraphicsLayoutWidget()
        # todo: add axisitems and initialize the plots
        self.display.setFixedWidth(DISPLAY_WIDTH)
        self.display.show()
        self.generalLayout.addWidget(self.display)


    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QVBoxLayout()

        keys = ['start', 'stop']

        for key in keys:
            self.buttonMap[key] = QPushButton(key)
            buttonsLayout.addWidget(self.buttonMap[key])

        self.generalLayout.addLayout(buttonsLayout)

    def _connect_signals(self):
        self.buttonMap['start'].clicked.connect(self.meas_start)
        self.buttonMap['stop'].clicked.connect(self.meas_stop)

    def meas_start(self):
        print('start!')
        # todo: perform measurements and plot the data

        """CODE BELOW NEEDS TO BE CHANGED"""
        myai = AnalogInput()
        data = []

        for i in range(1000):
            data.append(myai.get_y())
            time.sleep(0.01)
        print(data)

    def meas_stop(self):
        print('stop!')

class AnalogInput():
    """Dummy Analog Input: Generate a Sinusoidal Function"""
    
    def __init__(self):
        self.t_init = time.time()
        
    def get_y(self):
        t = time.time()
        return 10*np.sin(2*np.pi*1.7*(t-self.t_init))
    
    def get_xy(self):
        t = time.time()
        return t-self.t_init, 10*np.sin(2*np.pi*1.7*(t-self.t_init))

def main():
    """main function."""
    pyqtApp = QApplication([])
    pyqtWindow = QtGraphWindow()
    pyqtWindow.show()
    sys.exit(pyqtApp.exec())

if __name__ == "__main__":
    main()
