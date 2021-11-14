from PyQt5.QtWidgets import *
import sys


class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTextEdit控件演示")
        self.resize(300, 280)

        self.textEdit = QTextEdit()
        self.buttonText = QPushButton("显示文本")
        self.buttonHtml = QPushButton("显示HTML")
        self.buttonToText = QPushButton("获取文本")
        self.buttonToHtml = QPushButton("获取HTML")
        self.buttonQuit = QPushButton("退出")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHtml)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonToHtml)
        layout.addWidget(self.buttonQuit)

        self.setLayout(layout)
        self.slot_init()

    def slot_init(self):
        self.buttonText.clicked.connect(self.onClick_ButtonText)
        self.buttonHtml.clicked.connect(self.onClick_ButtonHtml)
        self.buttonToText.clicked.connect(self.onClick_ButtonToText)
        self.buttonToHtml.clicked.connect(self.onClick_ButtonToHtml)
        self.buttonQuit.clicked.connect(self.close)

    def onClick_ButtonText(self):
        self.textEdit.setPlainText("Hello World")

    def onClick_ButtonToText(self):
        print(self.textEdit.toPlainText())

    def onClick_ButtonHtml(self):
        self.textEdit.setHtml("<font color=\"blue\" size=\"5\">Hello World</font>")

    def onClick_ButtonToHtml(self):
        print(self.textEdit.toHtml())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTextEditDemo()
    main.show()
    sys.exit(app.exec_())