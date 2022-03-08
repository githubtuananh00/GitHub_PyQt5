from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load ui file
        uic.loadUi('open_file.ui', self)

        # Define Our Widgets
        self.button = self.findChild(QPushButton, 'pushButton')
        self.label = self.findChild(QLabel, 'label')

        # Click the DropDown Button
        self.button.clicked.connect(self.clicker)

        # Show app
        self.show()

    def clicker(self):
        # self.label.setText('You click the button')
        # Open File Dialog
        fname = QFileDialog.getOpenFileName(self,'Open File','c:/','All File (*);;Python FIle (*.py)')
        # Tham số 2: Tên title
        # Tham số 3: Đường dẫn muốn mở file
        # Tham số 4: Các loại File

        # Output file the screen
        if fname:
            self.label.setText(str(fname[0]))


app = QApplication(sys.argv)
uiWindow = UI()
app.exec_()
