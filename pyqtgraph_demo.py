"""Plotting Demo with pyqtgraph"""

import sys
import numpy as np
import pyqtgraph as pg
import time
import psutil

from PyQt6.QtCore import Qt, QTimer
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
        
        # initialize data storage
        self.x = []
        self.y = []
        self.timer = QTimer()
        self.timer.setInterval(10)

        self.myai = AnalogInput()

        self._createDisplay()
        self._createButtons()
        self._connect_signals()

    def _createDisplay(self):
        self.display = pg.GraphicsLayoutWidget()
        self.plotitem = self.display.addPlot(0,0)
        self.plotitem.setLabel('bottom', 'Bottom Axis', 's')
        self.plotitem.setLabel('left', 'Left Axis', 'V')
        self.plotdataitem = self.plotitem.plot([], [], pen='r')
        

        self.plotitem2 = self.display.addPlot(1,0)
        self.plotitem2.setLabel('bottom', 'Bottom Axis', 's')
        self.plotitem2.setLabel('left', 'Left Axis', 'V')
        self.plotdataitem2 = self.plotitem2.plot([], [], pen='r')

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

        self.timer.timeout.connect(self.update_plot_data)

    def meas_start(self):

        self.x = np.array([])
        self.y = np.array([])

        self.y2 = np.array([])
        self.timer.start()

        # print('start!')
        # # todo: perform measurements and plot the data

        # """CODE BELOW NEEDS TO BE CHANGED"""
        # myai = AnalogInput()
        # data = []

        # for i in range(1000):
        #     data.append(myai.get_y())
        #     time.sleep(0.01)
        # print(data)

    def meas_stop(self):
        print('stop!')
        self.timer.stop()

    def update_plot_data(self):
        x, y = self.myai.get_xy()
        self.x = np.append(self.x, x)
        self.y = np.append(self.y, y)

        self.y2 = np.append(self.y2, psutil.virtual_memory()[2])

        self.plotdataitem.setData(self.x - self.x[0], self.y)
        self.plotdataitem2.setData(self.x - self.x[0], self.y2)

        if len(self.x) > 1000:
            self.timer.stop()

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
