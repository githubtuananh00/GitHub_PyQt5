from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi('XO.ui', self)

        # Define Counter
        self.counter = 0

        # Define our Widgets
        self.button1 = self.findChild(QPushButton, 'pushButton_1')
        self.button2 = self.findChild(QPushButton, 'pushButton_2')
        self.button3 = self.findChild(QPushButton, 'pushButton_3')
        self.button4 = self.findChild(QPushButton, 'pushButton_4')
        self.button5 = self.findChild(QPushButton, 'pushButton_5')
        self.button6 = self.findChild(QPushButton, 'pushButton_6')
        self.button7 = self.findChild(QPushButton, 'pushButton_7')
        self.button8 = self.findChild(QPushButton, 'pushButton_8')
        self.button9 = self.findChild(QPushButton, 'pushButton_9')
        self.btn_start = self.findChild(QPushButton, 'btn_start')
        self.label = self.findChild(QLabel, 'label')

        # Click The Button
        self.button1.clicked.connect(lambda: self.clicker(self.button1))
        self.button2.clicked.connect(lambda: self.clicker(self.button2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))
        self.btn_start.clicked.connect(self.reset)

        # Show the app
        self.show()

    # Check win
    def check_win(self):
        # Across
        if self.button1.text() != '' and self.button1.text() == self.button5.text() and self.button1.text() == self.button6.text():
            self.winer(self.button1, self.button5, self.button6)

        if self.button2.text() != '' and self.button2.text() == self.button4.text() and self.button2.text() == self.button9.text():
            self.winer(self.button2, self.button4, self.button9)

        if self.button3.text() != '' and self.button3.text() == self.button7.text() and self.button3.text() == self.button8.text():
            self.winer(self.button3, self.button7, self.button8)

        # Down
        if self.button1.text() != '' and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text():
            self.winer(self.button1, self.button2, self.button3)

        if self.button4.text() != '' and self.button4.text() == self.button7.text() and self.button4.text() == self.button6.text():
            self.winer(self.button4, self.button7, self.button6)

        if self.button5.text() != '' and self.button5.text() == self.button9.text() and self.button5.text() == self.button8.text():
            self.winer(self.button5, self.button9, self.button8)

        # Diagonal
        if self.button1.text() != '' and self.button1.text() == self.button4.text() and self.button1.text() == self.button8.text():
            self.winer(self.button1, self.button4, self.button8)

        if self.button3.text() != '' and self.button3.text() == self.button5.text() and self.button3.text() == self.button4.text():
            self.winer(self.button3, self.button5, self.button4)
    def winer(self, a, b, c):
        # Change to button color to red
        a.setStyleSheet('QPushButton {color: red;}')
        b.setStyleSheet('QPushButton {color: red;}')
        c.setStyleSheet('QPushButton {color: red;}')
        self.label.setText(f'{a.text()} Wins!')

        self.disable()

    def clicker(self, b):
        if self.counter % 2 == 0:
            mark = 'X'
            self.label.setText("O's Turn")
        else:
            mark = 'O'
            self.label.setText("X's Turn")
        b.setText(mark)
        b.setEnabled(False)
        self.counter += 1

        self.check_win()



    def disable(self):
        button_list = [self.button1,
                       self.button9,
                       self.button8,
                       self.button3,
                       self.button4,
                       self.button2,
                       self.button5,
                       self.button6,
                       self.button7]
        for b in button_list:
            b.setEnabled(False)

    # Start Over
    def reset(self):
        button_list = [self.button1,
                       self.button9,
                       self.button8,
                       self.button3,
                       self.button4,
                       self.button2,
                       self.button5,
                       self.button6,
                       self.button7]
        for b in button_list:
            b.setText('')
            b.setEnabled(True)
            self.counter = 0
            self.label.setText('X Goes First')

            # Reset The Button Color
            b.setStyleSheet('QPushButton {color: #797979;}')



app = QApplication(sys.argv)
uiWindow = UI()
app.exec_()
