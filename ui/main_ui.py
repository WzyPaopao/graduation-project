#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import cv2
from PIL import Image, ImageTk


LOG_LINE_NUM = 0


class MY_GUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("三位目标识别工具")  # 窗口名
        self.init_window_name.geometry('1068x681+10+10')

        self.menu_bar = Menu(self.init_window_name)

        self.file_menu = Menu(self.menu_bar)
        self.file_menu.add_command(label='打开场景', command=self.hello)
        self.file_menu.add_command(label='关闭场景')
        self.file_menu.add_command(label='重新载入场景')
        self.file_menu.add_command(label='保存识别结果')
        self.file_menu.add_command(label='退出', command=self.init_window_name.quit)

        self.connect_menu = Menu(self.menu_bar)
        self.connect_menu.add_command(label='建立连接')
        self.connect_menu.add_command(label='在线识别')
        self.connect_menu.add_command(label='设置')
        self.connect_menu.add_command(label='断开连接')

        self.about_menu = Menu(self.menu_bar)
        self.about_menu.add_command(label='关于系统')
        self.about_menu.add_command(label='帮助')

        self.menu_bar.add_cascade(label='文件', menu=self.file_menu)
        self.menu_bar.add_cascade(label='连接', menu=self.connect_menu)
        self.menu_bar.add_cascade(label='关于', menu=self.about_menu)

        self.init_window_name.config(menu=self.menu_bar)

        self.cap = cv2.VideoCapture(0)  # 创建摄像头对象

        # 界面画布更新图像
        def tkImage():
            ref, frame = self.cap.read()
            frame = cv2.flip(frame, 1)  # 摄像头翻转
            cvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            pilImage = Image.fromarray(cvimage)
            pilImage = pilImage.resize((image_width, image_height), Image.ANTIALIAS)
            tkImage = ImageTk.PhotoImage(image=pilImage)
            return tkImage

        image_width = 850
        image_height = 500
        self.canvas = Canvas(self.init_window_name, bg='white', width=image_width, height=image_height)  # 绘制画布
        self.canvas.place(x=200, y=30)

        while True:
            self.pic = tkImage()
            self.canvas.create_image(0, 0, anchor='nw', image=self.pic)
            self.init_window_name.update()
            self.init_window_name.after(100)

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
