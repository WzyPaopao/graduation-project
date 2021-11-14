import sys
from PyQt5 import QtWidgets, QtGui


class IconForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle("设置窗口图标")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("./icon.ico"))
    main = IconForm()
    main.show()
    sys.exit(app.exec_())