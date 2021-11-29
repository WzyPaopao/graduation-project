'''
设置单元格的文本对齐方式

setTextAlignment

Qt.AlignRight
Qt.AlignLeft
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class CellTextAlign(QWidget):
    def __init__(self):
        super(CellTextAlign, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('对齐方式')
        self.resize(430, 230)
        layout = QVBoxLayout()
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(4)
        self.table_widget.setColumnCount(3)
        layout.addWidget(self.table_widget)

        self.table_widget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])

        newItem = QTableWidgetItem('张三')
        newItem.setTextAlignment(Qt.AlignRight | Qt.AlignBottom)
        self.table_widget.setItem(0, 0, newItem)

        newItem = QTableWidgetItem("男")
        newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        self.table_widget.setItem(0, 1, newItem)

        newItem = QTableWidgetItem("199")
        newItem.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.table_widget.setItem(0, 2, newItem)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellTextAlign()
    main.show()
    sys.exit(app.exec_())