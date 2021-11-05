import sys
from PyQt5.Qt import QApplication, QMainWindow
from test_1 import Ui_MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
