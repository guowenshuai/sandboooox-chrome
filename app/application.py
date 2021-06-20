import tkinter as tk
from util import googleAuth, uiController
from .table import makeTableCell
from util import GoogleAuthWatchDog, UIController
from .menu import Menu
from .header import makeHeader

# ddsasRGbrW1 google-chrome --user-data-dir=/opt/chrome/walkerquan695@gmail.com --proxy-server=socks://45.76.192.110:5158 walkerquan695@gmail.com https://mail.google.com/ https://coinlist.co/ &

data = [
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
        "email": "4@gmail.com",
        "user_data_dir": "/opt/chrome/",
        "pass1": "ddsasRGbrW1",
        "pass2": "ddsasRGbrW1",
        "server": "45.76.192.110",
        "port": "5158",
        "area": "Japan",
        "code": "hgnijq6x7ifpfj5p565xeh5h",
    },
    {
        "email": "3@gmail.com",
        "user_data_dir": "/opt/chrome/",
        "pass1": "ddsasRGbrW1",
        "pass2": "ddsasRGbrW1",
        "server": "45.76.192.110",
        "port": "5099",
        "area": "Singapore",
        "code": "ccg2aakwt2zsqlkykwqpbfq5",
    }, {
        "email": "2@gmail.com",
        "user_data_dir": "/opt/chrome/",
        "pass1": "ddsasRGbrW1",
        "pass2": "ddsasRGbrW1",
        "server": "45.76.192.110",
        "port": "5158",
        "area": "Japan",
        "code": "hgnijq6x7ifpfj5p565xeh5h",
    },
    {
        "email": "1@gmail.com",
        "user_data_dir": "/opt/chrome/",
        "pass1": "ddsasRGbrW1",
        "pass2": "ddsasRGbrW1",
        "server": "45.76.192.110",
        "port": "5099",
        "area": "Singapore",
        "code": "ccg2aakwt2zsqlkykwqpbfq5",
    },
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
        canvas.create_window((0, 0), window=tableFrame, anchor='nw')

        for i in range(len(data)):
            makeTableCell(self.master, tableFrame, data[i], i, Application.googleAuth_watch_dog, Application.uiController)
        tableFrame.update_idletasks()

        canvas.config(scrollregion=canvas.bbox("all"))

    def say_hi(self):
        print("hi there, everyone!")
        secret = "hgnijq6x7ifpfj5p565xeh5h"
        print(googleAuth(secret))
