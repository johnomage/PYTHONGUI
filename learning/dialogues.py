import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton

class Dialog(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialoue Stuff")

        button = QPushButton('Press')
        button.clicked.connect(self.clicked)
        self.setCentralWidget(button)

    
    def clicked(self):
        dlg = QDialog(self)
        dlg.setWindowTitle('Hello o?')
        dlg.setAutoFillBackground(True)
        dlg.exec()

app = QApplication(sys.argv)
d = Dialog()
d.show()
sys.exit(app.exec())