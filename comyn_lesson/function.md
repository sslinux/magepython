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

**位置参数可以和关键字参数并存，但在调用函数时，关键字参数必须写在位置参数之后；**

```python 
connect('192.168.47.129',user='sslinux','1qaz2wsx')   # 报错；

connect('192.168.47.129',user='sslinux',password='1qaz2wsx')  # 关键字参数之后只能继续使用关键字参数；
```

---
---
# 可变参数：

## 可变位置参数：

问题引入：

```python
n [62]: '{} {}'.format(3,4)  # format函数接收的参数个数是不固定的；
Out[62]: '3 4'

In [63]: '{}'.format(3)
Out[63]: '3'
```

**可变位置参数用星号(\*)定义,在函数体内，可变参数是一个元组。**
```python
In [64]: def fn(*args):
    ...:     print(args)
    ...:     

In [65]: fn()   # 没穿参数，是一个空元组；
()

In [66]: fn(1)
(1,)

In [67]: fn(1,2,3,4,5,6)
(1, 2, 3, 4, 5, 6)
```


```python
In [68]: fn(args=(1,2,3))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-68-b007f2d20303> in <module>()
----> 1 fn(args=(1,2,3))

TypeError: fn() got an unexpected keyword argument 'args'
```


## 可变关键字参数：

```python 
In [69]: def fn(**kwargs):
    ...:     print(kwargs)
    ...:     

In [70]: fn(a=1,b=2)
{'b': 2, 'a': 1}
```
**可变关键字参数使用两个星号(\*\*)来定义,在函数体内，可变关键字参数是一个字典；**

**可变关键字参数的key都是字符串，并且符合标识符定义规范;**

```python 
In [71]: def printName(*username):
    ...:     print(username)
    ...:     

In [72]: printName('guiyin.xiong','long.wang')
('guiyin.xiong', 'long.wang')

In [73]: def printInfo(**information):
    ...:     print(information)
    ...:     

In [74]: printInfo(name='guiyin.xiong',gender='Famle',age=18,hometown='Sichuan')
{'hometown': 'Sichuan', 'age': 18, 'gender': 'Famle', 'name': 'guiyin.xiong'}

In [75]: t = ('jason','michael','lucy')

In [76]: d = {'name':'guiyin.xiong','age':18}

In [77]: printName(t)
(('jason', 'michael', 'lucy'),)

In [78]: printInfo(d)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-78-b2184561aa19> in <module>()
----> 1 printInfo(d)

TypeError: printInfo() takes 0 positional arguments but 1 was given

In [79]: printInfo(**d)
{'age': 18, 'name': 'guiyin.xiong'}
```

* 可变位置参数只能以位置参数的形式调用；
* 可变关键字参数只能以关键字参数的形式调用；

```python 
In [80]: def fn(*args,**kwargs):
    ...:     print(args)
    ...:     print(kwargs)
    ...:     

In [81]: fn(1,2,3,a=1,b=2)
(1, 2, 3)
{'b': 2, 'a': 1}
```

```python 
In [1]: def fn(**args,*args):   
  File "<ipython-input-1-bd0a37fd5749>", line 1
    def fn(**args,*args):   # 定义函数时，可变关键字参数，不能在可变位置参数前面；
                 ^
SyntaxError: invalid syntax
```

**可变位置参数必须在可变关键字参数之前(不管是定义还是调用时。)**


```python 
n [2]: def fn(x,y,*args,**kwargs):
   ...:     print(x)
   ...:     print(y)
   ...:     print(args)
   ...:     print(kwargs)
   ...:     

In [3]: fn(1,2,3,4,5,6,7,a=1,b=2)
1
2
(3, 4, 5, 6, 7)
{'a': 1, 'b': 2}
# 调用时传递的关键字参数，与定义时位置参数的变量名重名咯；
In [4]: fn(1,2,3,4,x=5,y=6,a=7,b=8)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-0f897955d8b4> in <module>()
----> 1 fn(1,2,3,4,x=5,y=6,a=7,b=8)

TypeError: fn() got multiple values for argument 'x'
```

```python 
In [5]: def fn(*args,x,y):  # 在可变位置参数后，x,y被当成了关键字参数；
   ...:     print(args)
   ...:     print(x,y)
   ...:     

In [6]: fn(1,2,3,4)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-367b9b614766> in <module>()
----> 1 fn(1,2,3,4)

TypeError: fn() missing 2 required keyword-only arguments: 'x' and 'y'
# 缺少两个关键字参数：x和y


In [7]: fn(1,2,x=3,y=4)
(1, 2)
3 4

In [8]: def fn(*args,x,y,**kwargs):
   ...:     print(args)
   ...:     print(x,y)
   ...:     print(kwargs)
   ...:     

In [9]: fn(1,2,x=3,y=4,a=5,b=6)
(1, 2)
3 4
{'a': 5, 'b': 6}

In [10]: fn(1,2,a=5,b=6,x=3,y=4)
(1, 2)
3 4
{'a': 5, 'b': 6}
```


