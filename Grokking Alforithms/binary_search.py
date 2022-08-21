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


def Upper_bound(list, item):

    l, r = 0, len(list)-1
    ans = -1
    while l <= r:
        mid = (l+r)//2
        if list[mid] > item:
            ans = mid
            r = mid-1
        elif list[mid] <= item:
            l = mid+1
    return ans


if __name__ == "__main__":
    l = [2, 4, 5, 7, 15, 22, 26, 29, 31, 32, 35, 37, 40, 49, 55]
    n = 5

    l2 = [*range(128)]
    n2 = 45
    print(l2)

    # print(binary_search(l, n))
    print(Upper_bound(l2, n2))
