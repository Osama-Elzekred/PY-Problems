t = int(input())
for i in range(t):
    n = int(input())
    base = n//3
    if n == 7:
        print("2 4 1")
    elif n == 8:
        print("3 4 1")
    elif n % 3 == 2:
        print(f"{base+1} {base+2} {base-1}")
    elif n % 3 == 1:
        print(f"{base+1} {base+2} {base-2}")
    elif n % 3 == 0:
        print(f"{base} {base+1} {base-1}")
