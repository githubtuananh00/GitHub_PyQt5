import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QLabel
from PyQt5 import uic


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi('slide.ui', self)

        # Define Our Widgets
        self.slide = self.findChild(QSlider,'horizontalSlider')
        self.label = self.findChild(QLabel,'label')

        # Set Value Slide
        self.slide.setRange(10,150)
        self.label.setText('10')

        # Move The Slider
        self.slide.valueChanged.connect(self.slide_it)

        # Show
        self.setWindowTitle('Slide!')
        self.show()

    def slide_it(self,value):
        self.label.setText(f'{value}')

app = QApplication(sys.argv)
uiWindow = UI()
app.exec_()
