#!/usr/bin/env python 

class Door:
    def __init__(self,number,status):
        self.number = number
        self.status = "closed"

    def open(self):
        self.status = "openning"

    def close(self):
        self.status = "closed"

door = Door(1001,"closed")
door.open()
print(door.status)
Door.close(door)
print(door.status)


