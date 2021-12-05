'''
停靠控件 QDockWidget
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DockWidget(QMainWindow):
    def __init__(self):
        super(DockWidget, self).__init__()
        self.setWindowTitle("QDockWidget Demo")

        layout = QHBoxLayout()
        self.items = QDockWidget("Dockable", self)
        self.list_widget = QListWidget()
        self.list_widget.addItem("item1")
        self.list_widget.addItem("item2")
        self.list_widget.addItem("item3")

        self.items.setWidget(self.list_widget)
        self.setCentralWidget(QLineEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DockWidget()
    main.show()
    sys.exit(app.exec_())