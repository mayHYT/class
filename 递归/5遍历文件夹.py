
'''
import os

filelist=os.listdir(r"C:\\Users\\ehuamay\\Desktop\\pm_report_tags")
#print(filelist)
for file in filelist:
    if os.path.isdir("C:\\Users\\ehuamay\\Desktop\\pm_report_tags\\"+file):
        print("文件夹", file)
    else:
        print("文件", file)


'''

import os

def getall(path):
    filelist=os.listdir(path)
    for filename in filelist:
        filepath=os.path.join(path, filename)
        if os.path.isdir(filepath):
            print("文件夹", filename)
            getall(filepath)
        else:
            print("文件", filename)

getall(r"C:\Users\ehuamay\Desktop\pm_report_tags")