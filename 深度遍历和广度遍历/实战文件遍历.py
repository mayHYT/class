import tkinter
import tkinter.ttk
import os

class TreeWindows:
    def __init__(self):
        self.win = tkinter.Tk()
        self.tree = tkinter.ttk.Treeview(self.win)
        self.tree.pack()
        self.ysb = tkinter.ttk.Scrollbar(self.win, orient="vertical", command=self.tree.yview())#y 滚动条
        self.xsb = tkinter.ttk.Scrollbar(self.win, orient="horizontal", command=self.tree.xview())
        self.tree.config(yscroll=self.ysb.set,xscroll=self.xsb.set)
        self.tree.grid(row=0,column=0)
        self.tree.heading("#0",text="path", anchor="w")#初始化头部


        filepath="C:\\Users\\ehuamay\\Desktop\\pm_report_tags"
        root=self.tree.insert("","end",text=filepath,open=True)#插入一个节点
        self.loadtree(root, filepath)

        #选择的情况绑定他
        self.tree.bind("<<TreeviewSelect>>", self.gosel)
        self.e=tkinter.StringVar()
        self.entry=tkinter.Entry(self.win,textvariable=self.e)
        self.e.set("请选择文件")
        self.entry.grid(row=0, column=2)

        self.ysb.grid(row=0, column=1, sticky="ns")
        self.xsb.grid(row=1, column=0, sticky="ew")
        self.win.grid()

    def show(self):
        self.win.mainloop()


    def gosel(self, event):
        self.select=event.widget.selection()
        for idx in self.select:
            print(self.tree.item(idx)["text"])
            self.e.set(self.tree.item(idx)["text"])



    def loadtree(self, parent, rootpath):
        for path in os.listdir(rootpath): #遍历当前目录
            abspath=os.path.join(rootpath, path)
            oid = self.tree.insert(parent, 'end', text=path, open=False)#插入树枝
            if os.path.isdir(abspath):
                print("文件夹", abspath)
                self.loadtree(oid,abspath)
            else:
                print("文件", abspath)
mytree=TreeWindows()
mytree.show()