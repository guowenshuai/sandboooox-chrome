import tkinter as tk
from util import LocalConfig, Connector
import json
from api import AppCache


def makeHeader(root):
    frame_header = tk.Frame(root)
    frame_header.pack(side="top", fill=tk.X)
    
    lab_1 = tk.Label(frame_header, text="自建账号:", font=("华文行楷", 12), fg="red")
    lab_2 = tk.Label(frame_header, text="集成账号:", font=("华文行楷", 12), fg="green")
    lab_3 = tk.Label(frame_header, text="已导入:", font=("华文行楷", 12), fg="green")

    txt1 = tk.StringVar()
    txt1.set(1)
    txt2 = tk.StringVar()
    txt2.set(1)
    txt3 = tk.StringVar()
    txt3.set(1)
    
    num_1 = tk.Label(frame_header, textvariable=txt1)
    num_2 = tk.Label(frame_header, textvariable=txt2)
    num_3 = tk.Label(frame_header, textvariable=txt3)
    
    lab_2.pack(side="left")
    num_2.pack(side="left")
    lab_3.pack(side="left")
    num_3.pack(side="left")
    tk.Button(frame_header, text="同步", command=lambda: syncAccount(txt1, txt2, txt3)).pack(side="left")

    lab_1.pack(side="left")
    num_1.pack(side="left")

    tk.Button(frame_header, text="显示(隐藏)密码", command=showPass).pack(side="right")

    def change_table():
        current = AppCache().config['current']
        Connector().send("changeTab", current=current)
        AppCache().config['current'] = not current

    tk.Button(frame_header, text="切换", command=change_table).pack(side=tk.LEFT)


def showPass():
    config = LocalConfig().config
    show = "yes"
    if config['auto'].getboolean('showpass'):
        show = "no"
    config['auto']['showpass'] = show
    LocalConfig().save(config)
    Connector().send("showpass", show=config['auto'].getboolean('showpass'))

def syncAccount(txt1, txt2, txt3):
    # TODO
    config = LocalConfig().config
    existsEmails = set(json.loads(config.get('coinlist', 'email', fallback="[]")))
    tk.messagebox.showinfo("同步账号", "正在同步\n %s" % "\n".join(existsEmails))
    txt1.set(100)
    txt2.set(200)
    txt3.set(30)

