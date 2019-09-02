
def go(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return go(num-1) + go(num-2)

print(go(5))