```python 
In [11]: def fn(x,y=1,*args,**kwargs):
    ...:     print(x,y)
    ...:     print(args)
    ...:     print(kwargs)
    ...:     

In [12]: fn(1,2,3,4,5,a=6,b=7)
1 2
(3, 4, 5)
{'a': 6, 'b': 7}

In [13]: def fn(x,*args,y=1,**kwargs):
    ...:     print(x,y)
    ...:     print(args)
    ...:     print(kwargs)
    ...:     

In [14]: fn(1,2,3,4,5,a=6,b=7)
1 1
(2, 3, 4, 5)
{'a': 6, 'b': 7}

In [15]: fn(1,2,3,4,5,a=6,b=7,x=8,y=9)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-a9e515b2f156> in <module>()
----> 1 fn(1,2,3,4,5,a=6,b=7,x=8,y=9)

TypeError: fn() got multiple values for argument 'x'

In [16]: def fn(*args,x,y=1,**kwargs):
    ...:     print(x,y)
    ...:     print(args)
    ...:     print(kwargs)
```


## 规律：

* 可变参数后置；
* 可变参数不和默认参数一起出现；

```python 
#在使用可变关键字参数时，如果一定要使用默认参数的话就这样用；

def fn(**kwargs):   
    a = kwargs.get('a',1)   # 判断可变关键字参数中是否有a,如果没有就赋予默认值；
```


## 参数解构：


### 位置参数解包：

位置参数解包，必须是针对线性结构(序列);

```python
In [17]: def fn(a,b,c):
    ...:     print(a,b,c)
    ...:     

In [18]: lst = [1,2,3]

In [19]: fn(lst[0],lst[1],lst[2])
1 2 3

# 函数调用时，一个星号(*)可以把线性结构解包成位置参数；
In [20]: fn(*lst)
1 2 3

In [21]: lst = [1,2,3,4]

In [22]: fn(*lst)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-22-7efbe31a6763> in <module>()
----> 1 fn(*lst)

TypeError: fn() takes 3 positional arguments but 4 were given

```

### 关键字参数解包：

关键字解包，必须是针对字典；

```python
In [23]: d = {'a':1,'b':2,'c':3}

# 调用函数时，两个星号(**)可以把字典解构成关键字参数；
In [24]: fn(**d)
1 2 3
```



---

定义时使用可变参数，调用时使用参数解包：

```python 
In [25]: def fn(a,b,c,*args):  # 定义时使用可变位置参数；
    ...:     print(a,b,c)
    ...:     print(args)
    ...:     

In [26]: lst = list(range(10))

# 调用时使用位置参数解包，列表；
In [27]: fn(*lst)
0 1 2
(3, 4, 5, 6, 7, 8, 9)

In [28]: lst = tuple(range(11,20))
# 调用时使用位置参数解包，元组；
In [29]: fn(*lst)
11 12 13
(14, 15, 16, 17, 18, 19)
```

```python
In [30]: def fn(a,b,c,*args,**kwargs):
    ...:     print(a,b,c)
    ...:     print(args)
    ...:     print(kwargs)
    ...:     

In [31]: dt = {'a':1,'b':2,'c':3,'d':4,'e':5}

In [32]: fn(**dt)  # 调用时使用可变关键字参数解包，但未传递可变位置参数，所以会输出一个空元组；
1 2 3
()
{'d': 4, 'e': 5}
```

### 传参的顺序(建议)： 位置参数、线性结构解构、关键字参数、字典解构；

**解构的时候，线性结构的解构是位置参数，字典解构是关键字参数；

```python
# 不建议两种结构混合使用；
In [33]: def fn(a,b,c,d):
    ...:     print(a,b,c,d)
    ...:     

In [34]: fn(0,b=1,*[2],**{'d':3})
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-34-45ec77cbf68a> in <module>()
----> 1 fn(0,b=1,*[2],**{'d':3})

TypeError: fn() got multiple values for argument 'b'

In [35]: fn(0,*[2],c=1,**{'d':3})
0 2 1 3
```

**尽量少的同时使用两种解构，除非你真的知道在做什么**


---
---

## 参数槽

        定义的时候叫参数槽(slot)，调用的时候叫命名参数(named argument)

