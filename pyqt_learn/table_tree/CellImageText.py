from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class CellImageText(QWidget):
    def __init__(self):
        super(CellImageText, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在单元格中实现图文混排')
        self.resize(500, 300)
        layout = QHBoxLayout()

        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(4)
        layout.addWidget(self.table_widget)

        self.table_widget.setHorizontalHeaderLabels(['姓名', '性别', '体重', '显示图片'])

        new_item = QTableWidgetItem("李宁")
        self.table_widget.setItem(0, 0, new_item)

        new_item = QTableWidgetItem("男")
        self.table_widget.setItem(0, 1, new_item)

        new_item = QTableWidgetItem("160")
        self.table_widget.setItem(0, 2, new_item)

        new_item = QTableWidgetItem(QIcon('../images/icon.ico'), '背包')
        self.table_widget.setItem(0, 3, new_item)

        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellImageText()
    main.show()
    sys.exit(app.exec_())