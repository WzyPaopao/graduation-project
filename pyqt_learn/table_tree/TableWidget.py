from PyQt5.QtWidgets import *
import sys


class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableWidget Demo')
        self.resize(430, 230)
        layout = QHBoxLayout()
        table_widget = QTableWidget()
        table_widget.setRowCount(4)
        table_widget.setColumnCount(3)
        layout.addWidget(table_widget)

        table_widget.setHorizontalHeaderLabels(['Name', 'Age', 'Address'])
        table_widget.setVerticalHeaderLabels(['a', 'b'])

        nameItem = QTableWidgetItem('alan')
        table_widget.setItem(0, 0, nameItem)
        ageItem = QTableWidgetItem('19')
        table_widget.setItem(0, 1, ageItem)
        addressItem = QTableWidgetItem('London')
        table_widget.setItem(0, 2, addressItem)

        table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止编辑
        table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 整行选择
        table_widget.resizeColumnsToContents()  # 调整列自适应
        table_widget.resizeRowsToContents()  # 调整行自适应

        # table_widget.horizontalHeader().setVisible(False)  # 隐藏水平头
        # table_widget.verticalHeader().setVisible(False)  # 隐藏垂直头

        table_widget.setShowGrid(False)  # 隐藏表格线

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TableWidgetDemo()
    main.show()
    sys.exit(app.exec_())