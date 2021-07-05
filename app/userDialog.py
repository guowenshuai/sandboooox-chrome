import tkinter as tk
from api import AppCache
# 用户信息

class UserDialog(tk.Toplevel):
    def __init__(self, root, line=None):
        super().__init__()
        self.title('我的信息')
        self.attributes("-topmost", True)
        self.resizable(False, False)

        self.desc = {
          "uuid": "uuid",
          "username": "用户名",
          "email": "邮箱",
          "phone": "电话",
          "customNumbers": "自建账号",
          "coinlistNumbers": "集成账号",
        }
        self.userInfo = AppCache.user
    
        # 弹窗界面
        self.setup_UI()

        x = root.winfo_x()
        y = root.winfo_y()
        w = root.winfo_width()
        h = root.winfo_height()  
        print(x,y,w,h)
        self.geometry("+%d+%d" % (x + w/3, y + h/3))
        
    def setup_UI(self):
        for k,v in self.userInfo.items():
          print(k,v)
          row = tk.Frame(self)
          row.pack(fill="x")
          tk.Label(row, text="%s:" % self.desc[k], width=10, anchor="w").pack(side=tk.LEFT)
          tk.Label(row, textvariable=tk.StringVar(value = v), width=20, anchor="w").pack(side=tk.LEFT)

        