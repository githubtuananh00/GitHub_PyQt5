import sys

import language as language
from googletrans import LANGUAGES
import textblob

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QTextEdit, QMessageBox
from PyQt5 import uic


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the file ui
        uic.loadUi('translate.ui', self)

        # Define our Widgets
        self.t_button = self.findChild(QPushButton, 'pushButton')
        self.c_button = self.findChild(QPushButton, 'pushButton_2')

        self.combox_1 = self.findChild(QComboBox, 'comboBox')
        self.combox_2 = self.findChild(QComboBox, 'comboBox_2')

        self.text_1 = self.findChild(QTextEdit, 'textEdit')
        self.text_2 = self.findChild(QTextEdit, 'textEdit_2')

        # Click button
        self.t_button.clicked.connect(self.translate)
        self.c_button.clicked.connect(self.clear)

        # Add language to comboBox
        self.language = LANGUAGES

        # Convert to list
        self.language_list = list(self.language.values())
        # print(self.language_list)

        # Add items to comboBox
        self.combox_1.addItems(self.language_list)
        self.combox_2.addItems(self.language_list)

        # Set default comboBox
        self.combox_1.setCurrentText('english')
        self.combox_2.setCurrentText('vietnamese')


        # Show
        self.show()

    def clear(self):
        self.text_1.setText('')
        self.text_2.setText('')
        self.combox_1.setCurrentText('english')
        self.combox_2.setCurrentText('vietnamese')

    def translate(self):
        try:
            from_language_key = to_language_key = ''
            for key, value in self.language.items():
                if value == self.combox_1.currentText():
                    from_language_key = key

            for key, value in self.language.items():
                if value == self.combox_2.currentText():
                    to_language_key = key

            # Lấy text1
            words = textblob.TextBlob(self.text_1.toPlainText())

            # Translate
            words = words.translate(from_lang=from_language_key,to=to_language_key)

            # Output
            self.text_2.setText(f'{words}')
        except Exception as e:
            QMessageBox.about(self, 'Translator', str(e))


app = QApplication(sys.argv)
uiWindow = UI()
app.exec_()
