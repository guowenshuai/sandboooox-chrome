import tkinter as tk

class MyDialog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('添加coinlist账号')
        # 弹窗界面
        self.setup_UI()
  
    def setup_UI(self):
        # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='email:', width=10).pack(side=tk.LEFT)
        self.email = tk.StringVar()
        tk.Entry(row1, textvariable=self.email, width=30).pack(side=tk.LEFT)
        # 第二行
        row2 = tk.Frame(self)
        row2.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row2, text='邮箱密码:', width=10).pack(side=tk.LEFT)
        self.pass1 = tk.StringVar()
        tk.Entry(row2, textvariable=self.pass1, width=30).pack(side=tk.LEFT)
        # 第三行
        row3 = tk.Frame(self)
        row3.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row3, text='coinlist密码:', width=10).pack(side=tk.LEFT)
        self.pass2 = tk.StringVar()
        tk.Entry(row3, textvariable=self.pass2, width=30).pack(side=tk.LEFT)

        rowarea = tk.Frame(self)
        rowarea.pack(fill="x", ipadx=1, ipady=1)
        self.area = tk.StringVar()
        tk.Label(rowarea, text='注册区域:', width=10).pack(side=tk.LEFT)
        tk.Entry(rowarea, textvariable=self.area, width=30).pack(side=tk.LEFT)
        # 第四行
        row4 = tk.Frame(self)
        row4.pack(fill="x", ipadx=1, ipady=1)
        server_top = tk.Frame(row4)
        # server_middle = tk.Frame(row4)
        # server_bottom = tk.Frame(row4)
        server_top.pack(fill="x",  ipadx=1, ipady=1)
        # server_middle.pack(fill="x",  ipadx=1, ipady=1)
        # server_bottom.pack(fill="x",  ipadx=1, ipady=1)

        self.server = tk.StringVar()
        self.port = tk.IntVar()
        tk.Label(server_top, text='服务器:', width=10).pack(side=tk.LEFT)
        tk.Entry(server_top, textvariable=self.server, width=15).pack(side=tk.LEFT)
        tk.Label(server_top, text='端口:', width=6).pack(side=tk.LEFT)
        tk.Entry(server_top, textvariable=self.port, width=8).pack(side=tk.LEFT)

        # self.serverUser = tk.StringVar()
        # self.serverPass = tk.StringVar()
        # tk.Label(server_top, text='服务器:', width=10).pack(side=tk.LEFT)
        # tk.Entry(server_top, textvariable=self.server, width=10).pack(side=tk.LEFT)
        # tk.Label(server_top, text='端口:', width=8).pack(side=tk.LEFT)
        # tk.Entry(server_top, textvariable=self.port, width=8).pack(side=tk.LEFT)

        # 第五行
        row5 = tk.Frame(self)
        row5.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row5, text='谷歌秘钥:', width=10).pack(side=tk.LEFT)
        self.code = tk.StringVar()
        tk.Entry(row5, textvariable=self.code, width=30).pack(side=tk.LEFT)


        row6 = tk.Frame(self)
        row6.pack(fill="x")
        tk.Button(row6, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row6, text="确定", command=self.ok).pack(side=tk.RIGHT)
    def ok(self):
        self.info = {
            "email": self.email.get(),
            "pass1": self.pass1.get(),
            "pass2": self.pass2.get(),
            "server": self.server.get(),
            "port": self.port.get(),
            "area": self.area.get(),
            "code": self.code.get(),
        }
        self.destroy() # 销毁窗口
    def cancel(self):
        self.info = None # 空！
        self.destroy()
