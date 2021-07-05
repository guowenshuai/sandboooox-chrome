import tkinter as tk
from tkinter import messagebox

from .createLnkDialog import ChromeDialog
from .userDialog import UserDialog
from .priceDialog import PriceDialog
from .settingsDialog import SettingsDialog
from util import LocalConfig, Connector
from .coinlist import loadLocalAccounts, saveLocalAccount, exportLocalAccount, importLocalAccount
from .editEmailDialog import EditEmailDialog

def Menu(root):
    #　创建一个菜单栏，这里我们可以把它理解成一个容器，在窗口的上方
    menubar = tk.Menu(root)
    coinlistmenu = tk.Menu(menubar, tearoff=0)  # tearoff意为下拉
    menubar.add_cascade(label='coinlist', menu=coinlistmenu)
   
    # 分隔线
    coinlistmenu.add_command(label='导入邮箱', command=importEmail)
    coinlistmenu.add_separator()

    submenu = tk.Menu(coinlistmenu) 
    coinlistmenu.add_cascade(label='本地', menu=submenu)
    submenu.add_command(label='新建', command=lambda: createLnk(root))
    submenu.add_command(label='导出到剪贴板', command=exportClipboard)
    submenu.add_command(label='从剪贴板导入', command=importClipboard)

    # 创建编辑菜单
    privatemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='我的', menu=privatemenu)
    privatemenu.add_command(label='信息', command=lambda: showUserDialog(root))
    privatemenu.add_separator()
    privatemenu.add_command(label='设置', command=lambda: showSettingsDialog(root))
    
    aboutmenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='关于', menu=aboutmenu)
    aboutmenu.add_command(label='团队', command=lambda: aboutTeam(root))
    aboutmenu.add_separator()
    aboutmenu.add_command(label='价格', command=lambda: showPriceDialog(root))
    
    root.config(menu=menubar)
    

def do_job():
    print("menu job")
    
from tkinter.filedialog import askopenfilename
import os, json, re
def importEmail():
    filepath = askopenfilename(title='选择账号文件导入', 
                  initialdir='~', filetypes=[('coinlist账号列表','*.txt')])
    if len(filepath) == 0:
        return
    if not os.path.exists(filepath):
        return
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    
    config = LocalConfig().config
    existsEmails = set(json.loads(config.get('coinlist', 'email', fallback="[]")))
    with open(filepath, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if EMAIL_REGEX.match(line):
                existsEmails.add(line)
    config['coinlist']['email'] = json.dumps(list(existsEmails))
    LocalConfig().save(config)

def exportClipboard():
    line = exportLocalAccount()
    r = tk.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(line)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()

def importClipboard():
    r = tk.Tk()
    r.withdraw()
    line = r.clipboard_get()
    r.update()
    r.destroy()
    if importLocalAccount(line.strip()):
        tk.messagebox.showinfo("导入成功", "导入成功")
    else:
        tk.messagebox.showinfo("导入失败", "从剪贴板导入失败,数据格式错误")
        
def editEmail(root):
    dia = EditEmailDialog(root)
    root.wait_window(dia)

def createLnk(root):
    inputDialog = ChromeDialog(root)
    root.wait_window(inputDialog) # 这一句很重要！！！
    # TODO 提交并保存
    if not inputDialog.info:
        return
    print(inputDialog.info)
    if inputDialog.info['email'] != "":
        print("todo save")
        saveLocalAccount(inputDialog.info)
        Connector().send("addAccount", data=[inputDialog.info])

    return inputDialog.info

def aboutTeam(root):
    msg = '''  心之所向,身之所往

    coinlist账号
    coinlist工具
    币安公告订阅
    全方位的服务
    '''
    tk.messagebox.showinfo("关于团队", msg)


def showUserDialog(root):
    userDialog = UserDialog(root)
    root.wait_window(userDialog)

def showPriceDialog(root):
    priceDialog = PriceDialog(root)
    root.wait_window(priceDialog)

def showSettingsDialog(root):
    settingsDialog = SettingsDialog(root)
    root.wait_window(settingsDialog)