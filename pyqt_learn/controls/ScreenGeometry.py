import sys
from PyQt5.Qt import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget


def onClick_Button1():
    print("widget.x() = %d" % widget.x())  # 250 窗口横坐标
    print("widget.x() = %d" % widget.y())  # 200 窗口纵坐标
    print("widget.width() = %d" % widget.width())  # 300 工作区宽度
    print("widget.height() = %d" % widget.height())  # 240 工作区高度
    print("--------------------------------------")


def onClick_Button2():
    print("widget.geometry().x() = %d" % widget.geometry().x())  # 250 工作区横坐标
    print("widget.geometry().y() = %d" % widget.geometry().y())  # 228 工作区纵坐标
    print("widget.geometry().width() = %d" % widget.geometry().width())  # 300 工作区宽度
    print("widget.geometry().height() = %d" % widget.geometry().height())  # 240 工作区高度
    print("--------------------------------------")


def onClick_Button3():
    print("widget.frameGeometry().x() = %d" % widget.frameGeometry().x())  # 250 窗口横坐标
    print("widget.frameGeometry().y() = %d" % widget.frameGeometry().y())  # 200 窗口纵坐标
    print("widget.frameGeometry().width() = %d" % widget.frameGeometry().width())  # 300 窗口的宽度
    print("widget.frameGeometry().height() = %d" % widget.frameGeometry().height())  # 268 窗口高度
    print("--------------------------------------")


if __name__ == '__main__':

    app = QApplication(sys.argv)

    widget = QWidget()
    btn = QPushButton(widget)
    btn.clicked.connect(onClick_Button1)
    btn.setText("button_1")

    btn.move(24, 52)

    btn2 = QPushButton(widget)
    btn2.clicked.connect(onClick_Button2)
    btn2.setText("button_2")
    btn2.move(24, 82)

    btn3 = QPushButton(widget)
    btn3.clicked.connect(onClick_Button3)
    btn3.setText("button_3")
    btn3.move(24, 112)

    widget.resize(300, 240)
    widget.move(250, 200)

    widget.setWindowTitle("屏幕坐标系")
    widget.show()
    sys.exit(app.exec_())



