import math as m
# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
y = int(input())
precent = chr(176)
mc = m.hypot(x, y)/2
degree = round(m.degrees(m.asin(mc/y)))
print(degree, precent, sep='')
