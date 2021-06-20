import tkinter as tk
from tkinter import messagebox

from .createLnkDialog import ChromeDialog
from .userDialog import UserDialog
from util import LocalConfig

def Menu(root):
    #　创建一个菜单栏，这里我们可以把它理解成一个容器，在窗口的上方
    menubar = tk.Menu(root)
    #　定义一个空的菜单单元
    coinlistmenu = tk.Menu(menubar, tearoff=0)  # tearoff意为下拉
    #　将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
    menubar.add_cascade(label='coinlist', menu=coinlistmenu)
    #　在`文件`中加入`新建`的小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
    #　如果点击这些单元, 就会触发`do_job`的功能
    coinlistmenu.add_command(label='新建', command=lambda: createLnk(root))
    # coinlistmenu.add_command(label='打开', command=do_job)
    # coinlistmenu.add_command(label='保存', command=do_job)
    # 分隔线
    coinlistmenu.add_separator()
    coinlistmenu.add_command(label='导入', command=importEmail)
    # coinlistmenu.add_command(label='导出', command=do_job)

    # 创建编辑菜单
    privatemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='我的', menu=privatemenu)
    privatemenu.add_command(label='信息', command=do_job)
    privatemenu.add_separator()
    privatemenu.add_command(label='设置', command=do_job)
    
    # 在‘文件’下拉菜单中创建二级菜单
    # submenu = tk.Menu(coinlistmenu) 
    # coinlistmenu.add_cascade(label='导入', menu=submenu, underline=0)
    # submenu.add_command(label='导入图片', command=do_job)

    aboutmenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='关于', menu=aboutmenu)
    aboutmenu.add_command(label='团队', command=lambda: aboutTeam(root))
    aboutmenu.add_separator()
    aboutmenu.add_command(label='价格', command=do_job)
    
    root.config(menu=menubar)
    

def do_job():
    print("menu job")
    
from tkinter.filedialog import askopenfilename
import os, json
def importEmail():
    filepath = askopenfilename(title='选择账号文件导入', 
                  initialdir='~', filetypes=[('coinlist账号列表','*.txt')])    
    if not os.path.exists(filepath):
        return
    
    config = LocalConfig().config
    existsEmails = set(json.loads(config.get('coinlist', 'email', fallback="[]")))
    with open(filepath, 'r') as f:
        for line in f.readlines():
            existsEmails.add(line.strip())
    config['coinlist']['email'] = json.dumps(list(existsEmails))
    LocalConfig().save(config)

def createLnk(root):
    inputDialog = ChromeDialog(root)
    root.wait_window(inputDialog) # 这一句很重要！！！
    # TODO 提交并保存
    print(inputDialog.info)
    return inputDialog.info


def aboutTeam(root):
    print(LocalConfig().config.sections())
    msg = '''  心之所向,身之所往

    coinlist账号
    coinlist工具
    币安公告订阅
    全方位的服务
    '''
    tk.messagebox.showinfo("关于团队", msg)