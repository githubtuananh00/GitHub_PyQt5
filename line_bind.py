import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5 import uic


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi('line_bind.ui', self)

        # Define our Widgets
        self.label = self.findChild(QLabel,'label')
        self.line_edit = self.findChild(QLineEdit,'lineEdit')

        # Hit Endter Button
        self.line_edit.editingFinished.connect(self.hitEnter)

        # Event change text
        self.line_edit.textChanged.connect(self.changeText)

        # Show
        self.setWindowTitle('Line Bind')
        self.show()

    def hitEnter(self):
        self.label.setText(self.line_edit.text())
        # self.line_edit.setText('')

    def changeText(self):
        self.label.setText(self.line_edit.text())

app = QApplication(sys.argv)
uiWindow = UI()
app.exec_()
