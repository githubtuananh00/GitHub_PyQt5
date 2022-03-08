from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(461, 395)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_it())
        self.btn_add.setGeometry(QtCore.QRect(50, 60, 121, 41))
        self.btn_add.setObjectName("btn_add")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_it())
        self.btn_delete.setGeometry(QtCore.QRect(170, 60, 151, 41))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_clearall = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_it())
        self.btn_clearall.setGeometry(QtCore.QRect(320, 60, 91, 41))
        self.btn_clearall.setObjectName("btn_clearall")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 110, 361, 221))
        self.listWidget.setObjectName("listWidget")
        self.txt_add = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_add.setGeometry(QtCore.QRect(50, 20, 361, 31))
        self.txt_add.setObjectName("txt_add")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 461, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Add items to list
    def add_it(self):
        # Grab the items from the list box
        items = self.txt_add.text()

        # Add Items to List
        self.listWidget.addItem(items)

        # Clear Items to the list box
        self.txt_add.setText('')

    # Delete Items from List
    def delete_it(self):
        # Grab the select row or current now
        index_row = self.listWidget.currentRow()  # Lay index dong

        # Delete select row
        self.listWidget.takeItem(index_row)

    # Clear Items to List
    def clear_it(self):
        self.listWidget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do list"))
        self.btn_add.setText(_translate("MainWindow", "Add Items to List"))
        self.btn_delete.setText(_translate("MainWindow", "Delete Items Form List"))
        self.btn_clearall.setText(_translate("MainWindow", "Clear The List"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
