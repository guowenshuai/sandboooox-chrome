import tkinter as tk
from util import LocalConfig, Connector
import json


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
    
    iv_default = tk.IntVar()
    def change_table():
        current = 2
        if iv_default.get() == 1:
            current = 1
        Connector().send("changeTab", current=current)

    rb_default1 = tk.Radiobutton(frame_header, text='集成账号', value=1, variable=iv_default, command=change_table)
    rb_default2 = tk.Radiobutton(frame_header, text='自建账号', value=2, variable=iv_default, command=change_table)
    iv_default.set(1)


    rb_default1.pack(side=tk.LEFT)
    lab_2.pack(side="left")
    num_2.pack(side="left")
    lab_3.pack(side="left")
    num_3.pack(side="left")
    tk.Button(frame_header, text="同步", command=lambda: syncAccount(txt1, txt2, txt3)).pack(side="left")

    rb_default2.pack(side=tk.LEFT)
    lab_1.pack(side="left")
    num_1.pack(side="left")

    tk.Button(frame_header, text="显示(隐藏)密码", command=showPass).pack(side="right", padx=10)
    
    tk.Button(frame_header, text="测试", command=test).pack(side="right")

from util import detect_port
def test():
    detect_port("127.0.0.1", 9999)
    pass
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

