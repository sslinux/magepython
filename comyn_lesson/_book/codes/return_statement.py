#!/usr/bin/env python

def add(a,b):
    return a + b

def sum(*num):
    ret = 0
    for x in num:
        ret += x
    return ret

lst = list(range(20))

print(sum(*lst))
print(sum(1,3,5,7,9))


