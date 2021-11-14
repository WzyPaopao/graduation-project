# 显示控件提示信息

import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QToolTip, QPushButton, QWidget
from PyQt5.QtGui import QFont


class TooltipForm(QMainWindow):
    def __init__(self):
        super(TooltipForm, self).__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSun', 12))
        self.setToolTip("今天是<b>星期五</b>")
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle("设置控件提示消息")

        self.btn = QPushButton("提示")
        self.btn.setToolTip("这是一个按钮")
        layout = QHBoxLayout()
        layout.addWidget(self.btn)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())
