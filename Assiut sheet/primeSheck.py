

def solve():
    num = int(input())
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return "NO"
    return "YES"


print(solve())
