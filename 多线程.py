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
        print("——————————————————————————————改造中——————————————————————————————")

    def hundun(self):
        print("——————————————————————————————混沌中——————————————————————————————")

    def jihui(self):
        print("——————————————————————————————机会中——————————————————————————————")

    def deal_text(self):    # 处理输入的参数用“、”分割
        try:
            text_list = (input1.get().split('、'))
            print(text_list)
        except:
            print(1)
        finally:
            return text_list

    def my_window(self):    # 界面窗口
        global text_box, window, var, input1
        window = tk.Tk()
        window.title('POE')  # 标题
        win_img = tk.PhotoImage(file=r'C:\Users\EDY\Pictures\Saved Pictures\小皮.gif')
        window.iconphoto(False, win_img)
        window.attributes('-topmost', True)  # 显示到最顶层
        window.geometry("600x700+1200+100")  # 窗口大小
        input1 = tk.Entry(window, width=60)  # 输入框的样式
        input1.pack()
        input2 = tk.Entry(window, width=10)
        input2.insert(0,1)
        input2.pack()
        tk.Button(window, text='确认', width=60,
                  command=lambda: (
                  window.withdraw(), self.main_method(self.deal_text(), var.get(), input2.get()))).pack()
        # 按钮调用改造方法并传入输入框的文本
        text_box = tk.Text(window, width=60, height=40)  # 设置按钮
        text_box.pack(padx=10)
        var = tk.StringVar(value=1)
        rdo = tk.Radiobutton(window, text="改造", variable=var, value=1)
        rdo.pack(side=tk.LEFT, padx=90)
        tk.Radiobutton(window, text="混沌", variable=var, value=2).pack(side=tk.LEFT)
        tk.Radiobutton(window, text="机会", variable=var, value=3).pack(side=tk.LEFT, padx=90)

        window.mainloop()

    def main_method(self, text_list, code, num):

        while 1:
            count_num = 0
            if not self.going:  # 控制整体循环
                print("program_stopping")
                self.going = True
                break
            print("going ==", self.going)
            self.gui.moveTo()
            self.gui.hotkey('ctrl', 'alt', 'c')
            my_mode = pyperclip.paste()
            for ct in text_list:
                if ct in my_mode:  # 判断需要的词缀
                    print(ct + "满足条件")
                    print("存在次数为" + str(count_num))
                    count_num += 1
                    if count_num == int(num):
                        text_box.delete('1.0', tk.END)  # 清除文本框
                        text_box.insert('1.0', pyperclip.paste())  # 把剪切板的数据放进去
                        window.deiconify()
                        return
                    else:
                        continue
                else:
                    print(ct+"不存在跳过")
                    continue
            print("存在个数为："+str(count_num)+"需要个数为："+num)
            if code == '1':
                self.gaizao()  # 调用改造方法
            elif code == '2':
                self.hundun()  # 调用的混沌方法
            elif code == '3':
                self.jihui()  # 调用机会重铸的方法
            else:
                print("code参数错误")
            sleep(1)

    def switch(self):
        while 1:
            keyboard.wait('f2')  # 这里暂时用的k键控制
            self.going = not self.going
            text_box.delete('1.0', tk.END)  # 清除文本框
            text_box.insert('1.0', pyperclip.paste())  # 呈现把剪切板的文本
            window.deiconify()
            # sleep(1)


if __name__ == "__main__":
    gui = MyThread()
    t = threading.Thread(target=gui.switch)  # 一直运行开关的线程
    t.daemon = True  # 守护线程
    t.start()  # 开启线程
    gui.my_window()  # 启动窗口
