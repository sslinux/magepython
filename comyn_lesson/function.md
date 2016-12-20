# 函数

## 函数性质：

    组织好的、可重用的、功能单一的代码片段；

    输入：参数；

    输出：返回值；


## 函数的定义：

```python 
In [2]: def fn(x):
   ...:     print(x)
   ...:     

In [3]: ## 函数调用;

In [4]: fn('guiyin.xiong')
guiyin.xiong

```

## 函数参数：

```python 
# 当函数有多个参数的时候，参数之间使用逗号分隔；
In [7]: def add(x,y):
   ...:     print('{} + {}  = {}'.format(x,y,x+y))
   ...:     

# 调用的时候，按顺序传入相同个数的参数；
In [8]: add(1,2)
1 + 2  = 3

In [9]: add(2,1)
2 + 1  = 3
```
**参数的顺序比较重要**

### python中，参数总是引用传递；

在python中一切皆对象；

对操作系统而言：值是保存在栈空间的，引用是保存在堆空间的；

```python 
In [19]: def swap(x,y):
    ...:     print(id(x),id(y))
    ...:     x,y = y,x
    ...:     print(id(x),id(y))
    ...:     

In [20]: x = 3

In [21]: y = 4

In [22]: swap(x,y)
9169600 9169632
9169632 9169600
```

## 作用域

    函数是python的最小作用域；


## 返回值

```python
In [25]: def add(x,y):
    ...:     return x+y   # 返回；
    ...: 

In [26]: add(1,2)
Out[26]: 3

In [27]: a = add(1,2)

In [28]: print(a)
3
```
没有显式地return语句，函数返回None；


函数只能返回一个值，如果return语句后面有多个逗号分隔的值，会自动封包成一个元组；

```python 
In [29]: def unpack(lst):
    ...:     head,*tail = lst
    ...:     return head,tail
    ...: 

In [30]: head,tail = unpack(lst)

In [31]: head
Out[31]: 1

In [32]: tail
Out[32]: [2, 3, 4]

In [33]: t = unpack(lst)

In [34]: type(t)
Out[34]: tuple

In [35]: t
Out[35]: (1, [2, 3, 4])
```

### 一个函数可以有任意多个return语句，但是始终只会执行第一个return语句，

### 执行return语句，会返回调用方的作用域，函数的作用域就被销毁了；

```python 
In [39]: def append(lst,x):
    ...:     return
    ...:     lst.append(x)
    ...: 

In [40]: lst
Out[40]: [1, 2, 3, 4]

In [41]: append(lst,5)

In [42]: lst   # 元素5并没有追加到lst中，因为执行到return语句后，函数就返回调用方了；
Out[42]: [1, 2, 3, 4]
```

简单理解：

    return 结束一个函数；

```python 
In [45]: def p(lst):
    ...:     for x in lst:
    ...:         if x == 2:
    ...:             return    # 结束了该函数；
    ...:     else:
    ...:         print('haha')  # 所以haha永远都不会输出；
    ...:             

In [46]: p([1,2,3,4,5,6])
```

**return之后，函数内的任何语句不再执行；**

```python             
In [47]: def loop(lst1,lst2):
    ...:     for x in lst1:
    ...:         for y in lst2:
    ...:             print(x,y)
    ...:             if y == 3:
    ...:                 return
    ...:           
# break只是结束本层循环，而return是结束函数，return之后的语句都不会再执行；
In [48]: loop(range(10),range(10))
0 0
0 1
0 2
0 3
```


## 函数的执行流程：

http://pythontutor.com

