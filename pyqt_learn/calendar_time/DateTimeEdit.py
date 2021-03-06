import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class DateTimeEdit(QWidget):
    def __init__(self):
        super(DateTimeEdit, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 90)
        self.setWindowTitle("设置不同风格的日期和时间")

        layout = QVBoxLayout()
        dateTimeEdit1 = QDateTimeEdit()
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))

        self.dateTimeEdit = dateTimeEdit1

        dateTimeEdit2.setCalendarPopup(True)

        dateEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())

        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")
        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:ss")

        dateTimeEdit1.dateChanged.connect(self.onDateChange)
        dateTimeEdit1.timeChanged.connect(self.onTimeChange)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChange)

        self.btn = QPushButton("get current selected time")
        self.btn.clicked.connect(self.onBtnClick)

        layout.addWidget(dateTimeEdit1)
        layout.addWidget(dateTimeEdit2)
        layout.addWidget(dateEdit)
        layout.addWidget(timeEdit)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def onDateChange(self, date):
        print(date)

    def onTimeChange(self, time):
        print(time)

    def onDateTimeChange(self, date_time):
        print(date_time)

    def onBtnClick(self):
        dateTime = self.dateTimeEdit.dateTime()
        print(dateTime)

        # 最大日期
        print('最大日期：', self.dateTimeEdit.maximumDate())
        # 最大日期和时间
        print('最大日期和时间：', self.dateTimeEdit.maximumDateTime())
        # 最小日期
        print('最小日期：', self.dateTimeEdit.minimumDate())
        # 最小日期和时间
        print('最小日期和时间：', self.dateTimeEdit.minimumDateTime())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DateTimeEdit()
    main.show()
    sys.exit(app.exec_())

