'''
按钮控件

父类：QAbstractButton

QPushButton
AToolButton
QRadioButton
QCheckBox
'''


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QPushButton demo")

        layout = QVBoxLayout()

        self.btn1 = QPushButton()
        self.btn1.setText("First Button1")
        # 将按钮变为开关
        self.btn1.setCheckable(True)
        self.btn1.toggle()

        self.btn2 = QPushButton("图像按钮")
        self.btn2.setIcon(QIcon(QPixmap("./icon.ico")))

        self.btn3 = QPushButton("不可用的按钮")
        self.btn3.setEnabled(False)

        self.btn4 = QPushButton("&MyButton")
        self.btn4.setDefault(True)

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        self.setLayout(layout)
        self.slot_init()

    def slot_init(self):
        self.btn1.clicked.connect(lambda: self.whichButton(self.btn1))
        self.btn1.clicked.connect(self.buttonState)

        self.btn2.clicked.connect(lambda: self.whichButton(self.btn2))

        self.btn4.clicked.connect(lambda: self.whichButton(self.btn4))

    def whichButton(self, btn):
        print("被单击的按钮是<" + btn.text() + ">")

    def buttonState(self):
        if self.btn1.isChecked():
            print("按钮1已经被选中")
        else:
            print("按钮1未被选中")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())
