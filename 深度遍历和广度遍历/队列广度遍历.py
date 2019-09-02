
import os

from collections import deque

path=r"C:\Users\ehuamay\Desktop\pm_report_tags"
queue=deque([])

queue.append(path)
while len(queue) != 0:
    path=queue.popleft()#取出拉出的值
    filelist=os.listdir(path)#遍历路径
    for filename in filelist:
        filepath=os.path.join(path, filename)

        if os.path.isdir(filepath):
            print("文件夹",filename)
            queue.append(filepath)
        else:
            print("文件", filename)
