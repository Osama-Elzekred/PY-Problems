import random


def qsort(arr):
    if len(arr) < 2:
        return arr
    mid = (len(arr)-1)//2
    povit_val = arr[mid]
    flag = True
    leftArr = []
    rightArr = []
    povit_list = []
    for item in arr:
        if item == povit_val and flag:
            flag = False
            continue
        elif item == povit_val and not flag:
            povit_list.append(item)
        elif item < povit_val:
            leftArr.append(item)
        else:
            rightArr.append(item)

    povit_list = [arr[mid]] + povit_list
    return qsort(leftArr) + povit_list + qsort(rightArr)


l = []
for i in range(4):
    l.append(random.randint(-150, 150))
print(qsort(l))
