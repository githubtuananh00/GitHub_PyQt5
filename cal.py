from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QLabel
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load file ui
        uic.loadUi('cal.ui', self)

        # Define Our Widgets
        self.calendar = self.findChild(QCalendarWidget, 'calendarWidget')
        self.label = self.findChild(QLabel, 'label')
        
        # Connect Calendar to the function
        self.calendar.selectionChanged.connect(self.grab_date)

        # Change the title and show
        self.setWindowTitle('calendar')
        self.show()

    def grab_date(self):
        dateSelected = self.calendar.selectedDate()

        # Put to label
        self.label.setText(str(dateSelected.toString()))

app = QApplication(sys.argv)
uiWindow = UI()
app.exec_()