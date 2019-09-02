import os
path="C:\\Users\\ehuamay\\Desktop\\pm_report_tags"

mystack=[]
mystack.append(path)

while len(mystack) != 0:
    path = mystack.pop()
    filelist=os.listdir(path) #遍历路径
    for filename in filelist:
        filepath=os.path.join(path,filename)
        if os.path.isdir(filepath):
            print("文件夹", filename)
            mystack.append(filepath)
        else:
            print("文件", filename)