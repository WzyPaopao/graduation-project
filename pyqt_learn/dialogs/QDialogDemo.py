'''
QDialog 对话框：

QMessageBox
QColorDialog
QFileDialog
QFontDialog
QInputDialog

窗口分为：
1 QMainWindow（有菜单栏的主对话框）
2 QWidget（可取代1和2）
3 QDialog（没有菜单栏和工具栏的提示框）
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QDialog Demo")
        self.resize(300, 100)

        self.button = QPushButton(self)
        self.button.setText("弹出对话框")
        self.button.move(50, 50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog = QDialog()
        button = QPushButton("确定", dialog)
        button.clicked.connect(dialog.close)
        button.move(50, 50)
        button.setWindowTitle("对话框")
        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())
