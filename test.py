# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 717)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 371, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(420, 20, 201, 151))
        self.groupBox.setObjectName("groupBox")
        self.spinBox = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(30, 40, 45, 25))
        self.spinBox.setObjectName("spinBox")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(110, 40, 68, 25))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 190, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(450, 260, 119, 23))
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(290, 260, 101, 23))
        self.checkBox.setObjectName("checkBox")
        self.btn_function = QtWidgets.QDialogButtonBox(parent=self.centralwidget)
        self.btn_function.setGeometry(QtCore.QRect(190, 410, 441, 34))
        self.btn_function.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok|QtWidgets.QDialogButtonBox.StandardButton.Save|QtWidgets.QDialogButtonBox.StandardButton.SaveAll)
        self.btn_function.setObjectName("btn_function")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(90, 350, 120, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(300, 322, 171, 61))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 480, 68, 19))
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(60, 300, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalSlider = QtWidgets.QSlider(parent=self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(670, 200, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(500, 510, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(500, 550, 107, 107))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 540, 261, 111))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.btn_ao_start = QtWidgets.QPushButton(parent=self.tab)
        self.btn_ao_start.setGeometry(QtCore.QRect(0, 20, 112, 34))
        self.btn_ao_start.setObjectName("btn_ao_start")
        self.btn_ao_stop = QtWidgets.QPushButton(parent=self.tab)
        self.btn_ao_stop.setGeometry(QtCore.QRect(130, 20, 112, 34))
        self.btn_ao_stop.setObjectName("btn_ao_stop")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btn_ai_start = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_ai_start.setGeometry(QtCore.QRect(10, 10, 112, 34))
        self.btn_ai_start.setObjectName("btn_ai_start")
        self.btn_ai_stop = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_ai_stop.setGeometry(QtCore.QRect(130, 10, 112, 34))
        self.btn_ai_stop.setObjectName("btn_ai_stop")
        self.tabWidget.addTab(self.tab_2, "")
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(320, 480, 111, 25))
        self.spinBox_2.setObjectName("spinBox_2")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(330, 530, 111, 25))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.dial = QtWidgets.QDial(parent=self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(300, 570, 50, 64))
        self.dial.setObjectName("dial")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(370, 590, 92, 25))
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.spinBox)
        MainWindow.setTabOrder(self.spinBox, self.doubleSpinBox)
        MainWindow.setTabOrder(self.doubleSpinBox, self.verticalSlider)
        MainWindow.setTabOrder(self.verticalSlider, self.radioButton)
        MainWindow.setTabOrder(self.radioButton, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.horizontalSlider)
        MainWindow.setTabOrder(self.horizontalSlider, self.dial)
        MainWindow.setTabOrder(self.dial, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.textEdit)
        MainWindow.setTabOrder(self.textEdit, self.spinBox_2)
        MainWindow.setTabOrder(self.spinBox_2, self.doubleSpinBox_2)
        MainWindow.setTabOrder(self.doubleSpinBox_2, self.tabWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton.setText(_translate("MainWindow", "Message"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.btn_ao_start.setText(_translate("MainWindow", "Start"))
        self.btn_ao_stop.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "AO"))
        self.btn_ai_start.setText(_translate("MainWindow", "Start"))
        self.btn_ai_stop.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "AI"))
