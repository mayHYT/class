
for name in ['lili','may','bob']:
    print(name)
    if(name == "may"):
        print("my name is may")
        break
    else:
        print("I don't know who is she?")
else:
    print("1")
    print("2")

def print_hello(name, sex):
    sex_dic = {1:u'先生', 2:"女士"}
    print("hello %s %s, welcome to python world!" % (name, sex_dic.get(sex, u'先生')))

print_hello('tanggu', sex = 1)

def kw_dict(**kwargs):
    return kwargs;

print(kw_dict(a=1,b=2,c=3) == {'a':1,'b':2,'c':3})

def foo(x,  *args, y=1):
    '''
    This is foo function
    '''
    print(x)
    print(y)
    print(args)

foo(1,2,3,4,5,6,y=100,)
print(foo.__doc__)

d = {'x':1,'y':2,'z':3}
for key in d:
    print(key, 'corresponds to', d[key])

print('#'*10)

for key,val in d.items():
    print(key,'corresponds to', val)

l="3,2,1,4,6,3,2]"

help(list)
