from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class QColorDialogDemo(QMainWindow):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QColortDialog Demo")
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)

        self.colorBtn = QPushButton("select color")
        self.colorBtn.clicked.connect(self.changeColor)
        layout.addWidget(self.colorBtn)

        self.colorBGBtn = QPushButton("select color for bg")
        self.colorBGBtn.clicked.connect(self.changeBGColor)
        layout.addWidget(self.colorBGBtn)

        self.colorLabel = QLabel("Test Color on Text")
        layout.addWidget(self.colorLabel)

    def changeColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.colorLabel.setPalette(p)

    def changeBGColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())