import os
path="C:\\Users\\ehuamay\\Desktop\\pm_report_tags"

mystack=[]
mystack.append([path,0])

while len(mystack) != 0:
    pathlist = mystack.pop()
    filelist=os.listdir(pathlist[0]) #遍历路径
    num=pathlist[1]#代表层次
    headstr=""
    for i in range(num): #控制层次感
        headstr += "    "

    for filename in filelist:
        filepath=os.path.join(pathlist[0],filename)
        if os.path.isdir(filepath):
            print(headstr, "文件夹", filename)
            mystack.append([filepath, num+1])
        else:
            print(headstr, "文件", filename)