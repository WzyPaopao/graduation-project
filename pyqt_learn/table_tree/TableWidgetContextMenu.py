'''
在表格中显示上下文菜单
1 如何弹出菜单
2 如果在满足条件的情况下弹出菜单

QMenu.exec_()
'''
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class TableWidgetContextMenu(QWidget):
    def __init__(self):
        super(TableWidgetContextMenu, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在表格中显示上下文菜单')
        self.resize(500, 300)
        layout = QHBoxLayout()
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(3)
        layout.addWidget(self.table_widget)

        self.table_widget.setHorizontalHeaderLabels(['姓名', '性别', '体重'])

        new_item = QTableWidgetItem('张三')
        self.table_widget.setItem(0, 0, new_item)

        new_item = QTableWidgetItem('男')
        self.table_widget.setItem(0, 1, new_item)

        new_item = QTableWidgetItem('160')
        self.table_widget.setItem(0, 2, new_item)

        new_item = QTableWidgetItem('李四')
        self.table_widget.setItem(1, 0, new_item)

        new_item = QTableWidgetItem('女')
        self.table_widget.setItem(1, 1, new_item)

        new_item = QTableWidgetItem('130')
        self.table_widget.setItem(1, 2, new_item)

        self.table_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_widget.customContextMenuRequested.connect(self.generateMenu)

        self.setLayout(layout)

    def generateMenu(self, pos):
        global row_num
        print(pos)

        for i in self.table_widget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num < 2:
            menu = QMenu()
            item1 = menu.addAction('菜单项1')
            item2 = menu.addAction('菜单项2')
            item3 = menu.addAction('菜单项3')

            # 从窗口坐标系转换到全局坐标系
            screen_pos = self.table_widget.mapToGlobal(pos)

            # 被阻塞
            action = menu.exec(screen_pos)
            if action == item1:
                print('选择了第一个菜单项', self.table_widget.item(row_num, 0).text(),
                                            self.table_widget.item(row_num, 1).text(),
                                            self.table_widget.item(row_num, 2).text())
            elif action == item2:
                print('选择了第二个菜单项', self.table_widget.item(row_num, 0).text(),
                                            self.table_widget.item(row_num, 1).text(),
                                            self.table_widget.item(row_num, 2).text())
            elif action == item3:
                print('选择了第三个菜单项', self.table_widget.item(row_num, 0).text(),
                                            self.table_widget.item(row_num, 1).text(),
                                            self.table_widget.item(row_num, 2).text())
            else:
                return



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableWidgetContextMenu()
    main.show()
    sys.exit(app.exec_())