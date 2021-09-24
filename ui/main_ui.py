#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import hashlib
import time

LOG_LINE_NUM = 0


class MY_GUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("三位目标识别工具")  # 窗口名
        self.init_window_name.geometry('1068x681+10+10')

        self.menu_btn_file = Menu(self.init_window_name, tearoff=0)
        self.menu_btn_file.add_command(label='打开场景', command=self.hello)
        self.menu_btn_file.add_separator()
        self.menu_btn_file.add_command(label='退出', command=self.init_window_name.quit)
        self.init_window_name.config(menu=self.menu_btn_file)

    def hello(self):
        print("hello world")




def gui_start():
    init_window = Tk()  # 实例化出一个父窗口
    MAIN_WIN = MY_GUI(init_window)

    # 设置根窗口默认属性
    MAIN_WIN.set_init_window()

    init_window.mainloop()  # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


if __name__ == '__main__':
    gui_start()
