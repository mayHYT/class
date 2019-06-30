

def uperName(self):
    return self.name.upper()

class rec:
    pass

rec.name = "bob"
rec.age = 70
rec.method = uperName


x = rec()
y = rec()
y.name = "lili"
y.job = 'develop'

print(x.name, x.age)
print(y.name, y.age)
print(y.job)
#print(x.job) #x没有job属性

print(rec.__dict__.keys())

print(x.__dict__.keys())
print(y.__dict__.keys())

print(x.method())
print(y.method())