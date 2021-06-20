import tkinter as tk
from util import LocalConfig
import json

def makeHeader(root):
    frame_header = tk.Frame(root)
    frame_header.pack(side="top", fill=tk.X)
    
    lab_1 = tk.Label(frame_header, text="自建账号:", font=("华文行楷", 14), fg="green")
    lab_2 = tk.Label(frame_header, text="集成账号:", font=("华文行楷", 14), fg="green")

    txt1 = tk.StringVar()
    txt1.set(1)
    txt2 = tk.StringVar()
    txt2.set(1)
    
    num_1 = tk.Label(frame_header, textvariable=txt1)
    num_2 = tk.Label(frame_header, textvariable=txt2)

    lab_1.pack(side="left")
    num_1.pack(side="left")
    lab_2.pack(side="left")
    num_2.pack(side="left")

    tk.Button(frame_header, text="显示密码", command=showPass).pack(side="right")
    tk.Button(frame_header, text="同步账号", command=lambda: syncAccount(txt1, txt2)).pack(side="left")

def showPass():
    config = LocalConfig().config
    show = "yes"
    if config['auto'].getboolean('showpass'):
        show = "no"
    config['auto']['showpass'] = show
    LocalConfig().save(config)

def syncAccount(txt1, txt2):
    # TODO
    config = LocalConfig().config
    existsEmails = set(json.loads(config.get('coinlist', 'email', fallback="[]")))
    tk.messagebox.showinfo("同步账号", "正在同步\n %s" % "\n".join(existsEmails))
    txt1.set(100)
    txt2.set(200)

