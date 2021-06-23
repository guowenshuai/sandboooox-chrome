import onetimepass as otp
import threading
from threading import Thread
from apscheduler.schedulers.blocking import BlockingScheduler
import tkinter as tk

def googleAuth(secret):
    if secret == "":
        return 0
    try:
        code = otp.get_totp(secret)
    except Exception as e:
        return 0
    else:
        return code


def watch_dog_job(*args):
    watch_dog_obj = args[0]

    for idx, obj in enumerate(watch_dog_obj.entry_manage_list):
        txt = tk.StringVar()
        txt.set(googleAuth(obj['code']))
        obj['entry'].config(textvariable=txt, relief='flat')

class GoogleAuthWatchDog(threading.Thread):
    mutex = threading.Lock()
    entry_manage_list = list()

    def __init__(self):
        threading.Thread.__init__(self)
        self.scheduler = BlockingScheduler()
        self.scheduler.add_job(watch_dog_job, "interval", max_instances=10, seconds=1, args=[self])
        self.setDaemon(True)

    def run(self):
        self.scheduler.start()

    def on_entry_created(self, entry, code):
        self.mutex.acquire()
        self.entry_manage_list.append({
            "entry": entry,
            "code": code,
        })
        self.mutex.release()
