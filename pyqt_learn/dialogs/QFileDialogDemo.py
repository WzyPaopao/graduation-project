from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class QFileDialogDemo(QMainWindow):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QFileDialog Demo')
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout()

        self.button1 = QPushButton("加载图片")
        self.button1.clicked.connect(self.loadImage)
        layout.addWidget(self.button1)

        self.imageLabel = QLabel()
        layout.addWidget(self.imageLabel)

        self.button2 = QPushButton("加载文本文件")
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        widget.setLayout(layout)

    def loadImage(self):
        file_name, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件(*.jpg *.png *.ico)')
        self.imageLabel.setPixmap(QPixmap(file_name))

    def loadText(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec():
            file_name = dialog.selectedFiles()
            with open(file_name[0], 'r') as f:
                data = f.read()
                self.contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())
