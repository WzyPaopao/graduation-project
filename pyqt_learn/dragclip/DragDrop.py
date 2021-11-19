'''
让控件支持拖拽动作

A. setDragEnable()

B. setAcceptDrops(True)

B需要两个事件
1 dragEnterEvent    将A拖到B触发
2 dropEvent         在B的区域放下A触发
'''

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys


class MyComboBox(QComboBox):
    def __init__(self):
        super(QComboBox, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, a0: QtGui.QDropEvent) -> None:
        self.addItem(a0.mimeData().text())


class DragDropDemo(QWidget):
    def __init__(self):
        super(DragDropDemo, self).__init__()
        formLayout = QFormLayout()
        formLayout.addRow(QLabel('请将左边的文本拖拽到右边的下拉列表'))
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)  # 让控件可以拖动

        combo = MyComboBox()
        formLayout.addRow(lineEdit, combo)
        self.setLayout(formLayout)
        self.setWindowTitle('拖动测试')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DragDropDemo()
    main.show()
    sys.exit(app.exec_())
