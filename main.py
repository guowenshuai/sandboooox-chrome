from threading import local
import tkinter as tk
import time
from app import Application
from util import LocalConfig\

LocalConfig()
root = tk.Tk()
root.geometry("1000x800")
root.maxsize(1000, 800)
root.title("sandbooooooox")
app = Application(master=root)
app.mainloop()