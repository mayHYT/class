def go(num):
    if num == 0:
        return 0
    else:
        return num + go(num-1)

print(go(5))