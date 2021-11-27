from PyQt5.QtWidgets import *
import sys


class ListWidgetDemo(QMainWindow):
    def __init__(self):
        super(ListWidgetDemo, self).__init__()
        self.setWindowTitle('QListWidget Demo')
        self.resize(300, 270)
        self.list_widget = QListWidget()
        self.list_widget.resize(300, 120)
        self.list_widget.addItem('item1')
        self.list_widget.addItem('item2')
        self.list_widget.addItem('item3')
        self.list_widget.addItem('item4')
        self.list_widget.addItem('item5')

        self.list_widget.itemClicked.connect(self.clicked)

        self.setCentralWidget(self.list_widget)

    def clicked(self, index):
        QMessageBox.information(self, "QListWidget",
                                "You choose: " + self.list_widget.item(self.list_widget.row(index)).text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListWidgetDemo()
    main.show()
    sys.exit(app.exec_())
