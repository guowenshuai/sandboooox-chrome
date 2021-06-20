import threading
from threading import Thread
from apscheduler.schedulers.blocking import BlockingScheduler
import tkinter as tk
from .config import LocalConfig

def watch_dog_job(*args):
    watch_dog_obj = args[0]
    config = LocalConfig().config

    if config['auto'].getboolean('showpass') == watch_dog_obj.lastStatus:
        return
    watch_dog_obj.lastStatus = not watch_dog_obj.lastStatus
    for idx, obj in enumerate(watch_dog_obj.entry_manage_list):
        txt = tk.StringVar()
        if config['auto'].getboolean('showpass'):
            txt.set(obj['text'])
        else: 
            txt.set("******")
        obj['entry'].config(textvariable=txt, relief='flat')

class UIController(threading.Thread):
    mutex = threading.Lock()
    entry_manage_list = list()

    def __init__(self):
        threading.Thread.__init__(self)
        self.scheduler = BlockingScheduler()
        self.lastStatus = True
        self.scheduler.add_job(watch_dog_job, "interval", max_instances=10, seconds=1, args=[self])
        self.setDaemon(True)

    def run(self):
        self.scheduler.start()

    def on_entry_created(self, entry, text):
        self.mutex.acquire()
        self.entry_manage_list.append({
            "entry": entry,
            "text": text,
        })
        self.mutex.release()
