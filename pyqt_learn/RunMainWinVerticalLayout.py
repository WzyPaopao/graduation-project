import sys
import MainWinVerticalLayout
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = MainWinVerticalLayout.Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
