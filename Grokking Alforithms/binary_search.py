def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low+high) // 2
        guess = list[mid]
        if(guess == item):
            return mid
        if(guess > item):
            high = mid-1
        else:
            low = mid+1
    return None


# def binary_search(list, item):
#     low = 0
#     high = len(list)-1
#     mid = (low+high) // 2
#     guess = list[mid]
#     if guess == item:
#         return mid
#     elif guess < item:
#         return binary_search(list[mid-1:], item)
#     elif guess > item:
#         return binary_search(list[:mid-1], item)
#     else:
#         return None

if __name__ == "__main__":
    l = [2, 4, 5, 7, 15, 22, 26, 29, 31, 32, 35, 37, 40, 49, 55]
    n = 5

    l2 = [*range(128)]
    n2 = 45

    print(binary_search(l, n))
    print(binary_search(l2, n2))
