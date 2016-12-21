1、分别使用递归、循环和生成器求斐波那契数列。
f(0) = 1
f(1) = 1
f(n) = f(n-1) + f(n-2)


## 递归实现：
```python 
In [5]: def fib1(n):
   ...:     if n == 0 or n == 1:
   ...:         return 1
   ...:     return fib1(n-1) + fib1(n-2)
```

## 循环实现：
```python 
# 空间复杂度较高；
In [16]: def fib2(n):
    ...:     lst = []
    ...:     for i in range(n+1):
    ...:         if i == 0 or i == 1:
    ...:             lst.append(1)
    ...:         else:
    ...:             lst.append(lst[-1] + lst[-2])
    ...:     print(lst)
    ...:     return lst.pop()
    ...:     
```

```python 
# 滑动窗口
In [19]: def fib3(n):
    ...:     a,b = 1,1
    ...:     for i in range(n+1):
    ...:         if i == 0 or i == 1:
    ...:             a,b = 1,1
    ...:         else:
    ...:             a,b = b,a + b
    ...:     return b
```

## 生成器方式实现：
```python 
In [24]: def fib_gen():
    ...:     idx = 0 
    ...:     a,b = 1,1
    ...:     while True:
    ...:         if idx == 0 or idx == 1:
    ...:             yield 1
    ...:         else:
    ...:             yield b
    ...:             a,b = b,a+b
    ...:         idx += 1
    ...:         


In [27]: def fib4(n):
    ...:     gen = fib_gen()
    ...:     for _ in range(n+1):
    ...:         next(gen)
    ...:     return next(gen)
    ...: 

In [28]: fib4(5)
Out[28]: 8

In [29]: fib4(6)
Out[29]: 13
```
## 生成器用来替换递归，通常用于此递归无法转换为迭代；


2、写一个函数，实现对整数的排序，默认升序排列，不能使用任何内置函数和第三方库；

```python 
In [35]: def sort(lst,reverse=False):
    ...:     dst = []
    ...:     for n in lst:
    ...:         for i,e in enumerate(dst):
    ...:             if not reverse:
    ...:                 if n < e:
    ...:                     dst.insert(i,n)
    ...:                     break
    ...:             else:
    ...:                 if n > e:
    ...:                     dst.insert(i,n)
    ...:                     break
    ...:         else:
    ...:             dst.append(n)
    ...:     return dst
    ...:     
    ...:                 
    ...: 

In [36]: sort([3,2,1,1,5,5,4,7,8,6])
Out[36]: [1, 1, 2, 3, 4, 5, 5, 6, 7, 8]
```


3、罗马数字转阿拉伯数字：

```python 
In [40]: def roman_to_int(src):
    ...:     convert_map = {
    ...:         'I':1,
    ...:         'V':5,
    ...:         'X':10,
    ...:         'L':50,
    ...:         'C':100,
    ...:         'D':500,
    ...:         'M':1000
    ...:     }
    ...:     roman = src.upper()[::-1]
    ...:     prev = 0
    ...:     lst = []
    ...:     for x in roman:
    ...:         i = convert_map[x]
    ...:         if i < prev:
    ...:             lst.append(-1 * i)
    ...:         else:
    ...:             lst.append(i)
    ...:         prev = i
    ...:     return sum(lst)
    ...: 

In [41]: roman_to_int('MCMLXXVII')
Out[41]: 1977

In [42]: roman_to_int('MCMLXXXVII')
Out[42]: 1987
```

