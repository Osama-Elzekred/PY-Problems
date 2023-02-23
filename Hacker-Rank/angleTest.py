import math as m
# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
y = int(input())

mc = (abs(pow(x, 2)+pow(y, 2)))/2
degree = m.asin(m.degrees(mc//y))
