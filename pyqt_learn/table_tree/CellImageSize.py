'''
改变单元格中图片的尺寸

setIconSize(QSize(width, height))
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class CellImageSize(QWidget):
    def __init__(self):
        super(CellImageSize, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在单元格中实现图文混排')
        self.resize(1000, 900)
        layout = QHBoxLayout()

        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(3)
        self.table_widget.setIconSize(QSize(300, 200))
        layout.addWidget(self.table_widget)

        self.table_widget.setHorizontalHeaderLabels(['图片1', '图片2', '图片3'])

        for i in range(3):
            self.table_widget.setColumnWidth(i, 300)

        for i in range(15):
            self.table_widget.setRowHeight(i, 200)

        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellImageSize()
    main.show()
    sys.exit(app.exec_())