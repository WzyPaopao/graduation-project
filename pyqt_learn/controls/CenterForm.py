import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self, parent=None):
        super(CenterForm, self).__init__(parent)

        # title
        self.setWindowTitle("第一个主窗口应用")
        # size
        self.resize(400, 300)
        self.status = self.statusBar()
        # self.status.showMessage("只存在5秒的消息", 5000)
        self.center()

    def center(self):
        # 获取屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标
        size = self.geometry()
        newLeft = int((screen.width() - size.width()) / 2)
        newTop = int((screen.height() - size.height()) / 2)
        self.move(newLeft, newTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CenterForm ()
    main.show()
    sys.exit(app.exec_())

