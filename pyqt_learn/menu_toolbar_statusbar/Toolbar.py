'''

工具栏按钮有三种现实状态：ToolButtonStyle
- 只显示图标
- 只显示文本
- 同时显示文本和图标

'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Toolbar(QMainWindow):
    def __init__(self):
        super(Toolbar, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("工具栏例子")
        self.resize(300, 200)

        tb1 = self.addToolBar("File")

        new = QAction(QIcon('../images/icon.ico'), "new", self)
        tb1.addAction(new)

        save = QAction(QIcon('../images/new.ico'), "save", self)
        tb1.addAction(save)

        tb2 = self.addToolBar("Act")

        stop = QAction(QIcon("../images/stop.ico"), "stop", self)
        tb2.addAction(stop)

        tb1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        tb2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        tb1.actionTriggered.connect(self.toolBtnPressed)
        tb2.actionTriggered.connect(self.toolBtnPressed)

    def toolBtnPressed(self, btn):
        print("按下的工具栏按钮是", btn.text() )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Toolbar()
    main.show()
    sys.exit(app.exec_())
