import PyQt5.QtGui as qtg
import PyQt5.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("From")
        # self.setLayout(qtw.QVBoxLayout())
        # Set layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # Add stuff/widgets
        label_1 = qtw.QLabel("This is a cool label")
        label_1.setFont(qtg.QFont("", 20))

        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)

        # Add Rows to app
        form_layout.addRow(label_1)
        form_layout.addRow("Frist Name", f_name)
        form_layout.addRow("Last Name", l_name)
        form_layout.addRow(qtw.QPushButton("Press me!", clicked=lambda: pressit()))

        self.show()

        def pressit():
            # Add to the label
            label_1.setText(f'You Clicked The Button! {f_name.text()}')


app = qtw.QApplication([])
mainwindown = MainWindow()
app.exec_()
