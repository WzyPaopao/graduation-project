from PyQt5.Qt import QApplication, QMainWindow, QWidget
import sys
import add_alg, dataset, inference, main, preprocess


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = QMainWindow()
    # ui = add_alg.Ui_Form()
    # ui = dataset.Ui_Form()
    ui = inference.Ui_Form()
    # ui = main.Ui_MainWindow()
    ui.setupUi(main_win)
    #
    # widget = QWidget()
    # data_ui = dataset.Ui_Form()
    # data_ui.setupUi(widget)

    # ui.pushButton_5.clicked.connect(data_ui.show)

    titles = ['注册算法', '数据集上传', '模型推理', '三维目标检测工具', '数据预处理']
    main_win.setWindowTitle(titles[0])
    # main_win.statusBar().setWindowTitle('等待摄像头连接')
    main_win.show()
    sys.exit(app.exec_())
