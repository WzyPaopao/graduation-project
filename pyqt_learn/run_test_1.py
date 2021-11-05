import sys
from PyQt5.QtWidgets import QApplication, QWidget
from test_1 import Ui_MainWindow


if __name__ == '__main__':
    # print("hello")
    # # 创建QApplication实例
    # app = QApplication(sys.argv)
    # # 创建一个窗口
    # w = QWidget()
    # # 设定窗口尺寸
    # w.resize(300, 150)
    # # 移动窗口
    # w.move(300, 300)
    # # 设置窗口属性
    # w.setWindowTitle("hello world")
    # # 显示窗口
    # w.show()
    #
    # # 进入程序的主循环，并通过exit确保主循环安全结束
    # sys.exit(app.exec_())
    ui = Ui_MainWindow()
    ui.setupUi()
