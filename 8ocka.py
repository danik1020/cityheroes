import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QTimer, QPointF, Qt
import math

def infinity_trajectory(t):
    x = math.sin(t)
    y = math.cos(t) * math.sin(t)
    return x, y

class Ball(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Infinite Trajectory')

        self.t = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(50)

    def animate(self):
        self.t += 0.05
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.drawBall(painter)
        painter.end()

    def drawBall(self, painter):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(255, 0, 0))
        x, y = infinity_trajectory(self.t)
        x_pixel = self.width() / 2 + x * self.width() / 4
        y_pixel = self.height() / 2 - y * self.height() / 4
        painter.drawEllipse(QPointF(x_pixel, y_pixel), 5, 5)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ball = Ball()
    ball.show()
    sys.exit(app.exec())
