import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QInputDialog,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel
)
from widgets_alignment import set_alignment


class Win(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Multi-Iput')
        layout = QVBoxLayout()

        self.label = QLabel('😒')
        self.label.setAlignment(set_alignment('center'))
        layout.addWidget(self.label)

        int_btn = QPushButton('Integer')
        int_btn.clicked.connect(self.get_int)
        layout.addWidget(int_btn)

        float_btn = QPushButton('Float')
        float_btn.clicked.connect(self.get_float)
        layout.addWidget(float_btn)

        list_btn = QPushButton('Get list')
        list_btn.clicked.connect(self.get_list)
        layout.addWidget(list_btn)

        str_btn = QPushButton('String')
        str_btn.clicked.connect(self.get_text)
        layout.addWidget(str_btn)
        layout.setAlignment(set_alignment('center'))

        pwd_btn = QPushButton('password')
        pwd_btn.clicked.connect(self.set_password)
        layout.addWidget(pwd_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def get_int(self):
        val, _ = QInputDialog.getInt(self, 'Int value', 'get int val')
    
    def get_float(self):
        val, _ = QInputDialog.getDouble(self, 'double', 'float val: ')

    def get_list(self):
        fruits_list = ["apple", "pear", "orange", "grape"]
        val, _ = QInputDialog.getItem(self, 'fruits', 'select fruit', fruits_list)
        self.label.setText(f'selected: {val}')


    def get_text(self):
        val, _ = QInputDialog.getText(self, 'text', 'enter text')
        self.label.setText(f'trigger: {val}')

    def set_password(self):
        mode = QLineEdit.EchoMode.Password
        password, _ = QInputDialog.getText(self, 'Password', 'Enter password: ', mode)
        self.label.setText(password)


app = QApplication(sys.argv)

win = Win()
win.show()
app.exec()
