import tkinter as tk
import time
import tkinter.font as tkFont

class Announcement(tk.Frame):
    def __init__(self, master):
        # self.master = tk.Frame(master)
        super().__init__(master)
        self.master = master
        self.__row_list = ["客服微信: 18810000000", "我们出售coinlist账号 https://www.baidu.com", "加入我们的社区!!!!!!!!!!!!!!!!!!!!!", "自动注册功能免费到2021.7.30"]
        self.create_widgets()

    def create_widgets(self):
        text = tk.StringVar()
        ent = tk.Entry(self.master, state='readonly', readonlybackground='white', fg='#008B45', font=tkFont.Font(family='Fixdsys', size=14, weight=tkFont.BOLD))
        ent.config(textvariable=text, relief='flat')
        text.set(self.__row_list[0])
        ent.pack(side="left", ipadx=20, expand=1, fill=tk.X)

        controller  = updateLine()
        controller.create(text, self.__row_list)
        controller.start()
        pass    

import threading
from threading import Thread
from apscheduler.schedulers.blocking import BlockingScheduler

def resetLine(*args):
    arg_obj = args[0]
    arg_obj.variable.set(arg_obj.row_list[arg_obj.idx])
    arg_obj.idx = arg_obj.idx + 1
    if arg_obj.idx >= len(arg_obj.row_list):
        arg_obj.idx = 0

class updateLine(threading.Thread):
    mutex = threading.Lock()

    def __init__(self):
        threading.Thread.__init__(self)
        self.scheduler = BlockingScheduler()
        self.scheduler.add_job(resetLine, "interval", max_instances=10, seconds=5, args=[self])
        self.setDaemon(True)

    def run(self):
        self.scheduler.start()

    def create(self, variable, row_list):
        self.variable = variable
        self.row_list = row_list
        self.idx = 0

