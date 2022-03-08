from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load file ui
        uic.loadUi('menu.ui',self)

        # Add the Menu Triggers
        self.actionBlack.triggered.connect(lambda :self.change('black'))
        self.actionGreen.triggered.connect(lambda :self.change('green'))
        self.actionYellow.triggered.connect(lambda :self.change('yellow'))
        self.actionRed.triggered.connect(lambda :self.change('red'))
        self.actionWhite.triggered.connect(lambda :self.change('white'))
        self.actionBlue.triggered.connect(lambda :self.change('blue'))

        # Show app
        self.setWindowTitle('Change Color')
        self.show()

    def change(self, color):
        self.setStyleSheet(f'background: {color};')

app = QApplication(sys.argv)
uiWindown = UI()
app.exec_()