import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        bar = self.menuBar()

        file = bar.addMenu("文件")
        file.addAction("新建")

        save = QAction("保存", self)
        save.setShortcut("Command + S")
        file.addAction(save)

        edit = bar.addMenu("edit")
        edit.addAction("copy")
        edit.addAction("paste")
        quit = QAction("退出", self)
        edit.addAction(quit)


        save.triggered.connect(self.process)

    def process(self):
        print(self.sender().text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Menu()
    main.show()
    sys.exit(app.exec_())
