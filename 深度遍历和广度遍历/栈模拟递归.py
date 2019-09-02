
'''
def add(num):
    if num == 0:
        return 0
    else:
        return num + add(num-1)

print(add(5))

'''

mystack=[]
lastnum=0
mystack.append(5)

while len(mystack) != 0:
    data=mystack.pop()
    print(data)
    lastnum += data
    if data == 0:
        break;
    else:
        mystack.append(data-1)

print(lastnum)