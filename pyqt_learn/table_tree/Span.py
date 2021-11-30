'''
合并单元格

setSpan(row, col, 要合并的行数, 要合并的列数)
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Span(QWidget):
    def __init__(self):
        super(Span, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('合并单元格测试')
        self.resize(430, 230)
        layout = QHBoxLayout()
        table_widget = QTableWidget()
        table_widget.setRowCount(4)
        table_widget.setColumnCount(3)
        table_widget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])

        new_item = QTableWidgetItem('雷神')
        table_widget.setItem(0, 0, new_item)
        table_widget.setSpan(0, 0, 3, 1)

        new_item = QTableWidgetItem('男')
        table_widget.setItem(1, 1, new_item)
        table_widget.setSpan(1, 1, 2, 2)

        new_item = QTableWidgetItem('190')
        table_widget.setItem(0, 2, new_item)

        layout.addWidget(table_widget)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Span()
    main.show()
    sys.exit(app.exec_())