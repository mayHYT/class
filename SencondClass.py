from FirstClass import FirstClass

class SecondClass(FirstClass):
    def display(self):
        print("current value = '%s' " % self.data)

z = SecondClass()
z.setdata("haha")
z.display()
