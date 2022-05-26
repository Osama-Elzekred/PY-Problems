import calendar
l = list(map(int, input().split()))
print(list(calendar.day_name)[calendar.weekday(l[2], l[0], l[1])].upper())
