'''
树控件的基本用法

QTreeWidget
'''

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class BasicTreeWidget(QMainWindow):
    def __init__(self):
        super(BasicTreeWidget, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('树控件的基本用法')
        self.resize(500, 600)
        self.tree = QTreeWidget()

        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Key', 'Value'])
        root = QTreeWidgetItem(self.tree)
        root.setText(0, '根')
        root.setIcon(0, QIcon('../images/icon.ico.ico'))
        self.tree.setColumnWidth(0, 120)

        child1 = QTreeWidgetItem(root)
        child1.setText(0, '子节点1')
        child1.setText(1, '子节点1的数据')
        child1.setIcon(0, QIcon('../images/stop.ico'))
        child1.setCheckState(0, Qt.Checked)

        child2 = QTreeWidgetItem(root)
        child2.setText(0, '子节点2')
        child2.setIcon(0, QIcon('../images/new.ico'))

        child3 = QTreeWidgetItem(child2)
        child3.setText(0, '子节点2-1')
        child3.setText(1, '新的值')
        child3.setIcon(0, QIcon('../images/new.ico'))

        self.tree.expandAll()

        self.setCentralWidget(self.tree)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = BasicTreeWidget()
    main.show()
    sys.exit(app.exec_())