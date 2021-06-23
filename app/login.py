import tkinter as tk
from util import LocalConfig


class LoginDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.success = False
        self.varName = tk.StringVar()
        self.varName.set('')
        self.varPwd = tk.StringVar()
        self.varPwd.set('')
        #创建标签
        self.labelName = tk.Label(self, text='用户名:', justify=tk.RIGHT, width=80)
        #将标签放到窗口上
        self.labelName.place(x=10, y=5, width=80, height=20)
        #创建文本框，同时设置关联的变量
        self.entryName = tk.Entry(self, width=80,textvariable=self.varName)
        self.entryName.place(x=100, y=5, width=80, height=20)
        self.labelPwd = tk.Label(self, text='密 码:', justify=tk.RIGHT, width=80)
        self.labelPwd.place(x=10, y=30, width=80, height=20)
        #创建密码文本框
        self.entryPwd = tk.Entry(self, show='*' ,width=80, textvariable=self.varPwd)
        self.entryPwd.place(x=100, y=30, width=80, height=20)
        self.buttonOk = tk.Button(self, text='登录', command=self.login)
        self.buttonOk.place(x=30, y=70, width=50, height=20)
        self.buttonCancel = tk.Button(self, text='取消', command=self.cancel)
        self.buttonCancel.place(x=90, y=70, width=50, height=20 )

    #登录按钮事件处理函数
    def login(self):
        name = self.varName.get()
        passwd = self.varPwd.get()
        if name=='admin'and passwd=='123456':
            self.success = True
        else:
            self.success = False
        #创建按钮组件，同时设置按钮事件处理函数   
        self.destroy()
    def cancel(self):
        self.entryPwd.config(show='')
        self.destroy()

        