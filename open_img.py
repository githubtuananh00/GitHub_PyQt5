from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load ui file
        uic.loadUi('open_img.ui', self)

        # Define our Widgets
        self.button = self.findChild(QPushButton, 'pushButton')
        self.label = self.findChild(QLabel, 'label')

        # Click the dropdown Button
        self.button.clicked.connect(self.clicker)

        # show App
        self.show()

    def clicker(self):
        fname = QFileDialog.getOpenFileName(self, 'Open Image', 'D:\Baitap\Python\opencv\img-video',
                                            'All file (*);; PNG File (*.png);; JPG File (*.jpg)')

        # Open File Img
        self.pixmax = QPixmap(fname[0])
        # Add Pic to label
        self.label.setPixmap(self.pixmax)


app = QApplication(sys.argv)
uiWindow = UI()
app.exec_()
