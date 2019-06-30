

class Person:
    ''' Person 类'''
    #编写构造函数
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    #编写方法
    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int( self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s , %s]' %(self.name, self.pay)

if __name__ == '__main__':

    bob = Person('Bob summin')
    sun = Person('sun huang', pay = 5000, job= 'teacher')
    #print(Person)
    print(bob.name, bob.job, bob.pay)
    print(sun.name, sun.job,sun.pay)

    #sun.pay *= 1.10
    #print(sun.pay)

    #print(bob.name.split()[-1])
    print(bob.lastName(), sun.lastName())
    #sun.giveRaise(1.9)
    print(sun.giveRaise(1.9))
    print(sun.pay)

    print(sun)#触发运算符重载 __str__
