# Enter your code here. Read input from STDIN. Print output to STDOUT


for i in range(int(input())):
    try:
        x, y = map(int, input().split())
        print(x//y)
    except BaseException as e:
        print("Error Code:", e)
