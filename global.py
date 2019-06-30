'''全局变量'''

X = 11

def g1():
    print(X)

def g2():
    global X
    X = 22

def h1():
    X = 33
    def nested():
        print(X)
def h2():
    X = 33
    def nested():
        nonlocal X
        X = 44

print(X, id(X))
g2()
print(X, id(X))

h1()
h2()
print(X, id(X))