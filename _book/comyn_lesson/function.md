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

## [代码执行流程分析网站](http://pythontutor.com)

函数的执行流程中的概念：


### 内存的分区：
* 堆： 支持随机访问，用于保存数据；引用；
* 栈： 先进后出，用于保存现场；值(引用真正保存的数据)；
* 指令： 顺序访问，用于存储程序指令；


```python 
def inc(n):
    return n+1

def inc_add(a,b):
    return inc(a) + inc(b)

x = 1
y = 2
z = inc_add(x,y)
```


## 默认参数：

    默认参数是在函数定义时的概念；

```python 
In [1]: def inc(init,step): 
   ...:         return init + step
   ...: 

In [2]: inc(3,2)
Out[2]: 5
# 一般情况下，step都是1的话，我们可以使用默认参数；
In [3]: inc(3,3)
Out[3]: 6
```

```python 
In [4]: def inc(init,step=1):   # step默认为1，调用时可以省略；
   ...:         return init + step
   ...: 

In [5]: inc(3,2)
Out[5]: 5

In [6]: inc(3)
Out[6]: 4
```

* 默认参数的作用：

**让API简洁，但又不失去灵活性；**

```python 
In [11]: def inc(x):
    ...:     return x + 1
    ...: 

In [12]: inc(10)
Out[12]: 11

In [13]: def new_inc(init,step):
    ...:     return init + step
    ...: 

In [14]: new_inc(10,2)
Out[14]: 12

In [15]: def inc(init,step=1):
    ...:     return init + step
    ...: 
```
**当重构的时候，默认参数可以很好的向下兼容。**

```python 
In [16]: def inc(init=0,step):
    ...:         return init + step
  File "<ipython-input-16-52cb4155d7a0>", line 1
    def inc(init=0,step):
           ^
SyntaxError: non-default argument follows default argument
```
**非默认参数必须在默认参数的前面。**

**允许有多个默认参数，但是默认参数需要放在参数列表的最后面。**


```python 
In [27]: def append(x,lst=[]):   # 对于默认参数，定义函数时就定义了一个变量了；
    ...:     lst.append(x)
    ...:     return lst
    ...: 

In [28]: append(1)
Out[28]: [1]

In [29]: append(2)
Out[29]: [1, 2]
```

```python 
In [30]: def append(x,lst=None):
    ...:     if lst is None:
    ...:         lst = []
    ...:     lst.append(x)
    ...:     return lst
    ...: 

In [31]: append(1)
Out[31]: [1]

In [32]: append(2)
Out[32]: [2]
```
**通常来说，当默认参数是可变对象(list,dict,set,bytearray)的时候，需要特别注意作用域的问题；**


## 再谈作用域：

* 全局作用域
* 函数作用域

### 全局作用域：
* 函数之外的；
* 参数列表里的；(只能在当前函数中才能调用，在全局中看不到它的名字。)

### 函数作用域：
* 函数内定义的；

### 内置函数：
* locals()  以字典形式返回当前作用域下的所有变量；

```python 
In [40]: def fn():
    ...:     x = 1
    ...:     print(locals())
    ...:     

In [41]: fn()
{'x': 1}

In [42]: def fn(x):
    ...:     print(locals())
    ...:     

In [43]: fn(3)
{'x': 3}

In [44]: def fn(x):
    ...:     x = 1
    ...:     print(locals())
    ...:     

In [45]: fn(3)
{'x': 1}
```

* globals()  以字典形式返回当前作用域内的所有全局变量；


## 位置参数：

    位置参数的顺序必须一致(定义时的顺序和调用时的顺序);

```python 
In [50]: def minus(x,y):
    ...:     return x - y
    ...: 

In [51]: minus(5,3)  # 位置参数；位置传参；
Out[51]: 2

In [53]: minus(3,5)  # 位置参数；位置传参；
Out[53]: -2
```

## 关键字参数：

```python 
In [54]: minus(x=5,y=3)    # 关键字传参；
Out[54]: 2

In [55]: minus(y=3,x=5)    # 关键字传参；
Out[55]: 2
```

**位置传参和关键字传参是函数调用时的概念。**

```python 
In [56]: def connect(host,port,user,password,db):   # 仅使用位置参数；
    ...:     pass
    ...: 

In [57]: connect('127.0.0.1',3306,'root','123456','test') # 调用时全部使用位置参数很累；

In [58]: connect(host='127.0.0.1',port=3306,user='root',password='123456',db='test') # 全部使用关键字传参，也很累；

In [59]: def connect(host='127.0.0.1',port=3306,user='root',password='123456',db='test'): # 若定义时使用默认参数，调用就很方便了；
    ...:     pass
    ...: 

In [60]: connect()    # 全部使用默认参数进行调用；
```








































































