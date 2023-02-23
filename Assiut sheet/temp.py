
s = input()

index = 0
hello = "hello"
for i in range(len(s)):
    if s[i] == hello[index]:
        if index == 4:
            break
        index += 1
if index == len(hello)-1:
    print("YES")
else:
    print("NO")
