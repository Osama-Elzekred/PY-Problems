def solve():

    for _ in range(int(input())):
        n = int(input())
        st1 = input()
        st2 = input()
        flag = 0
        for i in range(n):
            if st1[i] != st2[i]:
                if not (st1[i] in ('B', 'G')) or not (st2[i] in ('B', 'G')):
                    print("NO")
                    flag = 1
                    break
        if not flag:
            print("Yes")


solve()

# for _ in range(int(input())):
#     n = int(input())
#     st1 = input()
#     st2 = input()
#     copy = ""
#     for let in st1:
#         if let == 'G':
#             copy += 'B'
#         elif let == 'B':
#             copy += 'G'
#         else:
#             copy += let
#     print(st1, st2, copy)
#     if st2 == st1 or st2 == copy:
#         print("Yes")
#     else:
#         print("No")
