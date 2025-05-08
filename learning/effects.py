

from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import QTimer, QPoint, Qt
from PyQt6.QtGui import QPainter, QColor
from random import randint


class RippleButton(QPushButton):
    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.ripple_radius = 0
        self.ripple_opacity = 150
        self.ripple_center = QPoint(0, 0)
        self.anim_timer = QTimer()
        self.anim_timer.timeout.connect(self.animate_ripple)
        # self.setStyleSheet("border: 1px solid #ccc; padding: 10px;")
        self.setMouseTracking(True)
        self.setStyleSheet("""
                            QPushButton {
                                         border: 1px solid #2980b9;
                                         border-radius: 10px;
                                         padding: 2px;
                                        }"""
                           )

    def mousePressEvent(self, event):
        self.ripple_center = event.position().toPoint()
        self.ripple_radius = 0
        self.ripple_opacity = 150
        self.anim_timer.start(5)
        super().mousePressEvent(event)

    def animate_ripple(self):
        self.ripple_radius += 5
        self.ripple_opacity -= 5
        if self.ripple_opacity <= 0:
            self.anim_timer.stop()
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.ripple_opacity > 0:
            painter = QPainter(self)
            color = QColor(randint(0, 255),
                           randint(0, 255),
                           randint(0, 255),
                           self.ripple_opacity)
            
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setBrush(color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawEllipse(self.ripple_center, self.ripple_radius, self.ripple_radius)