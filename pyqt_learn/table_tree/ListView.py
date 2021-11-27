import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel


class ListViewDemo(QWidget):
    def __init__(self):
        super(ListViewDemo, self).__init__()
        self.setWindowTitle('QListView 例子')
        self.resize(300, 270)
        layout = QVBoxLayout()

        list_view = QListView()
        list_model = QStringListModel()
        self.list = ['列表项1', '列表项2', '列表项3']

        list_model.setStringList(self.list)
        list_view.setModel(list_model)
        list_view.clicked.connect(self.clicked)
        layout.addWidget(list_view)
        self.setLayout(layout)

    def clicked(self, item):
        QMessageBox.information(self, 'QListView', '您选择了：' + self.list[item.row()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ListViewDemo()
    main.show()
    sys.exit(app.exec_())
