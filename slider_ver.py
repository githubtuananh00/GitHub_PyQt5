import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load file ui
        uic.loadUi('slider_ver.ui',self)

        # Define our Widgets
        self.slider_ver = self.findChild(QSlider,'verticalSlider')
        self.label = self.findChild(QLabel, 'label')

        # set value slider_ver
        self.slider_ver.setRange(50,100)
        self.label.setText('50')

        # Move the slider_ver
        self.slider_ver.valueChanged.connect(self.slider_ver_it)


        # Show
        self.show()

    def slider_ver_it(self,value):
        self.label.setText(f'{value}')

app = QApplication(sys.argv)
uiWindow = UI()
app.exec_()