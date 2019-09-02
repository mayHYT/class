
class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x

'''组合类'''
class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("there have %d tutle and %d fish" %(self.turtle.num, self.fish.num))


class CC:
    def setXY(self, x, y):
        self.x = x
        self.y = y
    def printXY(self):
        print(self.x, self.y)

pool = Pool(1, 10)
pool.print_num()

'''__new__使用'''

class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)

a = CapStr("I love China!")
print(a)

# __def__(self) 方法
class C:
    def __init__(self):
        print("This is class init interface...")
    def __del__(self):
        print("Delete this valuable...")

#逐行读取文件
for line in open('test.py'):
    print(line.upper(), end='')
