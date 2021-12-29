'''
容纳多文档的窗口

QMdiArea

QMdiSubWindow
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MultiWindows(QMainWindow):
    def __init__(self):
        super(MultiWindows, self).__init__()
        self.setWindowTitle('容纳多文档窗口')

        self.dmi = QMdiSubWindow()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MultiWindows()
    main.show()
    sys.exit(app.exec_())

