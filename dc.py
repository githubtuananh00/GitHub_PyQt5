from PyQt5.QtWidgets import QMainWindow, QApplication, QComboBox, QLabel
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi('dc.ui', self)

        # Define Our Widgets
        self.label = self.findChild(QLabel)
        self.combox1 = self.findChild(QComboBox, 'comboBox')
        self.combox2 = self.findChild(QComboBox, 'comboBox_2')

        # Add Item to the combo box
        self.combox1.addItem('Male', ['Tuan Anh', 'Hai', 'Phuong'])
        self.combox1.addItem('Female', ['Hoa', 'Như', 'Trang'])

        # Click The Dropdown Box
        self.combox1.activated.connect(self.clicker)
        self.combox2.activated.connect(self.clicker2)

        # The show app
        self.show()

    def clicker(self, index):
        # Clear the second combo box
        self.combox2.clear()
        # Do the dependant thing
        self.combox2.addItems(self.combox1.itemData(index))

    def clicker2(self):
        self.label.setText(f'Your Picked: {self.combox2.currentText()} - {self.combox1.currentText()}')


# Initialize The app
app = QApplication(sys.argv)
uiWindow = UI()
app.exec_()
