

# def binary_search(list, item):
#     low = 0
#     high = len(list)-1
#     mid = (low+high) // 2
#     guess = list[mid]
#     if guess == item:
#         return mid
#     elif guess < item:
#         return binary_search(list[:mid-1], item)
#     elif guess > item:
#         return binary_search(list[mid-1:], item)
