from tkinter import Tk, Listbox, Button, Label, messagebox


root = Tk()  # 创建窗口对象的背景色
# 创建两个列表
li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']
listb = Listbox(root)  # 创建两个列表组件
listb2 = Listbox(root)
for item in li:  # 第一个小部件插入数据
    listb.insert(0, item)

for item in movie:  # 第二个小部件插入数据
    listb2.insert(0, item)


def hello_call_back():
   messagebox.showinfo("Hello Python", "Hello Runoob")


btn = Button(root, text="click me", command=hello_call_back)
lb = Label(root, text="hello world")

listb.pack()  # 将小部件放置到主窗口中
listb2.pack()
btn.pack()
lb.pack()
root.mainloop()  # 进入消息循环
