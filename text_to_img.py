import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw, ImageFont


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi('text_to_img.ui', self)

        # Define Our Widgets
        self.label = self.findChild(QLabel, 'label')
        self.button = self.findChild(QPushButton, 'pushButton')
        self.text_edit = self.findChild(QLineEdit, 'lineEdit')

        # Click the button
        self.button.clicked.connect(self.addText)

        # Show
        self.setWindowTitle('Text to Image')
        self.show()

    def addText(self):
        # Grab the text
        my_text = self.text_edit.text()

        # Open the Image
        my_img = Image.open('../opencv/img-video/vhl.jpg')

        # Define the font
        text_font = ImageFont.truetype('arial', 46)

        # Edit Image
        edit_image = ImageDraw.Draw(my_img)
        edit_image.text(xy=(250, 400), text=my_text, fill='red', font=text_font)

        # Save Image
        my_img.save('../opencv/img-video/vhl2.jpg')

        # Update Our app Image
        pixmap = QPixmap('../opencv/img-video/vhl2.jpg')
        self.label.setPixmap(pixmap)

        # Clear text
        self.text_edit.setText('')


app = QApplication(sys.argv)
uiWindow = UI()
app.exec_()
