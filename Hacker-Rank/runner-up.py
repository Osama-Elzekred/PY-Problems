
def solve(arr):
    set1 = set(arr)
    print("set : ", set1)
    arr = list(set1)
    print("arr : ", arr)
    return arr[-2]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))

    l = [1, 2, 1, 3, 4, 1]
    print(l.index(1, 3))
