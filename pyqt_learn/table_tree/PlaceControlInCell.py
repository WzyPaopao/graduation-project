'''
在单元格中放置控件

setCellWidget

'''

import sys
from PyQt5.QtWidgets import *


class PlaceControlInCell(QWidget):
    def __init__(self):
        super(PlaceControlInCell, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('在单元格中放置控件')
        self.resize(430, 300)

        layout = QHBoxLayout()
        table_widget = QTableWidget()
        table_widget.setRowCount(4)
        table_widget.setColumnCount(3)

        layout.addWidget(table_widget)
        table_widget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])

        text_item = QTableWidgetItem('小明')
        table_widget.setItem(0, 0, text_item)

        combox = QComboBox()
        combox.addItem('男')
        combox.addItem('女')
        # QSS
        combox.setStyleSheet('QComboBox{margin:3px};')
        table_widget.setCellWidget(0, 1, combox)

        modify_btn = QPushButton('修改')
        modify_btn.setDown(True)
        modify_btn.setStyleSheet('QPushButton{margin:3px};')
        table_widget.setCellWidget(0, 2, modify_btn)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PlaceControlInCell()
    main.show()
    sys.exit(app.exec_())
