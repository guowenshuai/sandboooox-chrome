import tkinter as tk
from util import googleAuth
from .createLnkDialog import ChromeDialog
from util import LocalConfig
   
def makeTableCell(wd, root, line, row, dog, uicontroller):
    config = LocalConfig().config
    # email
    email_label = copiedLabel(root, line['email'], weight=2.5)
    email_label.grid(row=row, column=0, padx=5, pady=3, ipadx=1, ipady=1)
    # pass1
    pass1_txt = line['pass1']
    if not config['auto'].getboolean('showpass'):
        pass1_txt = "******"
    pass1_label = copiedLabel(root, text=pass1_txt)
    pass1_label.grid(row=row, column=1, padx=5, pady=3, ipadx=1, ipady=1)
    uicontroller.on_entry_created(pass1_label, line['pass1'])
    # pass2
    pass2_txt = line['pass1']
    if not config['auto'].getboolean('showpass'):
        pass2_txt = "******"    
    pass2_label = copiedLabel(root, text=pass2_txt)
    pass2_label.grid(row=row, column=2, padx=5, pady=3, ipadx=1, ipady=1)
    uicontroller.on_entry_created(pass2_label, line['pass2'])
    # area
    area_label = copiedLabel(root, text=line['area'])
    area_label.grid(row=row, column=3, padx=5, pady=3, ipadx=1, ipady=1)
    # google code
    code_label = copiedLabel(root, googleAuth(line['code']))
    code_label.grid(row=row, column=4, padx=5, pady=3, ipadx=1, ipady=1)
    dog.on_entry_created(code_label, line['code'])

    # 打开浏览器
    tk.Button(root, text="浏览器", command=lambda: openChrome(config, line)).grid(row=row, column=5, padx=5, pady=3, ipadx=1, ipady=1)
    tk.Button(root, text="复制", command=lambda: copyLine(line)).grid(row=row, column=6, padx=5, pady=3, ipadx=1, ipady=1)
    tk.Button(root, text="编辑", command=lambda: editLine(wd, line)).grid(row=row, column=7, padx=5, pady=3, ipadx=1, ipady=1)

def copiedLabel(root, text, weight=1):
    width = 10
    ent = tk.Entry(root, state='readonly', readonlybackground='white', fg='black', width=int(width*weight))
    txt = tk.StringVar()
    txt.set(text)
    ent.config(textvariable=txt, relief='flat')
    return ent

def copyLine(line):
    r = tk.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(line)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()

import os
import subprocess

def openChrome(config, line):
    # TODO 检查浏览器执行路径
    browserExec = config.get("browser", "exec")
    if not os.access(browserExec, os.X_OK):
        tk.messagebox.showinfo("警告", '''请设置正确的谷歌浏览器执行路径
        我的->设置->浏览器''')

    # TODO 检查本地存储路径
    print("open chrome %s" % line)
    user_data = os.path.join(line["user_data_dir"], line["email"])
    cmd = "%s --user-data-dir=%s --proxy-server=socks://%s:%s %s https://mail.google.com/ https://coinlist.co/ &" % (browserExec, user_data, line["server"], line["port"], line["email"])
    print(cmd)
    subprocess.Popen(cmd, cwd=line["user_data_dir"], shell=True,)

def editLine(root, line):
    inputDialog = ChromeDialog(root, line=line)
    root.wait_window(inputDialog) # 这一句很重要！！！
    # TODO 提交并保存
    print(inputDialog.info)
    return inputDialog.info