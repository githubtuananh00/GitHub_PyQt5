import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMdiArea, QMdiSubWindow, QTextEdit
from PyQt5 import uic


class UI(QMainWindow):
    count = 0

    def __init__(self):
        super(UI, self).__init__()

        # Load the file ui
        uic.loadUi('new_win.ui', self)

        # Define Our Widgets
        self.mdi = self.findChild(QMdiArea, 'mdiArea')
        self.label = self.findChild(QLabel, 'label')
        self.button = self.findChild(QPushButton, 'pushButton')

        # Click button
        self.button.clicked.connect(self.add_window)
        # Show
        self.show()

    def add_window(self):
        UI.count += 1
        # Create sub window
        sub = QMdiSubWindow()

        # Do stuff in the sub window
        sub.setWidget(QTextEdit())

        # Set the titlebar or Sub Window
        sub.setWindowTitle(f'Subby Window {UI.count}')

        # Add Sub Window Into MDI Widget
        self.mdi.addSubWindow(sub)

        # Show the new sub window
        sub.show()

        # Position sub window
        # tile them
        # self.mdi.tileSubWindows()

        # Cascade them
        self.mdi.cascadeSubWindows()

app = QApplication(sys.argv)
uiWindow = UI()
app.exec_()
