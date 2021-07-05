import tkinter as tk
from util import googleAuth, uiController
from util import GoogleAuthWatchDog, UIController, LocalConfig, Connector
from .menu import Menu
from .header import makeHeader
from .customTable import Tables
from .deleteDialog import DeleteDialog
from .coinlist import loadLocalAccounts, saveLocalAccount
from .announcement import Announcement
import json
from api import API

# ddsasRGbrW1 google-chrome --user-data-dir=/opt/chrome/walkerquan695@gmail.com --proxy-server=socks://45.76.192.110:5158 walkerquan695@gmail.com https://mail.google.com/ https://coinlist.co/ &

dataSource = [
    {
        "email": "walkerquan695@gmail.com",
        "pass1": "ddsasRGbrW1",
        "pass2": "ddsasRGbrW1",
        "server": "45.76.192.110",
        "port": "5158",
        "area": "Japan",
        "code": "hgnijq6x7ifpfj5p565xeh5h",
    },
    {
        "email": "sheliciawyson68@gmail.com",
        "user_data_dir": "/opt/chrome/",
        "pass1": "ddsasRGbrW1",
        "pass2": "ddsasRGbrW1",
        "server": "45.76.192.110",
        "port": "5099",
        "area": "Singapore",
        "code": "ccg2aakwt2zsqlkykwqpbfq5",
    }, {
        "email": "walkerquan695@gmail.com",
        "user_data_dir": "/opt/chrome/",
        "pass1": "ddsasRGbrW1",
        "pass2": "ddsasRGbrW1",
        "server": "45.76.192.110",
        "port": "5158",
        "area": "Japan",
        "code": "hgnijq6x7ifpfj5p565xeh5h",
    }
]


class Application(tk.Frame):
    googleAuth_watch_dog = GoogleAuthWatchDog()
    uiController = UIController()
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        Menu(master)
        self.create_widgets()
        Application.googleAuth_watch_dog.start()
        Application.uiController.start()

    def create_widgets(self):
        # 头部工具
        makeHeader(root=self.master)
        # 内容
        content = tk.Frame(self.master)
        content.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        # 底部
        bottom = tk.Frame(self.master)
        bottom.pack(side=tk.BOTTOM, fill=tk.X)
        
        # 公告
        Announcement(bottom)

        # 内容
        frame_canvas = tk.Frame(content)
        frame_canvas.pack(side="top", fill=tk.BOTH, expand=1)

        group_left = tk.Frame(frame_canvas, bg="#DCDCDC")
        group_left.pack(side="left", fill=tk.BOTH, expand=1)
        group_right = tk.Frame(frame_canvas, bg="#DCDCDC")
        group_right.pack(side="left", fill=tk.Y)

        canvas = tk.Canvas(group_left, bg="#DCDCDC")
        canvas.pack(side="top", fill=tk.BOTH, expand=1)
        # Link a scrollbar to the canvas
        vsb = tk.Scrollbar(group_right, orient=tk.VERTICAL, command=canvas.yview)
        vsb.pack(side="left", fill=tk.Y)
        hsb = tk.Scrollbar(group_left, orient=tk.HORIZONTAL, command=canvas.xview)
        hsb.pack(side="bottom", fill=tk.X)
        canvas.configure(yscrollcommand=vsb.set)
        canvas.configure(xscrollcommand=hsb.set)

        tableFrame = tk.Frame(canvas, bg="#F8F8FF")

# 集成账号
        self.table1 = Tables(tableFrame, columns=columns_online, dataSource=dataSource, actions=[
            {
                "text": "浏览器",
                "command": copyLine,
            }, {
                "text": "移除",
                "command": removeEmail,
            },
        ], deleteFunc=deleteRow, editFunc=editFunc)
        self.table1.master.pack()
# 本地账号
        self.table2 = Tables(tableFrame, columns=columns_local, dataSource=loadLocalAccounts(), actions=[
            {
                "text": "浏览器",
                "command": copyLine,
            },
        ], deleteFunc=deleteRow, editFunc=editFunc)
        canvas.create_window((0, 0), window=tableFrame, anchor='nw')
        tableFrame.update_idletasks()

        canvas.config(scrollregion=canvas.bbox("all"))

