from PyQt5.QtWidgets import *
import sys


class QComboBoxDemo(QDialog):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()

        self.setWindowTitle("下拉列表控件演示")
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.label = QLabel("请选择编程语言")

        self.cb = QComboBox()
        self.cb.addItems(['C++', "Python", "C#", "Java"])

        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)

    def selectionChange(self, i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()

        for count in range(self.cb.count()):
            print("item" + str(count) + '=' + self.cb.itemText(count))
        print('current index', i, 'selection changed', self.cb.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())
