"""
QLabel 与 伙伴控件

mainLayout.addWidget(控件名, 行索引, 列索引, 行占用, 列占用)
"""

from PyQt5.QtWidgets import *
import sys


if __name__ == '__main__':
    class QLabelBuddy(QDialog):
        def __init__(self):
            super(QLabelBuddy, self).__init__()
            self.initUI()

        def initUI(self):
            self.setWindowTitle("QLabel与伙伴控件")
            nameLabel = QLabel("&Name", self)
            nameLineEdit = QLineEdit(self)
            nameLabel.setBuddy(nameLineEdit)

            passwordLabel = QLabel("&Password", self)
            passwordLineEdit = QLineEdit(self)
            passwordLabel.setBuddy(passwordLineEdit)

            btnOK = QPushButton("&OK")
            btnCancel = QPushButton("&Cancel")

            mainLayout = QGridLayout(self)
            mainLayout.addWidget(nameLabel, 0, 0)
            mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)
            mainLayout.addWidget(passwordLabel, 1, 0)
            mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)
            mainLayout.addWidget(btnOK, 2, 1)
            mainLayout.addWidget(btnCancel, 2, 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())


