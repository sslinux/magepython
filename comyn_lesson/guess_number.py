#！/usr/bin/env python 


NUM = 35

count = 0 

while count < 3:
    user_input = int(input("plz input a number:"))
    if user_input == NUM:
        print("you win")
    elif user_input < NUM:
        print("less")
    else:
        print("big")
    count += 1
else:
    print("you lose")


for _ in range(0,3):
    user_input = int(input("plz input a number:"))
    if user_input == NUM:
        print("you win")
    elif user_input < NUM:
        print("less")
    else:
        print("big")
    count += 1
else:
    print("you lose")

