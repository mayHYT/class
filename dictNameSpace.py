'''命名空间字典'''

class super:
    def hello(self):
        self.data1 = 'spam'


class sub(super):
    def hola(self):
        self.data2 = 'eggs'

X = sub()
print(X.__dict__)
print(X.__class__)
print(sub.__bases__)
print(super.__bases__)

Y = sub()

X.hello()
print(X.__dict__)
X.hola()
print(X.__dict__)

print(sub.__dict__.keys())
print(super.__dict__.keys())

print(X.data1, X.__dict__['data1'])
X.data3 = 'issue'
print(X.__dict__)
print(Y.__dict__)

print(dir(X))

list1 = [{111:"rule1"}, {222: "rule2"}]
dic = {111:"rule1",122:"rule2"}
for var, rule in dic.items():
    print(var, rule)
