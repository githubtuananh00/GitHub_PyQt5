from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3 as sql  # import library sql
from PyQt5.QtWidgets import QMessageBox

# Create a database or connect to one
conn = sql.connect('mylist.db')
# Create a cursor (con trỏ)
c = conn.cursor()

# Create a table
c.execute("""Create table if not exists todo_list(list_item text)""")

# Commit the change
conn.commit()

# Close a database
conn.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 395)
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
        self.listWidget.setGeometry(QtCore.QRect(50, 110, 471, 221))
        self.listWidget.setObjectName("listWidget")
        self.txt_add = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_add.setGeometry(QtCore.QRect(50, 20, 471, 31))
        self.txt_add.setObjectName("txt_add")
        self.txt_save = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.save_it())
        self.txt_save.setGeometry(QtCore.QRect(410, 60, 111, 41))
        self.txt_save.setObjectName("btn_save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Grab all item from the database
        self.grab_all()

    def grab_all(self):
        # Create a database or connect to one
        conn = sql.connect('mylist.db')
        # Create a cursor (con trỏ)
        c = conn.cursor()

        # Select all item
        c.execute('Select * from todo_list')
        records = c.fetchall()  # Nạp dữ liệu

        # Commit the change
        conn.commit()

        # Close a database
        conn.close()
        # Loop through records and add the screen
        for record in records:
            self.listWidget.addItem(str(record[0]))

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

    # Save to Database
    def save_it(self):
        # Create a database or connect to one
        conn = sql.connect('mylist.db')
        # Create a cursor (con trỏ)
        c = conn.cursor()

        # Delete everything in the database tabel
        c.execute('Delete from todo_list;', )

        # Create Blank List To Hold ToDo Items
        items = []

        # Loop through the listWidget and pull out each
        for index in range(self.listWidget.count()):
            items.append(self.listWidget.item(index))
        for item in items:
            # print(item.text())
            # Add stuff the table
            c.execute('Insert into todo_list values (:item)', {
                'item': item.text()
            })

        # Commit the change
        conn.commit()

        # Close a database
        conn.close()

        # Pop up box
        msg=QMessageBox()
        msg.setWindowTitle('Saved to Database')
        msg.setText('Your Todo List Has Been Saved')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do list"))
        self.btn_add.setText(_translate("MainWindow", "Add Items to List"))
        self.btn_delete.setText(_translate("MainWindow", "Delete Items Form List"))
        self.btn_clearall.setText(_translate("MainWindow", "Clear The List"))
        self.txt_save.setText(_translate("MainWindow", "Save to Database"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
