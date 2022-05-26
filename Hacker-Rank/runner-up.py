
def solve (arr):
    set1=set(arr)
    print("set : ",set1)
    arr=list(set1)
    print("arr : ",arr)
    return arr[-2]
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))
