from PyQt5.QtWidgets import QApplication, QMainWindow
import inference, add_alg, main, preprocess_with_label, dataset, preprocess
import sys


if __name__ == '__main__':
    title = ['模型推理', '算法注册', '三维目标检测工具', '数据预处理', '数据集上传']
    app = QApplication(sys.argv)
    main_window = QMainWindow()

    # ui = main.Ui_MainWindow()
    # ui = dataset.Ui_Form()
    # ui = add_alg.Ui_Form()
    ui = inference.Ui_Form()
    # ui = preprocess.Ui_Form()
    ui.setupUi(main_window)
    main_window.setWindowTitle(title[0])
    main_window.show()
    sys.exit(app.exec_())
