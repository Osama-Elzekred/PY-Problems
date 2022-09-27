# def solve():
#     n = int(input())
#     x = []

#     def rec(x):

#         if x:
#             if len(x) > 10:
#                 return float("inf")
#             nm = "".join(x)

#             if int(nm) >= n and x.count('4') == x.count('7'):
#                 return int("".join(x))

#         v = min(rec(x+['7']), rec(x+['4']))
#         return v

#     return rec(x)


# print(solve())

# def solve():
#     n = int(input())
#     x = []
#     count =1
#     def rec(x):

#        if x <=0 : return count
#        if  any(num not in ('4','7') for num in x) : return
#        return v

#     return rec(x)


# print(solve())


def solve():
    n = int(input())
    x = []
    count = [0]

    def rec(x):

        if x:
            if int("".join(x)) > n:
                return x
            count[0] += 1

        rec(x+['7'])
        rec(x+['4'])
        return x
    rec([])
    return count[0]


print(solve())
