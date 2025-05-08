import sys, os
from pathlib import Path
from random import choice

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QAction, QColor
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QLabel,
    QToolBar,
    QVBoxLayout,
    QWidget,
    QGraphicsDropShadowEffect
)

from widgets_alignment import set_alignment
from effects import RippleButton


class Toolbars(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toolbar")
        self.resize(300, 200)

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setOffset(5, 5)
        shadow.setColor(QColor(0, 0, 0, 160)) 

        self.label = QLabel("Edus")
        self.label.setAlignment(set_alignment("center"))
        self.label.setStyleSheet("border: 1px solid red;")
        self.label.setMargin(5)
        self.label.setFixedSize(200, 30)
        self.label.setWordWrap(True)
        self.label.setMaximumHeight(50)


        self.icons_list = self.load_icons()

        self.toolbar = QToolBar("Main Toolbar")

        self.toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(self.toolbar)

        button = RippleButton('Refresh Icons')
        button.setFixedSize(QSize(100, 40))
        button.setGraphicsEffect(shadow)
        button.adjustSize()
        button.clicked.connect(self.refresh_icons)   



        self.vbox = QVBoxLayout()

        self.vbox.addWidget(self.label, stretch=1, alignment=set_alignment('center'))
        self.vbox.addWidget(button, alignment=set_alignment('center'))

        self.vbox.setAlignment(set_alignment('center'))
        self.vbox.setSpacing(4)

        container = QWidget()
        container.setLayout(self.vbox)

        self.setCentralWidget(container)


        


    def create_something(self, icon_path, icon_text, status_tip):
        button_action = QAction(QIcon(icon_path), icon_text, self)
        button_action.setStatusTip(status_tip)
        button_action.triggered.connect(self.on_my_toolbar_button_click)
        button_action.setCheckable(True)
        self.toolbar.addAction(button_action)
        self.toolbar.addSeparator()

    def on_my_toolbar_button_click(self):
        # label = QLabel("Mango")
        self.label.setText(f'{Path(self.icon1).name}\n{Path(self.icon2).name}')

    
    def refresh_icons(self):
        self.toolbar.clear()
        self.icon1 = choice(self.load_icons())
        self.icon2 = choice(self.load_icons())
        self.create_something(self.icon1, Path(self.icon1).name, "&Your button")
        self.create_something(self.icon2, Path(self.icon2).name, "&Your Another")
        self.on_my_toolbar_button_click()

    @classmethod
    def load_icons(cls):
        icons_list = []
        for path, _, icons in os.walk("resources/icons"):
            for icon in icons:
                icons_list.append(os.path.join(path, icon))
        return icons_list


app = QApplication(sys.argv)
tb = Toolbars()
tb.show()
sys.exit(app.exec())