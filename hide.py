import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5 import uic


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the file ui
        uic.loadUi('hide.ui',self)

        # Define Our Widgets
        self.edit = self.findChild(QLineEdit,'lineEdit')
        self.button = self.findChild(QPushButton,'pushButton')

        # Click button
        self.button.clicked.connect(self.hide_unhide)

        # Show The App
        self.setWindowTitle('Hide And Unhidden')
        self.show()

        # Keep Track of hidden or not
        self.hidden = False

    def hide_unhide(self):
        if self.hidden:
            self.hidden = False
            self.edit.show()
        else:
            self.edit.hide()
            self.hidden = True

app = QApplication(sys.argv)
uiWindow = UI()
app.exec_()