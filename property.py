
class C:
    def __init__(self):
        self.x = 'X-man'

c = C()
print(c.x)
print(getattr(c, 'x','没有这个属性'))
print(getattr(c, 'y', '没有这个属性'))



class Pro:
    def __init__(self, size=10):
        self.__size = size

    def getSize(self):
        return self.__size

    def setSize(self, value):
        self.__size = value

    def delSize(self):
        del self.__size

    x = property(getSize, setSize, delSize)

p1 = Pro()
p1.x = 20

print(p1.x)
print(p1.getSize())

print(p1.__dict__)
print(Pro.__dict__)

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == 'square':
            self.width = value
            self.height = value
        else:
            #self.key = value #会产生无限递归
            #super().__setattr__(key, value) #推荐使用基类的方法
            self.__dict__[key] = value #运用__dict__属性进行赋值

    def getArea(self):
        return self.width * self.height

re = Rectangle(4, 5)
print(re.getArea())
print(re.__dict__)

#描述符

class MyDescriptor:
    def __get__(self, instance, owner):
        print("geting ...", self, instance, owner)

    def __set__(self, instance, value):
        print("setting ... ", self, instance, value)

    def __delete__(self, instance):
        print("delete ...", self, instance)

class Test:
    x = MyDescriptor()

test = Test()
print(test.x)
test.x = 20

#
class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, owner):
        return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __delete__(self, instance):
        self.fdel(instance)

class Tproperty:
    def __init__(self):
        self._x = None

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def delX(self):
        del self._x
    x = MyProperty(getX, setX, delX)

c = Tproperty()
c.x = "x-man"
print(c.getX())

#用两个描述符类表述温度转化

class Celsius:
    def __init__(self, value=26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Fahreheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (float(value)-32)/ 1.8

class Temprature:
    cel = Celsius()
    fah = Fahreheit()

temp = Temprature()
print(temp.cel)
temp.cel = 30
print(temp.fah)

temp.fah = 100
print(temp.cel)
