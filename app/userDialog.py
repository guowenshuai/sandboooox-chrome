import tkinter as tk

# 用户信息

class UserDialog(tk.Toplevel):
    def __init__(self, root, line=None):
        super().__init__()
        self.title('我的信息')
        
        self.email = tk.StringVar(value = line['email'] if line != None else "")
        self.pass1 = tk.StringVar(value = line['pass1'] if line != None else "")
        self.pass2 = tk.StringVar(value = line['pass2'] if line != None else "")
        self.area = tk.StringVar(value = line['area'] if line != None else "")
        self.server = tk.StringVar(value = line['server'] if line != None else "")
        self.port = tk.IntVar(value = line['port'] if line != None else 0)
        self.code = tk.StringVar(value = line['code'] if line != None else "")

        # 弹窗界面
        self.setup_UI()

        x = root.winfo_x()
        y = root.winfo_y()
        w = root.winfo_width()
        h = root.winfo_height()  
        print(x,y,w,h)
        self.geometry("+%d+%d" % (x + w/3, y + h/3))
    def setup_UI(self):
      # 第一行（两列）
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='email:', width=10).pack(side=tk.LEFT)
        tk.Entry(row1, textvariable=self.email, width=30).pack(side=tk.LEFT)