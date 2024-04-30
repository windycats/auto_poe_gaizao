import threading
from time import sleep
import keyboard
import pyautogui
import pyperclip
import tkinter as tk


class MyThread(object):
    def __init__(self):
        self.gui = pyautogui
        self.going = True  # bool值开关控制

    def gaizao(self):
        print(1)

    def my_window(self):
        global text_box
        window = tk.Tk()
        window.title('poe')  # 标题
        window.attributes('-topmost', True)  # 显示到最顶层
        window.geometry("600x600")  # 窗口大小
        input1 = tk.Entry(window, width=60)  # 输入框的样式
        input1.pack()
        tk.Button(window, text='确认', width=60, command=lambda: self.main_method(input1.get())).pack()
        # 按钮调用改造方法并传入输入框的文本
        text_box = tk.Text(window, width=60, height=40)  # 设置按钮
        text_box.pack()
        # text_box.insert('1.0', pyperclip.paste())
        window.mainloop()

    def main_method(self, ct):

        while 1:
            if not self.going:  # 控制整体循环
                print("program_stopping")
                self.going = True
                break
            print("going ==", self.going)
            self.gui.moveTo()
            self.gui.rightClick()
            self.gui.moveTo()
            self.gui.rightClick()
            my_mode = pyperclip.paste()
            if ct in my_mode:  # 判断需要的词缀

                break
            else:
                self.gaizao()  # 调用改造方法
            sleep(0.5)

    def switch(self):
        while 1:
            keyboard.wait('F1')  # 这里暂时用的f1键控制
            self.going = not self.going
            text_box.insert('1.0', pyperclip.paste())
            # sleep(1)


if __name__ == "__main__":
    gui = MyThread()
    t = threading.Thread(target=gui.switch)  # 一直运行开关的线程
    t.daemon = True  # 守护线程
    t.start()  # 开启线程
    gui.my_window()  # 启动窗口
