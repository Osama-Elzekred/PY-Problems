# def bits(n):
#     while n:
#         b = n & (~n+1)
#         yield b
#         n ^= b


# for b in bits(109):
#     print(b)

n = int(input())
for i in bin(n):
    print(i, end="")
print()
# for i in bin(1000000000000):
#     print(i, end="")
print(int(bin(n), 2))

# cnt = 1
# flag = 0
# for i, v in enumerate(bin(109)[:1:-1]) :
#     if cnt <= 2:
#         cnt += 1
#         continue
#     if i != 1:
#         print("NO")
#         flag ^= 1
#         break
# if not flag:
#     print("yes")
# for i, v in enumerate(bin(109)[:1:-1]):
#     if v==1:
# print(sum(map(int, bin(n)[:1:-1])))
if sum(map(int, bin(n)[:1:-1])) == 1:
    print("yes")
else:
    print("NO")
