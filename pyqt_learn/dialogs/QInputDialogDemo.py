import sys
from PyQt5.QtWidgets import *


class QInputDialogDemo(QMainWindow):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("输入窗口")
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QFormLayout()

        self.btn1 = QPushButton("获取列表")
        self.lineEdit1 = QLineEdit()
        layout.addRow(self.btn1, self.lineEdit1)

        self.btn2 = QPushButton("获取名字")
        self.lineEdit2 = QLineEdit()
        layout.addRow(self.btn2, self.lineEdit2)

        self.btn3 = QPushButton("获取年龄")
        self.lineEdit3 = QLineEdit()
        layout.addRow(self.btn3, self.lineEdit3)

        widget.setLayout(layout)
        self.slot_init()

    def slot_init(self):
        self.btn1.clicked.connect(self.getItem)
        self.btn2.clicked.connect(self.getString)
        self.btn3.clicked.connect(self.getInt)

    def getItem(self):
        items = ['C', 'C++', 'Java']
        item, ok = QInputDialog.getItem(self, 'choose language', 'language list', items)
        if ok and item:
            self.lineEdit1.setText(item)

    def getString(self):
        text, ok = QInputDialog.getText(self, 'input box', 'input name')
        if ok and text:
            self.lineEdit2.setText(text)

    def getInt(self):
        num, ok = QInputDialog.getInt(self, 'input number', 'input number')
        if num and ok:
            self.lineEdit3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())
