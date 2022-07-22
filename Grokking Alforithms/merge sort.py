def merge_sort(arr, key, descending):
    if len(arr) < 2:
        return
    mid = len(arr) // 2
    leftArr = arr[:mid]
    rightArr = arr[mid:]
    merge_sort(leftArr, key, descending)
    merge_sort(rightArr, key, descending)

    return merge_sorted2Arr(leftArr, rightArr, arr, key, descending)


def merge_sorted2Arr(a, b, arr, key, descending):
    lenA = len(a)
    lenB = len(b)
    i = j = k = 0
    while i < lenA and j < lenB:
        if descending:
            if a[i][key] > b[j][key]:
                arr[k] = a[i]
                i += 1
            else:            # elif a[i] > b[j]
                arr[k] = b[j]
                j += 1
            k += 1
        else:
            if a[i][key] < b[j][key]:
                arr[k] = a[i]
                i += 1
            else:            # elif a[i] > b[j]
                arr[k] = b[j]
                j += 1
            k += 1
    while i < lenA:
        arr[k] = a[i]
        i, k = i+1, k+1
    while j < lenB:
        arr[k] = b[j]
        j, k = j+1, k+1


# arr = [None]*6
# merge_sorted2Arr([2, 5, 7], [3, 6, 10], arr)
# print(arr)
arr2 = [5, 6, 11, 2, 5, 4, 55, 68, 45]
elements = [
    {'name': 'vedanth',   'age': 17, 'time_hours': 1},
    {'name': 'rajab', 'age': 12,  'time_hours': 3},
    {'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
    {'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
]
print(elements)

# def merge_sorted2Arr(a, b, arr):
#     lenA = len(a)
#     lenB = len(b)
#     i = j = k = 0
#     while i < lenA and j < lenB:
#         if a[i] < b[j]:
#             arr[k] = a[i]
#             i += 1
#         else:            # elif a[i] > b[j]
#             arr[k] = b[j]
#             j += 1
#         k += 1
#     while i < lenA:
#         arr[k] = a[i]
#         i, k = i+1, k+1
#     while j < lenB:
#         arr[k] = b[j]
#         j, k = j+1, k+1

merge_sort(elements, key='time_hours', descending=True)
