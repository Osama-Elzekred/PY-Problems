from collections import OrderedDict
from nis import match
import random
import dis
dis.dis("s+5/54")

d = OrderedDict()

for i in range(8, 0, -1):
    d[i] = random.randint(0, 98)
# print(list(reversed(d)))
# print(list(dict.fromkeys(d)))
z = 1
match z:
    case 3: pass
    case 1: print("aaaa")
