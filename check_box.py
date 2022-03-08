from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(302, 356)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.check_python = QtWidgets.QCheckBox(self.centralwidget)
        self.check_python.setGeometry(QtCore.QRect(80, 30, 167, 37))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_python.setFont(font)
        self.check_python.setObjectName("check_python")
        self.check_java = QtWidgets.QCheckBox(self.centralwidget)
        self.check_java.setGeometry(QtCore.QRect(80, 90, 79, 37))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.check_java.setFont(font)
        self.check_java.setObjectName("check_java")
        self.btn_click = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.check())
        self.btn_click.setGeometry(QtCore.QRect(110, 150, 93, 37))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_click.setFont(font)
        self.btn_click.setObjectName("btn_click")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 230, 155, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 302, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.check_python.setText(_translate("MainWindow", "Python QT5"))
        self.check_java.setText(_translate("MainWindow", "Java"))
        self.btn_click.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "You choose: "))

    def check(self):
        # State: 0 = not checked 2 = checked
        print(self.check_java.checkState())
        self.python = ''
        self.java = ''
        if self.check_python.isChecked():
            self.python = 'Python QT5'
        if self.check_java.isChecked():
            self.java = 'Java'
        self.label.setText(f'{self.python}{self.java}')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
