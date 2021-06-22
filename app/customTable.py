import tkinter as tk

'''
columns = [
    {
        "index": "name",
        "weight": 1,
        "title": "名称"

    }
]

actions = [
    {
        "text": "操作",
        "command": runcmd,
    }
]

dataSource = [
    {
        "name": "bob",
        "age": 28,
    }
]

'''

class Tables(tk.Frame):
    def __init__(self, master, columns, dataSource=None, actions=None, deleteFunc=None, editFunc=None):
        super().__init__(master)
        self.__master = master
        self.pack()
        self.__columns = columns
        self.__dataSource = dataSource
        self.__actions = actions
        self.__deleteFunc = deleteFunc
        self.__editFunc = editFunc
        self.__row_list = []
        self.baseWidth = 12

        self.create_widgets()

    def create_widgets(self):
        # 创建表格表头和内容
        row_header = tk.Frame(self.__master)
        for v in self.__columns:
            header_text = v['title']
            tk.Label(row_header, text=header_text, anchor="w", width=int(self.baseWidth*v['weight']),).pack(side=tk.LEFT, padx=1, pady=1)
        if self.__actions:
            tk.Label(row_header, text="操作", anchor="w", width=self.baseWidth).pack(side=tk.LEFT, expand=1, fill=tk.X, padx=1, pady=1)
        row_header.pack(side=tk.TOP,  anchor="w",  expand=1, fill=tk.X)
        # 创建行数据
        for dat in self.__dataSource:
            row = Rows(self.__master, self.__columns, dat, self.__actions, self.__deleteFunc, self.__editFunc)
            # row.pack(side=tk.TOP,  anchor="w")
            self.__row_list.append(row)

    # 表格中追加数据
    def add_data(self, data):
        for dat in data:
            row = Rows(self.__master, self.__columns, dat, self.__actions, self.__deleteFunc, self.__editFunc)
            # row.pack(side=tk.TOP,  anchor="w")
            self.__row_list.append(row)
        self.__dataSource.extend(data)
    
    def clear(self):
        for r in self.__row_list:
            r.destory()
        self.__row_list = []

# 行数据
class Rows(tk.Frame):
    def __init__(self, master, columns, rowData, actions=None, deleteFunc=None, editFunc=None):
        self.master = tk.Frame(master)
        super().__init__(master=self.master)
        self.master.pack(side=tk.TOP,  anchor="w")
        # self.master = master
        self.columns = columns
        self.rowData = rowData
        self.actions = actions
        self.deleteFunc = deleteFunc
        self.editFunc = editFunc
        self.rowDetail = {} # 行数据详情
        self.baseWidth = 12

        self.create_row()
        self.create_actions()
        self.edit_actions()
        self.remove_actions()
    # 创建行内容
    def create_row(self):
        for v in self.columns:
            cell_text = ""
            if v['index'] in self.rowData:
                cell_text = self.rowData[v['index']]
                self.rowDetail[v['index']] = {
                    "var": tk.StringVar(value=cell_text),
                    "text": cell_text
                }
            ent = self.cellLabel(v['index'], v['weight'])
            ent.pack(side=tk.LEFT, padx=1, pady=1)

    # 表格按钮
    def create_actions(self):
        if not self.actions:
            return
        for v in self.actions:
            action_text = v['text']
            tk.Button(self.master, text=action_text, command=v['command'](self.master, self.rowData)).pack(side=tk.LEFT)
    
    def edit_actions(self):
        def default_edit():
            editRow = EditRow(self.master, self.columns, self.rowData, self.rowDetail, self.editFunc)
            self.master.wait_window(editRow)
        action_text = "编辑"
        tk.Button(self.master, text=action_text, command=lambda: default_edit()).pack(side=tk.LEFT)
       
    def remove_actions(self):
        def default_remove():
            if self.deleteFunc:
                if not self.deleteFunc(self.master, self.rowData):
                    return
            self.master.destroy()
        action_text = "删除"
        tk.Button(self.master, text=action_text, command=lambda: default_remove()).pack(side=tk.LEFT)
        
    def cellLabel(self, index, weight=1):
        ent = tk.Entry(self.master, state='readonly', readonlybackground='white', fg='black',  width=int(self.baseWidth*weight))
        ent.config(textvariable=self.rowDetail[index]['var'], relief='flat')
        return ent    

    def destory(self):
        self.master.destroy()

class EditRow(tk.Toplevel):
    def __init__(self, root, columns, rowData, rowDetail, editFunc=None):
        super().__init__()
        self.title('编辑')
        self.attributes("-topmost", True)
        self.resizable(False, False)
        self.columns = columns
        self.rowData = rowData
        self.rowDetail = rowDetail
        self.editFunc = editFunc
        self.success = False

        # 弹窗界面
        self.setup_UI()

        # x = root.winfo_x()
        # y = root.winfo_y()
        # w = root.winfo_width()
        # h = root.winfo_height()  
        # self.geometry("+%d+%d" % (x + w/3, y + h/3))     

    def setup_UI(self):
        for v in self.columns:
            if "editable" in v and v['editable']:
                row = tk.Frame(self)
                row.pack(fill="x")
                tk.Label(row, text="%s:" % v['title'], width=15, anchor="w").pack(side=tk.LEFT)
                tk.Entry(row, textvariable=self.rowDetail[v['index']]["var"], width=20).pack(side=tk.LEFT)

        row_sub = tk.Frame(self)
        row_sub.pack(fill="x")
        tk.Button(row_sub, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row_sub, text="保存", command=self.ok).pack(side=tk.RIGHT)
        
    def ok(self):
        changed = {}
        for v in self.columns:
            if "editable" in v and v['editable']:
                val = self.rowDetail[v['index']]["var"].get()
                if val != self.rowDetail[v['index']]["text"]:
                    changed[v['index']] = val
                    self.rowDetail[v['index']]["text"] = val
        self.success = True
        if self.editFunc:
            self.editFunc(self.rowData, changed)
        self.destroy() 
    def cancel(self):
        for v in self.columns:
            if "editable" in v and v['editable']:
                self.rowDetail[v['index']]["var"].set(self.rowDetail[v['index']]["text"])
        self.success = False
        self.destroy()
