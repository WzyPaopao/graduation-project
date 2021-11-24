'''
显示而为表数据（QTableView控件）

数据源

Model

需要创建 QTableView 实例和一个数据源（Model），然后将两者关联
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class TableView(QWidget):
    def __init__(self):
        super(TableView, self).__init__()
        self.setWindowTitle('QTableView表哥视图控件演示')
        self.resize(500, 300)

        self.model = QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(['ID', 'Name', 'Age'])

        self.tableview = QTableView()
        self.tableview.setModel(self.model)  # 关联 QTableView 控件和 Model
        # 添加数据
        item11 = QStandardItem("10")
        item12 = QStandardItem("alan")
        item13 = QStandardItem("21")
        self.model.setItem(0, 0, item11)
        self.model.setItem(0, 1, item12)
        self.model.setItem(0, 2, item13)

        item21 = QStandardItem("20")
        item22 = QStandardItem("auggie")
        item23 = QStandardItem("25")
        self.model.setItem(1, 0, item21)
        self.model.setItem(1, 1, item22)
        self.model.setItem(1, 2, item23)


        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableView()
    main.show()
    sys.exit(app.exec_())



