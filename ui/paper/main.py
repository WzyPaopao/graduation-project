# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1209, 779)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(660, 380, 541, 361))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_3.setGeometry(QtCore.QRect(10, 40, 521, 311))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(290, 10, 451, 361))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_3)
        self.graphicsView.setGeometry(QtCore.QRect(10, 40, 431, 311))
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 271, 361))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 20, 241, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 1, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setProperty("value", 20)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 380, 641, 361))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser.setGeometry(QtCore.QRect(10, 40, 621, 311))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(750, 10, 451, 361))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.groupBox_6)
        self.graphicsView_2.setGeometry(QtCore.QRect(10, 40, 431, 311))
        self.graphicsView_2.setObjectName("graphicsView_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1209, 28))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.actionf = QtWidgets.QAction(MainWindow)
        self.actionf.setObjectName("actionf")
        self.actionf_2 = QtWidgets.QAction(MainWindow)
        self.actionf_2.setObjectName("actionf_2")
        self.actiona = QtWidgets.QAction(MainWindow)
        self.actiona.setObjectName("actiona")
        self.actiona_2 = QtWidgets.QAction(MainWindow)
        self.actiona_2.setObjectName("actiona_2")
        self.actiona_3 = QtWidgets.QAction(MainWindow)
        self.actiona_3.setObjectName("actiona_3")
        self.actionxiug = QtWidgets.QAction(MainWindow)
        self.actionxiug.setObjectName("actionxiug")
        self.actiona_4 = QtWidgets.QAction(MainWindow)
        self.actiona_4.setObjectName("actiona_4")
        self.actiona_5 = QtWidgets.QAction(MainWindow)
        self.actiona_5.setObjectName("actiona_5")
        self.actiona_6 = QtWidgets.QAction(MainWindow)
        self.actiona_6.setObjectName("actiona_6")
        self.actiona_7 = QtWidgets.QAction(MainWindow)
        self.actiona_7.setObjectName("actiona_7")
        self.actiona_8 = QtWidgets.QAction(MainWindow)
        self.actiona_8.setObjectName("actiona_8")
        self.actiona_9 = QtWidgets.QAction(MainWindow)
        self.actiona_9.setObjectName("actiona_9")
        self.menu_4.addAction(self.actiona)
        self.menu_4.addAction(self.actionxiug)
        self.menu_4.addAction(self.actiona_3)
        self.menu_4.addSeparator()
        self.menu_4.addAction(self.actiona_2)
        self.menu_5.addAction(self.actiona_4)
        self.menu_5.addAction(self.actiona_8)
        self.menu_5.addAction(self.actiona_6)
        self.menu_5.addSeparator()
        self.menu_5.addAction(self.actiona_5)
        self.menu_5.addAction(self.actiona_9)
        self.menu_5.addAction(self.actiona_7)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "彩色图像"))
        self.groupBox_3.setTitle(_translate("MainWindow", "深度图像"))
        self.groupBox_4.setTitle(_translate("MainWindow", "配置"))
        self.label.setText(_translate("MainWindow", "图像配置"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.checkBox_3.setText(_translate("MainWindow", "彩色图像"))
        self.checkBox_2.setText(_translate("MainWindow", "红外IR图像"))
        self.checkBox.setText(_translate("MainWindow", "深度图像"))
        self.label_2.setText(_translate("MainWindow", "帧率配置"))
        self.label_3.setText(_translate("MainWindow", "帧率："))
        self.label_4.setText(_translate("MainWindow", "FPS"))
        self.pushButton_4.setText(_translate("MainWindow", "确定"))
        self.label_7.setText(_translate("MainWindow", "数据选择"))
        self.pushButton_2.setText(_translate("MainWindow", "上传深度图"))
        self.pushButton_5.setText(_translate("MainWindow", "上传数据集"))
        self.pushButton_3.setText(_translate("MainWindow", "保存当前帧"))
        self.groupBox_5.setTitle(_translate("MainWindow", "控制台"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'黑体\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10.8pt;\"><br /></p></body></html>"))
        self.groupBox_6.setTitle(_translate("MainWindow", "红外IR图像"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "连接"))
        self.menu_3.setTitle(_translate("MainWindow", "关于"))
        self.menu_4.setTitle(_translate("MainWindow", "算法"))
        self.menu_5.setTitle(_translate("MainWindow", "数据"))
        self.actionf.setText(_translate("MainWindow", "算法注册"))
        self.actionf_2.setText(_translate("MainWindow", "f"))
        self.actiona.setText(_translate("MainWindow", "注册算法"))
        self.actiona_2.setText(_translate("MainWindow", "算法推理"))
        self.actiona_3.setText(_translate("MainWindow", "删除算法"))
        self.actionxiug.setText(_translate("MainWindow", "修改算法"))
        self.actiona_4.setText(_translate("MainWindow", "上传深度图"))
        self.actiona_5.setText(_translate("MainWindow", "上传数据集"))
        self.actiona_6.setText(_translate("MainWindow", "删除深度图"))
        self.actiona_7.setText(_translate("MainWindow", "删除数据集"))
        self.actiona_8.setText(_translate("MainWindow", "修改深度图"))
        self.actiona_9.setText(_translate("MainWindow", "修改数据集"))