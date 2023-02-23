def sumOdd(n):
    terms = (n + 1)//2
    sum1 = terms * terms
    return sum1


x, y = sorted(list(map(int, input().split())))
x -= 1
print((y*(y+1))//2-(x*(x+1))//2)
a = x
b = y
x //= 2
y //= 2
print((y*(y+1))-(x*(x+1)))
print(sumOdd(b)-sumOdd(a))
