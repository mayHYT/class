

def go(num):
    if num == 0:
        return
    else:
        print("hello world head", num-1)
        go(num-1)
        print("hello world foot", num-1)

go(5)