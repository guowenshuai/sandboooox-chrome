# Python program to create a table

import tkinter as tk
from tkinter import ttk
from app import Tables, DeleteDialog
# https://tk-tutorial.readthedocs.io/en/latest/tree/tree.html


count = 0
def addrow(tree):
    global count
    count += 1
    tree.insert("", "end", text="text_file.txt %s" % count, values=("23-Jun-17 11:25","TXT file","1 KB"))

def tree_click_handler(event):
    cur_item = tree.item(tree.focus())
    col = tree.identify_column(event.x)
    values = []
    values.append(cur_item['text'])
    values.extend(cur_item['values'])
    colIndex = col[1:]
    root.clipboard_clear()
    root.clipboard_append(values[int(colIndex)])

root = tk.Tk()

tree=ttk.Treeview(root)

tree["columns"]=("one","two","three")
tree.column("#0", width=270, minwidth=270)
tree.column("one", width=150, minwidth=150, stretch=tk.NO)
tree.column("two", width=400, minwidth=200, stretch=tk.NO)
tree.column("three", width=80, minwidth=50, stretch=tk.NO)

tree.heading("#0",text="Name",anchor=tk.W)
tree.heading("one", text="Date modified",anchor=tk.W)
tree.heading("two", text="Type",anchor=tk.W)
tree.heading("three", text="Size",anchor=tk.W)


# Level 1
folder1=tree.insert("", "0", text="Folder 1", values=("23-Jun-17 11:05","File folder",""))
tree.insert("", 2, text="text_file.txt", values=("23-Jun-17 11:25","TXT file","1 KB"))
tree.insert("", 2, text="text_file.txt", values=("23-Jun-17 11:25","TXT file","2 KB"))
# Level 2
tree.insert(folder1, "end", text="photo1.png", values=("23-Jun-17 11:28","PNG file","2.6 KB"))

tree.bind('<ButtonRelease-1>', tree_click_handler)

vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
# vsb.pack(side=tk.RIGHT, fill=tk.Y, expand=1)
# tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
tree.configure(yscrollcommand=vsb.set)


l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Button(text="add row", command=lambda: addrow(tree))
# l1.pack(side=tk.LEFT)
# l2.pack(side=tk.LEFT)
def printLine(root, line):
    def fun():
        print(line)
    return fun

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
    deleteDia = DeleteDialog(root, line)
    root.wait_window(deleteDia)
    if deleteDia.success:
        return True

def editRow(line, changed):
    print(line)
    print(changed)

table = Tables(root, columns=[
    {
        "index": "name",
        "weight": 1,
        "title": "姓名"
    },     {
        "index": "age",
        "weight": 1,
        "title": "年龄",
        "editable": True,
    },     {
        "index": "addr",
        "weight": 2,
        "title": "住址",
        "editable": True,
    },
], dataSource=[
    {
        "name": "bob",
        "age": 28,
        "addr": "beijing"
    },  {
        "name": "saum",
        "age": 22,
        "addr": "suzhou"
    },  {
        "name": "elice",
        "age": 21,
        "addr": "shanghai"
    },
], actions=[
    {
        "text": "打印",
        "command": printLine,
    }, 
            {
        "text": "复制",
        "command": copyLine,
    },

], deleteFunc=deleteRow, editFunc=editRow)

def addrows(table):
    table.add_data([{
        "name": "bob",
        "age": 28,
        "addr": "beijing"
    },  {
        "name": "saum",
        "age": 22,
        "addr": "suzhou"
    },])
l2 = ttk.Button(text="add data", command=lambda: addrows(table))
l2.pack(side=tk.RIGHT)
l3 = ttk.Button(text="clear data", command=lambda: table.clear())
l3.pack(side=tk.RIGHT)
table.pack(side=tk.RIGHT)


root.mainloop()


