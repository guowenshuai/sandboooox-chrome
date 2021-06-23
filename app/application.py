import tkinter as tk
from util import googleAuth, uiController
from .table import makeTableCell
from util import GoogleAuthWatchDog, UIController, LocalConfig, Connector
from .menu import Menu
from .header import makeHeader
from .customTable import Tables
from .deleteDialog import DeleteDialog
from .coinlist import loadLocalAccounts, saveLocalAccount
# ddsasRGbrW1 google-chrome --user-data-dir=/opt/chrome/walkerquan695@gmail.com --proxy-server=socks://45.76.192.110:5158 walkerquan695@gmail.com https://mail.google.com/ https://coinlist.co/ &

dataSource = [
    {
        "email": "walkerquan695@gmail.com",
        "user_data_dir": "/opt/chrome/",
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
        #表头
        makeHeader(root=self.master)
        # 表格
        frame_canvas = tk.Frame(self.master)
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
        table1 = Tables(tableFrame, columns=columns_online, dataSource=dataSource, actions=[
            {
                "text": "浏览器",
                "command": copyLine,
            },
        ], deleteFunc=deleteRow, editFunc=editRow)
        table1.master.pack()
# 本地账号
        table2 = Tables(tableFrame, columns=columns_online, dataSource=loadLocalAccounts(), actions=[
            {
                "text": "浏览器",
                "command": copyLine,
            },
        ], deleteFunc=deleteRow, editFunc=editRow)
        # table2.destory()
        canvas.create_window((0, 0), window=tableFrame, anchor='nw')
        tableFrame.update_idletasks()

        canvas.config(scrollregion=canvas.bbox("all"))

# 添加账号槽
        def add_data(**kwargs):
            table1.add_data(kwargs['data'])
        Connector().bind("addAccount", add_data)

        self.current = "online"
        def change_table():
            if self.current == "online":
                table1.master.pack_forget()
                table2.master.pack()
                self.current = "local"
            else:
                table1.master.pack()
                table2.master.pack_forget()
                self.current = "online"

        tk.Button(self.master, text="切换table", command=change_table).pack(side=tk.LEFT)

def loadAccounts():
    data = []
    data.extend(loadLocalAccounts())
    return data

def copyLine(root, line):
    def fun():
        r = tk.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(line)
        r.update() # now it stays on the clipboard after the window is closed
        r.destroy()
    return fun

def deleteRow(root, line):
    print(line)
    deleteDia = DeleteDialog(root, line, "email")
    root.wait_window(deleteDia)
    if deleteDia.success:
        return True

def editRow(line, changed):
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

def gooleCodeWatch(entry, text, variable):
    variable.set(googleAuth(text))
    dog = Application.googleAuth_watch_dog
    dog.on_entry_created(entry, text)

columns_online = [
            {
                "index": "email",
                "weight": 2,
                "title": "账号"
            },     {
                "index": "pass1",
                "weight": 1,
                "title": "coinlist密码",
                "editable": True,
                "slot": encryptionPass,
            },     {
                "index": "pass2",
                "weight": 1,
                "title": "邮箱密码",
                "editable": True,
                "slot": encryptionPass,
            },     {
                "index": "area",
                "weight": 1,
                "title": "区域",
            },     {
                "index": "code",
                "weight": 1,
                "title": "google秘钥",
                "editable": True,
                "slot": gooleCodeWatch,
            },
        ]
