import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QInputDialog,
    QMainWindow,
    QPushButton,
    QLabel,
    QWidget,
    QVBoxLayout,
)

class WinApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Input App')

        int_btn = QPushButton('Integer')
        int_btn.clicked.connect(self.get_int_value)

        # self.setCentralWidget(int_btn)
        self.display_lbl = QLabel('waiting...')
        self.display_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.display_lbl)
        self.vbox.addWidget(int_btn)
        self.vbox.setSpacing(2)
        self.vbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        widget = QWidget()
        widget.setLayout(self.vbox)
        self.setCentralWidget(widget)

    def get_int_value(self):
        val, flag = QInputDialog.getInt(self, "Input Required", "Enter a number:")
        self.display_lbl.setText(f'Triggered value: {val}\nflag: {flag}')


app = QApplication(sys.argv)

win = WinApp()
win.show()

app.exec()

