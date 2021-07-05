import tkinter as tk
from util import LocalConfig
import json
from .customTable import Tables

class EditEmailDialog(tk.Toplevel):
    def __init__(self, root):
        super().__init__()
        self.title('编辑邮箱')
        self.attributes("-topmost", True)

        self.resizable(False, False)
        config = LocalConfig().config
        self.emails = json.loads(config.get('coinlist', 'email', fallback="[]"))
        # 弹窗界面
        self.setup_UI()

    def setup_UI(self):
        row1 = tk.Frame(self)
        row1.pack(side=tk.TOP, fill="x")

        scroll = tk.Scrollbar(row1)
        #设置text的大小
        text = tk.Text(row1,width=40,height=20)
        
        #将滚动条填充,放在右边，y是竖直方向
        text.pack(side=tk.LEFT,fill=tk.Y)
        scroll.pack(side=tk.RIGHT,fill=tk.Y)
        
        #将滚动条和文本框关联
        scroll.config(command=text.yview)
        text.config(yscrollcommand=scroll.set) 


        text.insert(1.0, "\n".join(self.emails))

        row6 = tk.Frame(self)
        row6.pack(side=tk.BOTTOM, fill="x")
        tk.Button(row6, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row6, text="确定", command=self.ok).pack(side=tk.RIGHT)

    def ok(self):
        config = LocalConfig().config
        config['coinlist']['email'] = json.dumps(self.emails)
        LocalConfig().save(config)
        self.destroy() # 销毁窗口
    def cancel(self):
        self.destroy()