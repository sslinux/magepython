
# 打印素数：
for n in range(2,101):
    for x in range(2,n):
        if n % x == 0:
            break 
    else:
        print(n)




