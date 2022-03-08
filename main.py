import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # add a title
        self.setWindowTitle("Hello PyQt5")

        # set layout
        self.setLayout(qtw.QVBoxLayout())
        # qtw.QVBoxLayout() bố trí layout dọc
        # qtw.QHBoxLayout() bố trí layout ngang

        # create a label
        my_label = qtw.QLabel("Pick something From The List Below")
        # change the font size of label
        my_label.setFont(qtg.QFont('helvetica', 24))
        # đưa label lên màn hình
        self.layout().addWidget(my_label)

        # Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        # Create a combo box
        my_combo=qtw.QComboBox(self,editable=True,insertPolicy=qtw.QComboBox.InsertAtTop)
        # tham so 2 cho phép chỉnh sửa combo box tham số thứ 3 thứ tự insert
        # Add Items To The Combo box
        ITEMS={"Coke":"Nước ngọt","Pizza":"Cake","Chicken":1,"Rice":"Gạo","Apple":""}
        for item,data in ITEMS.items():
            my_combo.addItem(item,data)
        my_combo.addItems(['one','two','three'])
        my_combo.insertItem(5,'four')
        self.layout().addWidget(my_combo)
        # Create a button
        my_button = qtw.QPushButton("press me!", clicked=lambda: press_it())

        self.layout().addWidget(my_button)
        # Show the app
        self.show()

        def press_it():
            # Add name the label
            my_label.setText(f'You picked {my_combo.currentData()}!!!')
            # Clean entry the box
            # my_entry.setText("")


app = qtw.QApplication([])
mainwindow = MainWindow()

# run the app
app.exec_()
