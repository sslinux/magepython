import random

cai = []

for i in range(0,6):
    lan = random.randrange(1,33)
    if lan not in cai:
        cai.append(lan)
    else:
        lan = random.randrange(1,33)
        cai.append(lan)

cai.sort()
print(cai)



