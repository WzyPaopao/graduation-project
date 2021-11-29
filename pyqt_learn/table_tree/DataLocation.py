'''
在表格中快速定位到特定的行

1 数据定位: findItems() -> list
2 如果找到了满足条件的单元格，会定位到单元格所在的行: setSliderPosition(row)
'''
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DataLocation(QWidget):
    def __init__(self):
        super(DataLocation, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget 例子")
        self.resize(600, 800)

        layout = QHBoxLayout()
        table_widget = QTableWidget()
        table_widget.setRowCount(40)
        table_widget.setColumnCount(4)

        layout.addWidget(table_widget)

        for i in range(40):
            for j in range(4):
                item_content = '(%d, %d)' % (i, j)
                table_widget.setItem(i, j, QTableWidgetItem(item_content))

        self.setLayout(layout)

        text = '(12,'
        items = table_widget.findItems(text, Qt.MatchStartsWith)
        for i in range(len(items)):
            item = items[i]
            item.setBackground(QBrush(QColor(0, 255, 0)))
            item.setForeground(QBrush(QColor(255, 0, 0)))

            row = item.row()

            # 定位到指定的行
            table_widget.verticalScrollBar().setSliderPosition(row)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DataLocation()
    main.show()
    sys.exit(app.exec_())