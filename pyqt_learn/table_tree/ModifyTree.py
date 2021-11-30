from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class ModifyTree(QMainWindow):
    def __init__(self):
        super(ModifyTree, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('TreeWidget Demo')

        operator_layout = QHBoxLayout()
        add_btn = QPushButton('add node')
        update_btn = QPushButton('update node')
        delete_btn = QPushButton('delete node')

        operator_layout.addWidget(add_btn)
        operator_layout.addWidget(update_btn)
        operator_layout.addWidget(delete_btn)

        add_btn.clicked.connect(self.add_node)
        update_btn.clicked.connect(self.update_node)
        delete_btn.clicked.connect(self.delete_node)

        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(['Key', 'Value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        root.setText(1, '0')

        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, '1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '2')

        child3 = QTreeWidgetItem(root)
        child3.setText(0, 'child3')
        child3.setText(1, '3')

        child4 = QTreeWidgetItem(child3)
        child4.setText(0, 'child4')
        child4.setText(1, '4')

        self.tree.clicked.connect(self.onTreeClicked)
        main_layout = QVBoxLayout(self)
        main_layout.addLayout(operator_layout)
        main_layout.addWidget(self.tree)

        self.setLayout(main_layout)


    def onTreeClicked(self, index):
        row = self.tree.currentItem()
        print(index.row())
        print('Key={}, Value={}'.format(row.text(0), row.text(1)))


    def add_node(self):
        pass

    def update_node(self):
        pass

    def delete_node(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ModifyTree()
    main.show()
    sys.exit(app.exec_())