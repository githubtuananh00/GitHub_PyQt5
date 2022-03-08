from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(382, 286)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rad_cake = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_cake.setGeometry(QtCore.QRect(130, 40, 82, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.rad_cake.setFont(font)
        self.rad_cake.setObjectName("rad_cake")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 180, 237, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.rad_chicken = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_chicken.setGeometry(QtCore.QRect(130, 80, 117, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.rad_chicken.setFont(font)
        self.rad_chicken.setObjectName("rad_chicken")
        self.rad_banhmi = QtWidgets.QRadioButton(self.centralwidget)
        self.rad_banhmi.setGeometry(QtCore.QRect(130, 120, 123, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.rad_banhmi.setFont(font)
        self.rad_banhmi.setObjectName("rad_banhmi")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Update State Radio Button
        self.rad_cake.toggled.connect(lambda: self.show_radio(self.rad_cake))
        self.rad_chicken.toggled.connect(lambda: self.show_radio(self.rad_chicken))
        self.rad_banhmi.toggled.connect(lambda: self.show_radio(self.rad_banhmi))
        # function toggled nhận các tín hiệu bật tắt
        # function connect kết nối các tiến hiệu đó đền function show_radio có tham số là các radio button

        # Set default radio button
        self.rad_cake.setChecked(True)

    def show_radio(self, b):
        if b.isChecked():
            self.label.setText(f'You choose: {b.text()}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rad_cake.setText(_translate("MainWindow", "Cake"))
        self.label.setText(_translate("MainWindow", "Choose Your Topping"))
        self.rad_chicken.setText(_translate("MainWindow", "Chicken"))
        self.rad_banhmi.setText(_translate("MainWindow", "Bánh Mì"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
