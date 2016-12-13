#!/usr/bin/env python3

# shelve模块简介：

import shelve

d = shelve.open('shelve_test')   # 打开一个文件；

class Test(object):
    def __init__(self,n):
        self.n = n

t = Test(123)
t2 = Test(123334)

name = ['alex','rain','test']

d["test"] = name   #持久化列表
d["t1"] = t        #持久化类
d["t2"] = 52

d.close()
