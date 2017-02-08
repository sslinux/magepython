#!/usr/bin/env python3

import random
import string 
# 生成大写字母和小写字母列表：
# capital = [ chr(i) for i in range(65,91)]
# lowercase = [chr(i) for i in range(97,123)]

# string模块中已经有相应的实现，不过是字符串而已；
letters = list(string.ascii_letters)
capital = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
digits = list(string.digits)
punctuation = list(string.punctuation)

print(letters)
print(capital)
print(lowercase)
print(digits)
print(punctuation)
ran_lower = random.choice(digits)
print(ran_lower)


