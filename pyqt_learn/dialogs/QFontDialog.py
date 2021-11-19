from PyQt5.QtWidgets import *
import sys


class QFontDialogDemo(QMainWindow):
    def __init__(self):
        super(QFontDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QFontDialog Demo")
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)

        self.fontBtn = QPushButton("select font")
        self.fontBtn.clicked.connect(self.changeFont)
        layout.addWidget(self.fontBtn)

        self.fontLabel = QLabel("Test Font 测试字体")
        layout.addWidget(self.fontLabel)

    def changeFont(self):
        font, ok = QFontDialog.getFont(self)
        if ok:
            self.fontLabel.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())