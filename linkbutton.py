from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.count=0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(663, 198)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget,clicked=lambda :self.increment())
        self.commandLinkButton.setGeometry(QtCore.QRect(30, 50, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.lbl_kq = QtWidgets.QLabel(self.centralwidget)
        self.lbl_kq.setGeometry(QtCore.QRect(340, 50, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lbl_kq.setFont(font)
        self.lbl_kq.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_kq.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_kq.setObjectName("lbl_kq")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 663, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def increment(self):
        self.count+=1
        self.lbl_kq.setText(str(self.count))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.commandLinkButton.setText(_translate("MainWindow", "Increase Counter"))
        self.lbl_kq.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
