import sys
import MainWinSpacerLine
from PyQt5.Qt import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = MainWinSpacerLine.Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())