import tkinter as tk

class DeleteDialog(tk.Toplevel):
    def __init__(self, root, line, index):
        super().__init__()
        self.title('确认删除')
        self.attributes("-topmost", True)
        self.resizable(False, False)
        self.line = line
        self.index = index
        self.success = False

        # 弹窗界面
        self.setup_UI()

        # x = root.winfo_x()
        # y = root.winfo_y()
        # w = root.winfo_width()
        # h = root.winfo_height()  
        # self.geometry("+%d+%d" % (x + w/3, y + h/3))
        
    def setup_UI(self):
        row_tip = tk.Frame(self)
        row_tip.pack(fill="x")
        tk.Label(row_tip, text='删除账号后,账号将彻底删除').pack(side=tk.TOP)
        tk.Label(row_tip, text='无法恢复,请输入邮箱确认要删除').pack(side=tk.TOP)
        
        self.confirm = tk.StringVar(value="")
        
        row_check = tk.Frame(self)
        row_check.pack(fill="x")
        tk.Label(row_check, text='邮箱:', width=10, anchor="w").pack(side=tk.LEFT)
        tk.Entry(row_check, textvariable=self.confirm, width=20).pack(side=tk.LEFT)

        row_sub = tk.Frame(self)
        row_sub.pack(fill="x")
        tk.Button(row_sub, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row_sub, text="确定", command=self.ok).pack(side=tk.RIGHT)
    
    def ok(self):
        if self.confirm.get() == self.line[self.index]:
            self.success = True
        self.destroy() 
    def cancel(self):
        self.success = False
        self.destroy()
