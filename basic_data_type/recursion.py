'''递归'''
def counter(data):
    print(data)
    if (data == 0):
        return
    else:
        counter(data - 1)

counter(10)
