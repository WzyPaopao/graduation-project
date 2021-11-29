'''
按列排序

1 按哪一列排序
2 排序类型：升序或降序

sortItems(columnIndex, orderType)
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class ColumnSort(QWidget):
    def __init__(self):
        super(ColumnSort, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('按列排序')
        self.resize(430, 230)
        layout = QVBoxLayout()
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(4)
        self.table_widget.setColumnCount(3)
        layout.addWidget(self.table_widget)

        self.table_widget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])

        # 第一行
        newItem = QTableWidgetItem('张三')
        self.table_widget.setItem(0, 0, newItem)
        newItem = QTableWidgetItem("男")
        self.table_widget.setItem(0, 1, newItem)
        newItem = QTableWidgetItem("165")
        self.table_widget.setItem(0, 2, newItem)

        # 第二行
        newItem = QTableWidgetItem('李四 ')
        self.table_widget.setItem(1, 0, newItem)
        newItem = QTableWidgetItem("女")
        self.table_widget.setItem(1, 1, newItem)
        newItem = QTableWidgetItem("160")
        self.table_widget.setItem(1, 2, newItem)

        # 第三行
        newItem = QTableWidgetItem('王五')
        self.table_widget.setItem(2, 0, newItem)
        newItem = QTableWidgetItem("男")
        self.table_widget.setItem(2, 1, newItem)
        newItem = QTableWidgetItem("170")
        self.table_widget.setItem(2, 2, newItem)

        self.btn = QPushButton('排序')
        self.btn.clicked.connect(self.order)

        layout.addWidget(self.btn)
        self.orderType = Qt.DescendingOrder

        self.setLayout(layout)

    def order(self):
        if self.orderType == Qt.DescendingOrder:
            self.orderType = Qt.AscendingOrder
        else:
            self.orderType = Qt.DescendingOrder
        self.table_widget.sortItems(2, self.orderType)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ColumnSort()
    main.show()
    sys.exit(app.exec_())