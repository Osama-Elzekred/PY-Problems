def cube(x): return x**3


def fibonacci(n):
    d = {}
    d[0] = 0
    d[1] = 1
    l = []
    if n == 0:
        return []
    if n == 1:
        return [0]
    n -= 1

    def solve(n):
        if d.get(n, False) or n == 0:
            return d[n]
        d[n] = solve(n-1)+solve(n-2)
        return d[n]

    solve(n)
    return(list(d.values()))


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
