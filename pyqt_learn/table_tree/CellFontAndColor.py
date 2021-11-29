from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class CellFontAndColor(QWidget):
    def __init__(self):
        super(CellFontAndColor, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('设置单元格字体和颜色')
        self.resize(430, 230)
        layout = QHBoxLayout()
        table_widget = QTableWidget()
        table_widget.setRowCount(4)
        table_widget.setColumnCount(3)
        layout.addWidget(table_widget)

        table_widget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])
        new_item = QTableWidgetItem('雷神')
        new_item.setFont(QFont('Times', 14, QFont.Black))
        new_item.setForeground(QBrush(QColor(0, 200, 200)))
        table_widget.setItem(0, 0, new_item)

        new_item2 = QTableWidgetItem('死亡女神')
        new_item2.setForeground(QBrush(QColor(123, 20, 200)))
        new_item2.setBackground(QBrush(QColor(100, 153, 21)))
        table_widget.setItem(0, 1, new_item2)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CellFontAndColor()
    main.show()
    sys.exit(app.exec_())