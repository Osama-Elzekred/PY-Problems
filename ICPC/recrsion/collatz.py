def solve():
    d = {}
    l = []
    l[0] = int(input())

    def f(n):
        if l[n] not in d:
