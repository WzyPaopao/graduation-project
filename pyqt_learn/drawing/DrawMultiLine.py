import sys, math
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui


class DrawMultiLine(QWidget):
    def __init__(self):
        super(DrawMultiLine, self).__init__()
        self.resize(300, 300)
        self.setWindowTitle('设置Pen的样式')

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter()
        painter.begin(self)
        pen = QPen(Qt.red, 3, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 50)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(60, 100, 200, 60)

        pen.setStyle(Qt.SolidLine)
        pen.setColor(Qt.blue)
        painter.setPen(pen)
        painter.drawLine(10, 200, 90, 60)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawMultiLine()
    main.show()
    sys.exit(app.exec_())