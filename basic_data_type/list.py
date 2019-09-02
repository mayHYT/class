
'''选择排序'''
def findSmallest(arr):
    smallest = arr[0]
    smallindex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallindex = i
    return smallindex


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        print(smallest)
        newArr.append(arr.pop(smallest))
        print(arr)
        print(newArr)
    return newArr


print(selectionSort([9, 10,5,8,2,7,0]))
