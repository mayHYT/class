from personClass import Person

class Manager(Person):
    '''继承Person类'''
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    #不好的扩展方法
#    def giveRaise(self, percent, bonus = 0):
#        self.pay = int(self.pay * (1 + percent + bonus))

    # 好的扩展方法
    def giveRaise(self, percent, bonus = 0.10):
        Person.giveRaise(self, percent + bonus)
    def delegate(self):
        self.action()

if __name__ == '__main__':

    bob = Person('Bob Smith')
    sun = Person('sune jose', job = 'dev', pay=7890)
    print(bob)
    print(sun)
    sun.giveRaise(0.7)
    print(sun)
    tom = Manager('Tome jose', 9000)
    tom.giveRaise(0.9)
    #tom.delegate() #
    print(tom)

    print('------All three -------')

    for object in (bob, sun, tom):
        object.giveRaise(0.5)
        print(object)


