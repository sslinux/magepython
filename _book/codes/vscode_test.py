#!/usr/bin/env python3
class person(object):
    commpany = 'symbio'

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def setcommpay(self,commpany):
        self.commpany = commpany

    def getcommpany(self):
        print(self.commpany)

        