# 添加账号槽
        def add_data(**kwargs):
            self.table2.add_data(kwargs['data'])
        Connector().bind("addAccount", add_data)

        def change_table(**kwargs):
            current = kwargs['current']
            if current == 2:
                self.table1.master.pack_forget()
                self.table2.master.pack()
            else:
                self.table1.master.pack()
                self.table2.master.pack_forget()
        Connector().bind("changeTab", change_table)

    def init_data(self):
        # 获取集成账号
        config = LocalConfig().config
        existsEmails = set(json.loads(config.get('coinlist', 'email', fallback="[]")))
        API.syncCoinlistAccount(existsEmails)
        #  TODO
        pass

# 从本机移除集成邮箱账号,不再同步
def removeEmail(root, line, *args):
    def func():
        result = tk.messagebox.askokcancel(title = "移除",message="移除后,本设备不会再同步该账号 %s" % line['email'])
        if result:
            root.destroy()
            config = LocalConfig().config
            existsEmails = set(json.loads(config.get('coinlist', 'email', fallback="[]")))
            if line['email'] in existsEmails:
                existsEmails.remove(line['email'])
            config['coinlist']['email'] = json.dumps(list(existsEmails))
            LocalConfig().save(config)
            

    return func

def loadAccounts():
    data = []
    data.extend(loadLocalAccounts())
    return data

def copyLine(root, line, *args):
    def fun():
        r = tk.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(line)
        r.update() # now it stays on the clipboard after the window is closed
        r.destroy()
    return fun

def deleteRow(root, line, *args):
    print(line)
    deleteDia = DeleteDialog(root, line, "email")
    root.wait_window(deleteDia)
    if deleteDia.success:
        return True

def editFunc(line, changed, *args):
    print("保存")
    print(line)
    print(changed)        


# 密码加密处理
def encryptionPass(entry, text, variable):
    config = LocalConfig().config
    if config['auto'].getboolean('showpass'):
        entry.config(show='')
    else:
        entry.config(show='*')

    def changeStatus(**kwargs):
        if kwargs['show']:
            entry.config(show='')
        else:
            entry.config(show='*')
    Connector().bind("showpass", changeStatus)

def gooleCodeWatch(entry, sourvar, displayvar):
    displayvar.set(googleAuth(sourvar.get()))
    dog = Application.googleAuth_watch_dog
    dog.on_entry_created(displayvar, sourvar)

columns_online = [
            {
                "index": "email",
                "weight": 1.5,
                "title": "账号"
            },     {
                "index": "pass1",
                "weight": 0.8,
                "title": "coinlist密码",
                "editable": True,
                "slot": encryptionPass,
            },     {
                "index": "pass2",
                "weight": 0.8,
                "title": "邮箱密码",
                "editable": True,
                "slot": encryptionPass,
            },     {
                "index": "area",
                "weight": 0.6,
                "title": "区域",
            },     {
                "index": "code",
                "weight": 0.6,
                "title": "秘钥",
                "editable": True,
                "slot": gooleCodeWatch,
            },
        ]

columns_local = [
            {
                "index": "email",
                "weight": 1.5,
                "title": "账号"
            },     {
                "index": "pass1",
                "weight": 0.8,
                "title": "coinlist密码",
                "editable": True,
                "slot": encryptionPass,
            },     {
                "index": "pass2",
                "weight": 0.8,
                "title": "邮箱密码",
                "editable": True,
                "slot": encryptionPass,
            },     {
                "index": "area",
                "weight": 0.6,
                "title": "区域",
                "editable": True,
            },     {
                "index": "server",
                "weight": 0.8,
                "title": "服务器",
                "editable": True,
            },     {
                "index": "port",
                "weight": 0.4,
                "title": "端口",
                "editable": True,
            },     {
                "index": "code",
                "weight": 0.6,
                "title": "秘钥",
                "editable": True,
                "slot": gooleCodeWatch,
            },
        ]
