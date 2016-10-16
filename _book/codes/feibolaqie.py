#!/usr/bin/env python3
l0 = []
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []

def quMo(num):
    if num % 9 == 0:
        l0.append(num)
    elif num % 9 == 1:
        l1.append(num)
    elif num % 9 == 2:
        l2.append(num)
    elif num % 9 == 3:
        l3.append(num)
    elif num % 9 == 4:
        l4.append(num)
    elif num % 9 == 5:
        l5.append(num)
    elif num % 9 == 6:
        l6.append(num)
    elif num % 9 == 7:
        l7.append(num)
    elif num % 9 == 8:
        l8.append(num)
    else:
        return "fuck you"

for num in range(1,1000):
    quMo(num)

print(len(l0))
print(len(l1))
print(len(l2))
print(len(l3))
print(len(l4))
print(len(l5))
print(len(l6))
print(len(l7))
print(len(l8))



