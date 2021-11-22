'''
使用剪贴板
'''

from PyQt5 import QtGui, QtCore, QtWidgets
import sys


class ClipBoard(QtWidgets.QDialog):
    def __init__(self):
        super(ClipBoard, self).__init__()
        textCopyButton = QtWidgets.QPushButton("复制文本")
        textPasteButton = QtWidgets.QPushButton("粘贴文本")

        htmlCopyButton = QtWidgets.QPushButton("复制Html")
        htmlPasteButton = QtWidgets.QPushButton("粘贴Html")

        imageCopyButton = QtWidgets.QPushButton("复制图像")
        imagePasteButton = QtWidgets.QPushButton("粘贴图像")

        self.textLabel = QtWidgets.QLabel("默认文本")
        self.imageLabel = QtWidgets.QLabel()
        # self.imageLabel.setPixmap(QtGui.QPixmap('../controls/icon.ico'))

        layout = QtWidgets.QGridLayout()
        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(textPasteButton, 0, 1)
        layout.addWidget(htmlCopyButton, 1, 0)
        layout.addWidget(htmlPasteButton, 1, 1)
        layout.addWidget(imageCopyButton, 2, 0)
        layout.addWidget(imagePasteButton, 2, 1)
        layout.addWidget(self.textLabel, 3, 0)
        layout.addWidget(self.imageLabel, 3, 1)

        self.setLayout(layout)

        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

        self.setWindowTitle('剪贴板演示')

    def copyText(self):
         clipboard = QtWidgets.QApplication.clipboard()
         clipboard.setText('hello world')

    def pasteText(self):
        clipboard = QtWidgets.QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyImage(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setPixmap(QtGui.QPixmap('../images/icon.ico'))

    def pasteImage(self):
        clipboard = QtWidgets.QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())

    def copyHtml(self):
        mimeData = QtCore.QMimeData()
        mimeData.setHtml('<b>Bold and <font color=red>Red</font></b>')
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QtWidgets.QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = ClipBoard()
    main.show()
    sys.exit(app.exec_())
