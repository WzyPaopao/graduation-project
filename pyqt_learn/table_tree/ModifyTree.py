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
        self.tree.expandAll()

        main_layout = QVBoxLayout()
        main_layout.addLayout(operator_layout)
        main_layout.addWidget(self.tree)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def onTreeClicked(self, index):
        row = self.tree.currentItem()
        print(index.row())
        print('Key={}, Value={}'.format(row.text(0), row.text(1)))

    def add_node(self):
        print('add node')
        item = self.tree.currentItem()
        print(item)
        node = QTreeWidgetItem(item)
        node.setText(0, 'node')
        node.setText(1, 'value')

    def update_node(self):
        print('update node')
        item = self.tree.currentItem()
        item.setText(0, 'up node')
        item.setText(1, 'up value')

    def delete_node(self):
        print('delete node')
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ModifyTree()
    main.show()
    sys.exit(app.exec_())