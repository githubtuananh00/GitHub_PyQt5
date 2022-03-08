import sys
from datetime import datetime

from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLCDNumber


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi('lcd.ui', self)

        # Define Our Widgets
        self.lcd = self.findChild(QLCDNumber, 'lcdNumber')

        # Create timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_number)

        # Start the timer and update every second
        self.timer.start(1000)

        # Call the lcd function
        self.lcd_number()

        # Change the title and shown
        self.setWindowTitle('LCD')
        self.show()

    def lcd_number(self):
        # Get the time
        time = datetime.now()

        # Format the time
        format_time = time.strftime('%H:%M:%S')

        self.lcd.setDigitCount(8)

        self.lcd.display(format_time)


app = QApplication(sys.argv)
uiWindow = UI()
app.exec_()
