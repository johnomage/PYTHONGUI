import sys

from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QTabWidget,
    QLabel,
    QPushButton,
    QWidget
)

from PyQt6.QtCore import Qt
from layout_colorwidget import Color


class Tabb(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Working Tab')

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(True)
        tabs.setDocumentMode(True)
        
        for color in ["red", "green", "blue", "yellow"]:
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)

app = QApplication(sys.argv)
tab = Tabb()
tab.show()
app.exec()