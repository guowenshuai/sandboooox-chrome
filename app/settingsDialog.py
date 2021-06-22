import tkinter as tk
from util import LocalConfig
from tkinter.filedialog import askopenfilename

class SettingsDialog(tk.Toplevel):
    def __init__(self, root, line=None):
        super().__init__()
        self.title('设置')
        self.resizable(width=False, height=False)
        # self.positionfrom(who="program")
        self.attributes("-topmost", True)
        config = LocalConfig().config
       
    #   设置浏览器
        self.exec = tk.StringVar(value=config.get("browser", "exec"))
        self.showpass = tk.IntVar()
        if config['auto'].getboolean('showpass'):
            self.showpass.set(1)

    #   是否展示密码
 
        # 弹窗界面
        self.setup_UI()
        x = root.winfo_x()
        y = root.winfo_y()
        w = root.winfo_width()
        h = root.winfo_height()  
        self.geometry("+%d+%d" % (x + w/3, y + h/3))

    def setup_UI(self):
        # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='浏览器:', width=10, anchor="w").pack(side=tk.LEFT)
        tk.Entry(row1, textvariable=self.exec, width=20).pack(side=tk.LEFT)
        tk.Button(row1, text="选择", command=lambda: self.selectFile()).pack(side=tk.LEFT)
        # 第二行
        row2 = tk.Frame(self)
        row2.pack(fill="x", ipadx=1, ipady=1)
        tk.Label(row2, text='显示密码:', width=10, anchor="w").pack(side=tk.LEFT)
        tk.Checkbutton(row2, variable=self.showpass, width=30, anchor="w").pack(side=tk.RIGHT)
       
        row6 = tk.Frame(self)
        row6.pack(fill="x")
        tk.Button(row6, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row6, text="确定", command=self.ok).pack(side=tk.RIGHT)
    def selectFile(self):
        filename = askopenfilename(parent=self, title='选择谷歌浏览器',  initialdir='~')    
        self.exec.set(filename)
    def ok(self):
        config = LocalConfig().config
        config['browser']['exec'] = self.exec.get()
        config['auto']["showpass"] = "no"
        if self.showpass.get() == 1:
            config['auto']["showpass"] = "yes"
        LocalConfig().save(config)
        self.destroy() # 销毁窗口
    def cancel(self):
        self.destroy()
