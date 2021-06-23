from threading import local
import tkinter as tk
import time, os
from app import Application, LoginDialog
from util import LocalConfig

LocalConfig()
root = tk.Tk()
root.geometry("1000x800")
root.maxsize(1000, 800)
root.title("sandbooooooox")
root.withdraw()

def run(root):

    app = Application(master=root)
    app.mainloop()

# loginDialog = LoginDialog()
# root.wait_window(loginDialog)
# if loginDialog.success:
#     root.deiconify()
#     run(root)
# else:
#     os._exit(-1)


root.deiconify()
run(root)