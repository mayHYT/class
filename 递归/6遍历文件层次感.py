
import os

def getall(path, treeshow):
    treeshow += "   "
    filelist=os.listdir(path)
    for filename in filelist:
        filepath=os.path.join(path, filename)
        if os.path.isdir(filepath):
            print(treeshow, "文件夹", filename)
            getall(filepath, treeshow)
        else:
            print(treeshow, "文件", filename)

getall(r"C:\Users\ehuamay\Desktop\pm_report_tags", "")