```python
In [36]: def fn(a,b,c):
    ...:     print(a,b,c)
    ...:     

In [37]: fn(1,2,3)
1 2 3

In [38]: fn(a=1,b=2,c=3)
1 2 3

In [39]: def fn(*,a,b,c): # *号之后的参数，必须以关键字参数的形式传递，称之为参数槽；
    ...:     print(a,b,c)
    ...:     

In [40]: fn(1,2,3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-40-cfb566fc1d8f> in <module>()
----> 1 fn(1,2,3)

TypeError: fn() takes 0 positional arguments but 3 were given

In [41]: fn(a=1,b=2,c=3)
1 2 3
```

### \*号之后的参数，必须以关键字参数的形式传递，称之为参数槽（slot)；

```python
In [42]: def fn(a,b,*,c):
    ...:     print(a,b,c)
    ...:     

In [43]: fn(1,2,c=3)
1 2 3

In [44]: fn(a=1,b=2,c=3)
1 2 3

In [45]: fn(1,b=2,c=3)
1 2 3

In [46]: fn(1,b=2,3)  # 参数槽前面可以使用位置参数也可以使用关键字参数，但参数槽后，只能使用关键字参数传递；
  File "<ipython-input-46-aa9cb7e5f8c9>", line 1
    fn(1,b=2,3)
            ^
SyntaxError: positional argument follows keyword argument
```

**参数槽通常和默认参数搭配使用；**


* 星号(\*)之后必须有参数；
```python
In [54]: def fn(a,b,*):
    ...:     print(a,b)
  File "<ipython-input-54-817145d612f5>", line 1
    def fn(a,b,*):
              ^
SyntaxError: named arguments must follow bare *
```


* 命名参数可以有默认值：
```python
In [55]: def fn(a,b,*,c=1):
    ...:     print(a,b,c)
    ...:     

In [56]: fn(1,2)
1 2 1

In [57]: fn(1,2,c=3)
1 2 3
```

* 命名参数有默认值时，命名参数必须有默认值：
```python 
In [58]: def fn(a,b=1,*,c=1):
    ...:     print(a,b,c)
    ...:     

In [59]: fn(0)
0 1 1

In [60]: fn(0,c=3)
0 1 3

```

* 非命名参数有默认值时，命名参数可以没有默认值；

**默认参数应该在每段参数的最后。**

---

**使用参数槽时，不能使用可变位置参数，可变关键字参数，必须放在命名参数之后。**


```python 
In [62]: def fn(a,*args,*,c):
  File "<ipython-input-62-3e167b300ece>", line 1
    def fn(a,*args,*,c):
                   ^
SyntaxError: invalid syntax


In [63]: def fn(a,*,**kwargs):
    ...:     print(a)
  File "<ipython-input-63-5ace9df68721>", line 1
    def fn(a,*,**kwargs):
              ^
SyntaxError: named arguments must follow bare *


In [64]: def fn(a,**kwargs,*,c):
  File "<ipython-input-64-a4cfeefa2770>", line 1
    def fn(a,**kwargs,*,c):
                     ^
SyntaxError: invalid syntax

In [65]: def fn(a,*,c,**kwargs):
    ...:     print(a,c)
    ...:     print(kwargs)
    ...:     

In [66]: fn(1,c=2,b=3,d=4)
1 2
{'d': 4, 'b': 3}

In [67]: def fn(a,*,c,*args,**kwargs):   # 使用参数槽时，不能使用可变位置参数；
    ...:     print(a)
    ...:     print(c)
    ...:     print(args)
    ...:     print(kwargs)
  File "<ipython-input-67-da26942ef118>", line 1
    def fn(a,*,c,*args,**kwargs):
                 ^
SyntaxError: invalid syntax

```

---
---


## 类型示意 Python3.5才有；

```python
In [68]: def add(x:int,y:int) -> int:
    ...:     return x + y
    ...: 

In [69]: add(1,2)
Out[69]: 3

In [70]: help(add)


In [71]: add(1.0,2.0)
Out[71]: 3.0

In [72]: add('x','y')
Out[72]: 'xy'

In [73]:help(add)
Out[73]:add(x:int, y:int) -> int

```
**类型示意任何类型检查，仅仅只是一个示意而已。**

但是有什么用呢？

        python是一种自文档的语言。

```python 
def add(x,y):
    '''
    @param x int
    @param y int
    @return int
    '''
    return x + y
```

```python
def add2(x:int,y:int) -> int:
    return x + y 

help(add)
```

三引号在python中是docstring，可以作为注释使用；


### 类型示意的作用：

* 更清晰的自文档；
* 帮助IDE做检查；
* 可以通过这种机制，做类型检查；
















































