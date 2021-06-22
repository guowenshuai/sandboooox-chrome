import tkinter as tk
from api import AppCache

class PriceDialog(tk.Toplevel):
    def __init__(self, root, line=None):
        super().__init__()
        self.title('会员价格')
        self.attributes("-topmost", True)
        self.resizable(False, False)

        self.desc = {
          "免费自建位置": "2个",
          "自建账号位置": "10U/个",
          "集成账号": "根据市场行情浮动,请联系客服",
          "联系客服wx": "simon",
        }
    
        # 弹窗界面
        self.setup_UI()

        x = root.winfo_x()
        y = root.winfo_y()
        w = root.winfo_width()
        h = root.winfo_height()  
        print(x,y,w,h)
        self.geometry("+%d+%d" % (x + w/3, y + h/3))
        
    def setup_UI(self):
        for k,v in self.desc.items():
          row = tk.Frame(self)
          row.pack(fill="x")
          tk.Label(row, text="%s:" % k, width=15, anchor="w").pack(side=tk.LEFT)
          tk.Label(row, textvariable=tk.StringVar(value = v), width=30, anchor="w").pack(side=tk.LEFT)

        