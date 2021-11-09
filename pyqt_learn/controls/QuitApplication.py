import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.Qt import QHBoxLayout, QWidget, QPushButton


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.resize(300, 200)
        self.setWindowTitle("退出应用程序")

        # add Button
        self.button1 = QPushButton("退出")
        self.button1.clicked.connect(self.onClick_Button1)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    # click action
    def onClick_Button1(self):
        sender = self.sender()
        print('\"' + sender.text() + '\"按钮被按下')
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
