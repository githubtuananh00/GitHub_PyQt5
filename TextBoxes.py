import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setLayout(qtw.QVBoxLayout())
        self.setWindowTitle("Text Boxes")

        # Create a label
        my_label = qtw.QLabel("Tpye Something Into The Box Below")
        my_label.setFont(qtg.QFont("", 15))
        self.layout().addWidget(my_label)

        # Create a Text boxes
        my_text = qtw.QTextEdit(self, lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                                lineWrapColumnOrWidth=50,
                                placeholderText="Hello World!!",
                                readOnly=False,
                                html='<center><h1><i>Big Header Text</i></h1></center>'
                                )
        self.layout().addWidget(my_text)

        # Create a button
        my_button = qtw.QPushButton("Press me", clicked=lambda: pressit())
        self.layout().addWidget(my_button)

        self.show()

        def pressit():
            # Add the label
            my_label.setText(f'You picked {my_text.toPlainText()}')
            my_text.setPlainText('You pressed the button')


app = qtw.QApplication([])
mainwindown = MainWindow()
app.exec_()
