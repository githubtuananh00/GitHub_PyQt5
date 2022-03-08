from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QTextEdit
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        # Load the ui file
        uic.loadUi('loadui.ui', self)

        # Define Our Widgets
        self.label= self.findChild(QLabel,'label')
        self.textEdit = self.findChild(QTextEdit,'textEdit')
        self.button = self.findChild(QPushButton,'pushButton')
        self.clear_btn = self.findChild(QPushButton,'pushButton_2')

        # Do something
        self.button.clicked.connect(self.clicker)
        self.clear_btn.clicked.connect(self.clearText)

        # Show the app
        self.show()

    def clicker(self):
        self.label.setText(f'Hello There {self.textEdit.toPlainText()}')
        self.textEdit.setPlainText('')

    def clearText(self):
        self.label.setText('Enter Your Name ...')
        self.textEdit.setPlainText('')


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()