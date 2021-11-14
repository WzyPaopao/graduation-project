from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()

        self.setWindowTitle("滑块演示")
        self.resize(300, 700)

        layout = QVBoxLayout()
        self.label = QLabel("你好，PyQt5")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(28)
        self.slider.setMaximum(88)
        self.slider.setValue(32)
        self.slider.setSingleStep(2)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(6)
        layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.valueChange)

        self.slider1 = QSlider(Qt.Vertical)
        self.slider1.setMinimum(10)
        self.slider1.setValue(20)
        self.slider1.setMaximum(100)
        self.slider1.setSingleStep(30)
        self.slider1.setTickPosition(QSlider.TicksRight)
        self.slider1.setTickInterval(10)
        self.slider1.valueChanged.connect(self.valueShow)
        layout.addWidget(self.slider1)

        self.label1 = QLabel("20")
        layout.addWidget(self.label1)

        self.setLayout(layout)

    def valueChange(self):
        print("当前值：{}".format(self.slider.value()))
        size = self.slider.value()
        self.label.setFont(QFont('Arial', size))

    def valueShow(self):
        self.label1.setText(str(self.slider1.value()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QSliderDemo()
    main.show()
    sys.exit(app.exec_())

