import sys, math
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DrawAll(QWidget):
    def __init__(self):
        super(DrawAll, self).__init__()
        self.resize(300, 600)
        self.setWindowTitle('绘制各种图形')

    def paintEvent(self, event) -> None:
        qp = QPainter()
        qp.begin(self)

        qp.setPen(Qt.blue)

        # 绘制弧
        rect = QRect(0, 10, 100, 100)
        qp.drawArc(rect, 0, 50 * 16)

        qp.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawAll()
    main.show()
    sys.exit(app.exec_())
