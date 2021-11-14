'''
复选框控件（QCheckBox）

三种状态
- 未选中：0
- 半选中：1
- 选中：2
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class QCheckBoxDemo(QDialog):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QCheckBox Demo")
        layout = QHBoxLayout()

        self.checkBox1 = QCheckBox("复选框1")
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(self.checkboxState)

        self.checkBox2 = QCheckBox("复选框2")
        self.checkBox2.stateChanged.connect(self.checkboxState)

        self.checkBox3 = QCheckBox("复选框3")
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        self.checkBox3.stateChanged.connect(self.checkboxState)

        layout.addWidget(self.checkBox1)
        layout.addWidget(self.checkBox2)
        layout.addWidget(self.checkBox3)

        self.setLayout(layout)

    def checkboxState(self):
        state1 = self.checkBox1.text() + ", isChecked=" + str(self.checkBox1.isChecked()) \
                + ", checkState=" + str(self.checkBox1.checkState())
        state2 = self.checkBox2.text() + ", isChecked=" + str(self.checkBox2.isChecked()) \
                + ", checkState=" + str(self.checkBox2.checkState())
        state3 = self.checkBox3.text() + ", isChecked=" + str(self.checkBox3.isChecked()) \
                + ", checkState=" + str(self.checkBox3.checkState())
        print("{}, {}, {}".format(state1, state2, state3))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())
