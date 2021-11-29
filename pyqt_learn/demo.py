from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class demo(QWidget):
    def __init__(self):
        super(demo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = demo()
    main.show()
    sys.exit(app.exec_())