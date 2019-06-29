
class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()

#x.setdata(2.34)
#y.setdata(7.99)

x.data = "hello world"
y.data = 90

x.age = 18 #实例产生一个新的属性

y.display()
x.display()

x.setdata(x.age) #实例对象x的任何类方法都可以使用它。也可以不使用它
x.display()
