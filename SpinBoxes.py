import PyQt5.QtWidgets as ptw
import PyQt5.QtGui as ptg


class MainWindown(ptw.QWidget):
    def __init__(self):
        super().__init__()
        # Add title
        self.setWindowTitle("Soin Boxes")

        # Set layout
        self.setLayout(ptw.QVBoxLayout())

        # Create a label
        my_label = ptw.QLabel("")
        my_label.setFont(ptg.QFont("avc", 20))
        self.layout().addWidget(my_label)

        # Create a spin boxes
        my_spin = ptw.QSpinBox(self, value=10, maximum=100, minimum=0, singleStep=2, prefix='#', suffix="$")
        # Change Font of size Spin box
        my_spin.setFont(ptg.QFont("", 20))
        self.layout().addWidget(my_spin)

        # Create a button
        my_button = ptw.QPushButton("Press me", clicked=lambda: pressit())
        self.layout().addWidget(my_button)
        # Show the app
        self.show()

        def pressit():
            # Add name to lable
            my_label.setText(f'You picked {my_spin.value()}!!')


app = ptw.QApplication([])
mainwindow = MainWindown()

app.exec_()
