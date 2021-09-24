from tkinter import *

root = Tk()


def callback():
    print("~被调用啦~")


# 创建一个顶级菜单
menu_bar = Menu(root)

file_menu = Menu(menu_bar)
file_menu.add_command(label="Hello", command=callback)
file_menu.add_command(label="Quit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

connect_bar = Menu(menu_bar)
connect_bar.add_command(label="Detect Online")
connect_bar.add_command(label="Preference")
menu_bar.add_cascade(label="Connect", menu=connect_bar)

help_bar = Menu(menu_bar)
help_bar.add_command(label="About")
help_bar.add_command(label="Help")
menu_bar.add_cascade(label="About", menu=help_bar)

# 显示菜单
root.config(menu=menu_bar)

root.mainloop()