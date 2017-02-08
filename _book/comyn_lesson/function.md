# 函数

## 函数性质：

    组织好的、可重用的、功能单一的代码片段；
    函数是Python里组织代码的最小单元；

    输入：参数；

    输出：返回值；


## 函数的定义：

def Function_Name(arguments,...):
    Function_suit
    return xxx


```python 
In [2]: def fn(x):  # 函数定义def表示定义一个函数，紧接着是函数名，函数名后面用一对小括号列出参数列表，参数列表后面使用 一个冒号开始的函数体；

   ...:     print(x)   # 函数体是正常的python语句，可以包含任意结构；
            return x+1 #return语句表示函数的返回值；
# 函数有输入(参数)和输出(返回值),函数其实是一个代码单元，把输入转化为输出。 
```

## 函数调用;

定义函数的时候，并不会执行函数体，当调用函数的时候，才会执行其中的语句块。

调用方式：

    Function_Name(Arguments,...)  

    函数调用时，传入的参数必须和定义时的参数相匹配；如果不匹配，会抛出TypeError；


```python 
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

```python
def add(x,y):
    ret = x + y 
    print('{} + {} = {}'.format(x,y,ret))

add(3,5)   # 参数按照定义的顺序传入，这样的传参方法叫做位置参数；

add(y=3,x=5)  # 参数按照定义时的变量名传递，这样的传参方法称为关键字参数；关键字参数和顺序无关。

add(3,y=5)  # 位置参数和关键字参数混合使用；

# add(x=3,5)  # 当关键字参数和位置参数混合使用时，位置参数必须在前面，否则会引发错误；
```


##参数

###参数默认值：

参数可以有默认值，当一个参数有默认值时，调用时如果不传递此参数，会使用默认值；

```python 
def inc(base,x=1): # 带默认值的参数必须在不带默认值的参数之后；
    return base + x
     
inc(3,1)
inc(3,2)

def connect(host="127.0.0.1",port=3306,user='root',password='',db='test'):
    pass

connect('172.16.0.1',password='abcd')
# 参数默认值和关键字参数一起使用，会让代码非常简洁；
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




## 返回值

    使用可选的return语句进行返回，若省略return语句则默认返回none。
```python
In [25]: def add(x,y):
    ...:     return x+y   # return语句除了返回值外，还会结束函数，即return之后的语句将不会被执行；
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

    return 返回指定的值(默认为None),并结束一个函数；

```python 
In [45]: def p(lst):
    ...:     for x in lst:
    ...:         if x == 2:
    ...:             return None   # return None 可以简写为return，通常用于结束函数；
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
main()      # 全局作用域
    f1()    # 当调用函数的时候，解释器会把当前现场压栈，然后开始执行被调用函数，
            # 被调用函数执行完成，解释器弹出当前栈顶，恢复现场；
# 压栈(保存现场)的内容：
#    各种变量的地址；

```

```python 
def inc(n):
    return n+1

def inc_add(a,b):
    return inc(a) + inc(b)

x = 1
y = 2
z = inc_add(x,y)
```

---

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

---

## 作用域

    作用域是一个变量的可见范围叫做这个变量的作用域；

    函数是python的最小作用域；

```python
x = 1  # 定义在全局作用域中；

def inc():   #函数内部时一个局部作用域，不能直接使用全局作用域的变量；
    x += 1
    return x

inc()    # 调用时会报本地变量x在使用前未被声明的错误；
```

## 再谈作用域：

* 全局作用域(针对文件而言)
* 函数作用域

变量的作用域为变量定义同级的作用域；

```python
In [1]: def fn():   # 上级作用域对下级作用域可见；
   ...:     xx = 1
   ...:     print(xx)
   ...:     def inner():
   ...:         print(xx)
   ...:     inner()
   ...:     

In [2]: fn()
1
1
```

```python
In [3]: def fn():    # 上级作用域对下级作用域时只读可见的；
   ...:     xx = 1
   ...:     print(xx)
   ...:     def inner():
   ...:         xx = 2     # 赋值即定义，在下级作用域里面，重新定义了xx。  # 如果此处修改为 xx += 2则会报错；
   ...:     inner()
   ...:     print(xx)
   ...:     
   ...:     

In [4]: fn()
1
1
```

不同作用域变量不可见，但是下级作用域可以对上级作用域的变量只读可见；

全局作用域对所有作用域可见；

```python
In [1]: xx = 1

In [2]: def fn():
   ...:     global xx   # 不管xx在全局中是否定义，都可以提升变量作用域为全局变量；
                        # 提升只是标记，并没有定义变量，还需要在某处定义变量；
   ...:     xx += 1
   ...:     

In [3]: fn()

In [4]: xx
Out[4]: 2
```

```python
In [6]: def fn():
   ...:     global zz # global的提升只对本作用域有用，如果要在其他非全局作用域使用，也需要作同样的提升；
   ...:     zz = 3
   ...:     print(zz)
   ...:     

In [7]: def fn2():
   ...:     global zz  # 虽然前面的fn()函数已经使用global提升zz为全局变量了，但是只对fn()和全局有效；
                       # fn2()想要引用全局的变量zz还是需要重新提升的；
   ...:     zz += 1
   ...:     print(zz)
   ...:     

In [8]: fn()
3

In [9]: zz
Out[9]: 3

In [10]: fn2()
4

In [11]: zz
Out[11]: 4
```

**建议：** 

**除非你清除的知道global会带来什么，并且明确的知道，非global不行，否则不要使用global。**


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


## 默认参数的作用域：

在python中一切皆对象，函数也是对象，参数是函数对象的属性，所以函数的作用域伴随函数整个生命周期；

```python
In [23]: def fn(xxyy=[]):
    ...:     xxyy.append(1)
    ...:     print(xxyy)
    ...:     

In [24]: fn()
[1]

In [25]: fn()
[1, 1]

In [26]: fn.__defaults__
Out[26]: ([1, 1],)

In [27]: fn()
[1, 1, 1]

In [28]: fn.__defaults__
Out[28]: ([1, 1, 1],)
```

### 何时销毁：

对于定义在全局作用域里面的函数：

* 重新定义：
* del关键字删除；
* 程序结束；

对于局部作用域：

* 重新定义；
* del 删除；
* 上级作用域被销毁；


**注意：**

    当使用可变类型作为默认参数的默认值时，需要特别注意；
```python 
In [34]: def fn(x=0,y=0):
    ...:     x += 3
    ...:     y += 3
    ...:     

In [35]: fn.__defaults__
Out[35]: (0, 0)

In [36]: fn()

In [37]: fn.__defaults__
Out[37]: (0, 0)
```

### 解决方法：
* 使用不可变类型作为默认值；
* 函数体内不改变默认值；

Example:

```python 
# 使用不可变类型作为默认值；
In [38]: def fn(lst=None):
    ...:     if lst is None:
    ...:         lst = []
             else:
                 lst = lst[:]
    ...:     lst.append(3) # 如果传入的参数是非None，那么改变了传入参数；
    ...:     print(lst)
    ...:     

In [39]: fn.__defaults__
Out[39]: (None,)

In [40]: fn()
[3]

In [41]: fn()
[3]

In [42]: fn.__defaults__
Out[42]: (None,)
```

Example:

```python 
# 函数体内不改变默认值；
In [43]: def fn(lst=[]):
    ...:     lst = lst[:]   # 这里是影子拷贝；
    ...:     lst.append(3)  # 无论如何不修改传入参数；
    ...:     print(lst)
    ...:     

In [44]: fn()
[3]

In [45]: fn()
[3]

In [46]: fn.__defaults__
Out[46]: ([],)
```
通常如果使用一个可变类型作为默认参数时，会使用None来代替；

---

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
def sum(lst):
    ret = 0 
    for x in lst:
        ret += x
    return ret  

print(sum([1,2,3,4]))

def sum2(*lst):    # 参数前加一个星号，表示这个参数是可变的，也就是可以接受任意多个参数，这些参数将构成一个元组；
    print(type(lst))
    ret = 0 
    for x in lst:
        ret += x
    return ret 

print(sum2(1,2,5))
print(sum2(1,3,5,7,9))
```

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
def connect(**kwargs): # 参数前加两个星号，表示这个参数是可变的，可以接收任意多个参数，这些参数构成一个字典，此时只能通过关键字参数传递；
    print(type(kwargs))
    for k,v in kwargs.items():
        print('{} => {}'.format(k,v))

connect(host="127.0.0.1",port=3306)
```

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

* 默认参数靠后；
* 可变参数后置；
* 可变参数不和默认参数一起出现；

```python 
#在使用可变关键字参数时，如果一定要使用默认参数的话就这样用；

def fn(**kwargs):   
    a = kwargs.get('a',1)   # 判断可变关键字参数中是否有a,如果没有就赋予默认值；

def connect(**kwargs):
    host = kwargs.pop('host','127.0.0.1')  # 使用pop或get都可以判断其是否有值传入，如果没有就赋予默认值；
    port = kwargs.get('port',3306)
    print(host)
    print(port)

connect(user="root",password="",db="test")
```


## 参数解构：

参数解构发生在函数调用时；

可变参数发生在函数定义的时候；

### 位置参数解包：

函数调用时：位置参数解包，必须是针对线性结构(序列);

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

函数调用时：关键字参数解包，必须是针对字典；字典的key必须时str；

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

### keyword-only参数： py3新增的

**注意：**

**    keyword-only参数、参数槽(slot)、命名参数(named argument)说的都是一回事；**

```python
def fn(*,x):  # 星号之后的参数，只能通过关键字传递；叫做keyword-only参数；
              # 可变位置参数之后的参数也是keyword-only参数； 
    print(x)

fn(x=3)
```

```python
def fn(x=1,*,y=5):
    print(x)
    print(y)

def fn1(*,x=1,y=5):
    print(x)
    print(y)

def fn2(x=1,*,y):
    print(x)
    print(y)

# keyword-only参数可以有默认值；
# keyword-only参数可以和默认参数一起出现，不管它有没有默认值，不管默认参数是不是keyword-only参数；
# 通常的用法，keyword-only参数都有默认值；
```

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


* 定义函数时：星号(\*)之后必须有参数；
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
**类型示意不进行任何类型检查，仅仅只是一个示意而已。**

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



---
---

## 递归：

函数体内调用自身(函数自己);

递归函数必须要有退出条件；


**斐波那契数列：**

        f(0) = 1
        f(1) = 1
        f(n) = f(n-2) + f(n-1)


```python 
# 求斐波那契数列的第n项：
In [1]: def fib(n):
   ...:         if n == 0:
   ...:                 return 1
   ...:         if n == 1:
   ...:                 return 1
   ...:         return fib(n-1) + fib(n-2)
   ...: 

In [2]: fib(5)
Out[2]: 8

In [3]: fib(8)
Out[3]: 34
```

为了保护解释器，python对最大递归深度有限制；



**阶乘：**

        g(0) = 1
        g(1) = 1 
        g(n) = n * g(n-1)

```python 
def g(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * g(n-1)
```

递归函数总是涉及到压栈和出栈的过程；

递归函数压栈，直到遇到退出条件，然后出栈；

python的递归函数有深度限制，可以通过sys.getrecursionlimit()函数得到；

可以通过sys.setrecursionlimit()函数修改递归深度限制；

```python 
In [11]: import sys

In [12]: sys.getrecursionlimit()
Out[12]: 1000
```

```python 
In [13]: def g(n):
    ...:         if n == 0:
    ...:                 return 1
    ...:         if n == 1:
    ...:                 return 1
    ...:         return n * g(n-1)
    ...: 

In [14]: g(1000)
---------------------------------------------------------------------------
RecursionError                            Traceback (most recent call last)
<ipython-input-14-036a7be74c8a> in <module>()
----> 1 g(1000)

<ipython-input-13-8454a97b7766> in g(n)
      4         if n == 1:
      5                 return 1
----> 6         return n * g(n-1)

... last 1 frames repeated, from the frame below ...

<ipython-input-13-8454a97b7766> in g(n)
      4         if n == 1:
      5                 return 1
----> 6         return n * g(n-1)
# 提示说超出最大递归深度限制；
RecursionError: maximum recursion depth exceeded in comparison
```

```python 
# 修改最大递归深度限制，并重新调用递归函数计算；
In [15]: sys.setrecursionlimit(10000)

In [16]: g(1000)
Out[16]: 402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

函数调用的开销是比较大的，python中的递归没有做尾递归优化；

递归函数在python中比较慢，并且有深度限制(大多少语言都有)，所以**应尽量避免使用递归**。

循环都可以转化为递归，但不是所有递归都可以转化为循环；


```python 
In [19]: def g(n):
    ...:     ret = 1
    ...:     for x in range(1,n+1):
    ...:         ret *= x
    ...:     return ret
    ...: 

In [20]: g(1000)
Out[20]: 402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461
```

在python中可以完全不使用递归；

冯诺依曼模型本质就是递归；

绝大多数递归都可以转化为循环；

**千万要避免出现下面这样的代码：**

```python
# 环回引用函数：
def f():    # 不可重现错误；
    g()
def g():
    k()
def k():
    f()
```


---
---

## 生成器：

* 生成器解析式： 用小括号()代替列表解析式的中括号[].

g = (x for x in range(1,100))

```python 
In [21]: g = (x for x in range(1,100) if x % 2 == 1)

In [22]: type(g)
Out[22]: generator

In [23]: g
Out[23]: <generator object <genexpr> at 0x7fbca809ff68>


In [25]: next(g)
Out[25]: 1

In [26]: next(g)
Out[26]: 3
```

生成器惰性求值：

生成器定义：

```python 
In [27]: def gen():
    ...:     yield 0
    ...:     

In [28]: g = gen()

In [29]: type(g)
Out[29]: generator

In [30]: g
Out[30]: <generator object gen at 0x7fbca9351f68>

In [31]: next(g)
Out[31]: 0

In [32]: next(g)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-32-5f315c5de15b> in <module>()
----> 1 next(g)

StopIteration: 
```

```python 
In [33]: def gen():
    ...:     while True:
    ...:         yield 0
    ...:         print('....')
    ...:         

In [34]: g = gen()

In [35]: next(g)
Out[35]: 0

In [36]: next(g)
....
Out[36]: 0
```

**生成器的定义和函数类似，但是有yield语句；**

**生成器执行到yield的时候会暂停，再次next会从暂停的地方继续执行；**


```python 
In [37]: def gen(x):
    ...:     for i in range(x):
    ...:         yield x
    ...:         

In [38]: g = gen(10)

In [39]: for x in g:
    ...:     print(x)
    ...:     
10
10
10
10
10
10
10
10
10
10

In [40]: next(g)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-40-5f315c5de15b> in <module>()
----> 1 next(g)

StopIteration: 
```

**yield弹出值，并暂停函数；return返回值，并结束函数。**


```python 
In [41]: def gen(x):
    ...:     for i in range(10):
    ...:         if i == 3:
    ...:             return i
    ...:         yield i
    ...:         

In [42]: g = gen(10)

In [43]: for x in g:
    ...:     print(x)
    ...:     
0
1
2
```
**当yield和return同时存在时，return的返回值会被忽略，但是return依然可以中断生成器。**

```python 
In [44]: def gen(x):   # 生成器函数，返回值是一个生成器；
    ...:     for i in range(x):
    ...:         yield i 
    ...:     return 'ok'  # 会被当作StopIteration的值；
    ...: 

In [45]: for x in gen(10):
    ...:     print(x)
    ...:     
0
1
2
3
4
5
6
7
8
9
```

协程是用户空间的轻量线程，跑在一个线程内，由用户空间调度；

```python 
In [46]: def gen1():
    ...:     while True:
    ...:         yield 'gen 1'
    ...:         

In [48]: def gen2(g):
    ...:     for x in range(10):
    ...:         yield 'gen 2'
    ...:         print(next(g))
    ...:         

In [49]: g = gen2(gen1())

In [50]: next(g)
Out[50]: 'gen 2'

In [51]: next(g)
gen 1
Out[51]: 'gen 2'
```

**Example:计数器**

```python 
In [52]: def counter(init):
    ...:     c = init
    ...:     while True:
    ...:         yield c
    ...:         c += 1
    ...:         

In [53]: c = counter(0)

In [54]: next(c)
Out[54]: 0

In [55]: next(c)
Out[55]: 1
```

**Example: 惰性求值。求阶乘：**

```python 
In [70]: def factorial():
    ...:     ret = 1
    ...:     idx = 1
    ...:     while True:
    ...:         yield ret
    ...:         idx += 1
    ...:         ret *= idx
    ...:         

In [71]: g = factorial()

In [72]: next(g)
Out[72]: 1

In [73]: next(g)
Out[73]: 2

In [74]: next(g)
Out[74]: 6

In [75]: next(g)
Out[75]: 24

In [76]: next(g)
Out[76]: 120

In [77]: next(g)
Out[77]: 720
```


```python 
In [79]: def g(n):
    ...:     def factorial():
    ...:         ret = 1
    ...:         idx = 1
    ...:         while True:
    ...:             yield ret 
    ...:             idx += 1
    ...:             ret *= idx
    ...:     gen = factorial()
    ...:     for _ in range(n-1):
    ...:         next(gen)
    ...:     return next(gen)
    ...: 

In [82]: %timeit g(1000)
1000 loops, best of 3: 678 µs per loop

```

上例：**使用生成器来替换递归；**

**所有的递归，都可以用生成器替换；**

```python 
n [4]: def gen(n):
   ...:     for x in range(n):
   ...:         yield x   # 此处暂停一次；
   ...:         yield x   # 此处再暂停一次；
   ...:         

In [5]: g = gen(10)

In [6]: for i in g:
   ...:     print(i)
   ...:     
0
0
1
1
2
2
3
3
4
4
5
5
6
6
7
7
8
8
9
9
```


## yield from

```python 
In [7]: def gen(lst):                # python 2
   ...:     for x in lst:
   ...:         yield x
   ...:         

In [8]: g = gen(range(10))

In [9]: for x in g:
   ...:     print(x)
   ...:     
0
1
2
3
4
5
6
7
8
9

In [10]: def gen(lst):              # python 3
    ...:     yield from lst     # <==> for x in lst: yield x 
    ...:     

In [11]: g = gen(range(10))

In [12]: for x in g:
    ...:     print(x)
    ...:     
0
1
2
3
4
5
6
7
8
9
```

有yield关键字的函数，叫做生成器函数。

生成器函数返回的值，才叫生成器；



---
---

## 高阶函数：

可以接受别的函数作为参数的函数叫做高阶函数；

**函数是一等对象；**

函数可以作为参数传递给其他函数；


```python 
In [45]: def sort(lst,cmp=None,reverse=False):
    ...:     def default_cmp(a,b):
    ...:         if a > b:
    ...:             return 1
    ...:         if a == b:
    ...:             return 0
    ...:         if a < b:
    ...:             return -1
    ...:     if cmp is None:
    ...:         cmp = default_cmp   # 函数是一等对象的一个体现；
    ...:     dst = []
    ...:     for n in lst:
    ...:         for i,e in enumerate(dst):
    ...:             if not reverse:
    ...:                 if cmp(n,e) < 0:
    ...:                     dst.insert(i,n)
    ...:                     break
    ...:             else:
    ...:                 if cmp(n,e) > 0:
    ...:                     dst.insert(i,n)
    ...:                     break
    ...:         else:
    ...:             dst.append(n)
    ...:     return dst
    ...: 

In [46]: sort([3,7,2,9,85,4,1,6,])
Out[46]: [1, 2, 3, 4, 6, 7, 9, 85]

```


**闭包：**一个函数引用了它上一级作用域的变量，当上一级作用域被回收时，它依然存在；

```python 
# 函数可以作为返回值返回；
In [47]: def make_counter(init):
    ...:     counter = [init]
    ...:     def inc():
    ...:         counter[0] += 1
    ...:     def dec():
    ...:         counter[0] -= 1
    ...:     def get():
    ...:         return counter[0]
    ...:     def reset():
    ...:         counter[0] = init
    ...:     return inc,dec,get,reset
    ...: 

In [48]: inc,dec,get,reset = make_counter(0)

In [49]: inc()

In [50]: get()
Out[50]: 1

In [51]: dec()

In [52]: inc()

In [53]: inc()

In [54]: inc()

In [55]: get()
Out[55]: 3
```


* 参数是函数；
* 返回值是函数；

满足以上两点任意一点的函数，称之为高阶函数；


```python 
# python 3中的闭包；
# 函数作为返回值；

In [60]: def make_counter(init=0):
    ...:     counter = init
    ...:     def inc():
    ...:         nonlocal counter 
    # nonlocal 类似于global，声明此处使用的变量counter是上一级作用域内的；
    ...:         counter += 1
    ...:     def dec():
    ...:         nonlocal counter # nonlocal关键字标记一个变量有他的上级作用域定义，通过nonlocal定义的变量，可读可写；
    ...:         counter -= 1     # 如果上级每页定义此变量的话，会抛出语法错误；
    ...:     def get():
    ...:         nonlocal counter
    ...:         return counter
    ...:     def reset():
    ...:         nonlocal counter
    ...:         counter = init
    ...:     return inc,dec,get,reset
    ...: 
# 多个函数共享一个变量；

In [61]: inc,dec,get,reset = make_counter(0)

In [62]: inc()

In [63]: get()
Out[63]: 1

In [64]: inc()

In [65]: get()
Out[65]: 2

In [66]: dec()

In [67]: get()
Out[67]: 1

In [68]: dec()

In [69]: get()
Out[69]: 0

In [70]: inc()

In [71]: inc()

In [72]: get()
Out[72]: 2

In [73]: reset()

In [74]: get()
Out[74]: 0
```

```python 
In [12]: def counter(): # 闭包：函数已经结束，但是函数内部不能分变量的引用还存在；
    ...:     c = [0]    # python的闭包可以用可变容器实现，这也是py2唯一的方式；
    ...:     def inc():
    ...:         c[0] += 1
    ...:         return c[0]
    ...:     return inc
    ...: 

In [13]: f = counter()

In [14]: f()
Out[14]: 1

In [15]: f()
Out[15]: 2

In [16]: f()
Out[16]: 3

In [17]: f = counter()

In [18]: f()
Out[18]: 1

In [19]: f()
Out[19]: 2
```

---


**偏函数：**

```python 
from functools import partial

partial(func, *args, **keywords) - new function with partial application
 |  of the given arguments and keywords.

# 将传入的函数的部分参数固定下来；
In [3]: help(int)


In [4]: hex_to_int = partial(int,base=16)  # 将int函数的参数：base固定为16；

In [5]: hex_to_int('0xAAAA')
Out[5]: 43690
```

```python 
# 库提供者为了通用性，提供了默认参数；
In [11]: def connect(host='127.0.0.1',port=3306,username='sslinux',password='1qaz2wsx'):
    ...:     pass
    ...: 

# 企业在生产环境中都修改了端口，为程序方便，将其固化下来；
In [12]: myconnect = partial(connect,port=3307)

In [13]: myconnect()
```


**柯里化：**

```python 
In [6]: def add(x,y):
   ...:     return x + y
   ...: 

In [8]: def add(x):
   ...:     def add(y):
   ...:         return x + y
   ...:     return add
   ...: 

In [9]: add(3)(5)
Out[9]: 8
```

f(x,y,z) => g(x)(y)(z)




---
---

## 匿名函数：

lambda params : expr

* 只能写在一样上；
* 表达式的结果就是返回值；


```python 
In [14]: lambda x,y: x+y
Out[14]: <function __main__.<lambda>>

In [15]: add = lambda x,y: x+y

In [16]: add(3,5)
Out[16]: 8
```

```python
In [17]: lambda x,y=1: x+y   # 匿名函数的参数也可以有默认值；
Out[17]: <function __main__.<lambda>>

In [18]: add = lambda x,y=1: x+y

In [21]: add(x=5)    # 调用匿名函数是也可以传递关键字参数；
Out[21]: 6

In [22]: add(5)
Out[22]: 6
```

```python 
In [23]: f = lambda *x: x   # lambda也支持可变位置参数；

In [24]: f(1,2,3)
Out[24]: (1, 2, 3)

In [25]: f = lambda **kw: kw  # 支持可变关键字参数；

In [26]: f(a=0)
Out[26]: {'a': 0}

In [27]: d = {'a':0,'b':1,'c':2} 

In [28]: f(**d)
Out[28]: {'a': 0, 'b': 1, 'c': 2}    # 支持可变关键字参数解包；

In [29]: f = lambda x,*,y: x+y       # 支持参数槽；

In [30]: f(1,y=3)
Out[30]: 4
```

```python 
In [31]: concat = lambda *args: ''.join(args)

In [32]: concat('a','b','c')
Out[32]: 'abc'
```

### lambda弱点：只能有一个表达式；

* 应用场景：

        匿名函数通常和高阶函数配合使用，作为参数传入、或者作为返回值返回；



**匿名函数最好不要定义成递归函数。**
```python 
In [35]: fib = lambda n: 1 if n == 0 or n == 1 else fib(n-1) + fib(n-2)

In [36]: fib(5)
Out[36]: 8

In [38]: fib(1000)
---------------------------------------------------------------------------
RecursionError                            Traceback (most recent call last)
<ipython-input-38-0034b0f1a990> in <module>()
----> 1 fib(1000)

<ipython-input-35-47ac903ec519> in <lambda>(n)
----> 1 fib = lambda n: 1 if n == 0 or n == 1 else fib(n-1) + fib(n-2)

... last 1 frames repeated, from the frame below ...

<ipython-input-35-47ac903ec519> in <lambda>(n)
----> 1 fib = lambda n: 1 if n == 0 or n == 1 else fib(n-1) + fib(n-2)

RecursionError: maximum recursion depth exceeded in comparison
```

# 匿名函数

```python 
In [1]: lambda x: x + 1
Out[1]: <function __main__.<lambda>>
```

* lambda来定义
* 参数列表不需要用小括号 
* 冒号不是用来开启新语句块
* 没有return，最后一个表达式的值即返回值；

```python
In [5]: (lambda x: x + 1)(3)   #第一对括号用来改变优先级，第二对括号表示函数调用
   ...: 
Out[5]: 4
```

```python
In [6]: inc = lambda x: x + 1

In [7]: inc(2)
Out[7]: 3

In [8]: inc(3)
Out[8]: 4

In [9]: type(inc)
Out[9]: function
```


匿名函数(lambda)只能写在一行上，所以也有人叫它单行函数；

```python
In [14]: (lambda :0)()   # 匿名函数可以没有参数；
Out[14]: 0

In [15]: (lambda x,y: x+y)(3,5)  # 可以接受多个参数；
Out[15]: 8

In [16]: (lambda x,y=3: x+y)(5)  # 可以有默认参数；
Out[16]: 8

In [17]: (lambda *args: args)(*range(3))   # 可以有可变位置参数；
Out[17]: (0, 1, 2)

# 可以有可变位置参数和可变关键字参数；
In [19]: (lambda *args,**kwargs: print(args,kwargs))(*range(3),**{str(x):x for x in range(3)})
(0, 1, 2) {'0': 0, '1': 1, '2': 2}

# 也可以有keyword-only参数；
In [20]: (lambda *,x: x)(x=3)
Out[20]: 3
```

应用场景：构建简单函数作为参数传递给高阶函数：

    匿名函数通常用于高阶函数的参数，当此函数非常短小的时候，就适合使用匿名函数；

高阶函数：

* sorted
* map
* filter


```python
In [22]: from collections import namedtuple

In [23]: User = namedtuple('User',['name','age'])

In [24]: users = {User('comyn',18),User('paggy',16),User('tom',32)}

In [25]: def get_age(user):
    ...:     return user.age
    ...: 

In [26]: sorted(users,key=get_age)
Out[26]: 
[User(name='paggy', age=16),
 User(name='comyn', age=18),
 User(name='tom', age=32)]

In [27]: sorted(users,key=lambda x: x.age)
Out[27]: 
[User(name='paggy', age=16),
 User(name='comyn', age=18),
 User(name='tom', age=32)]
```

```python
In [28]: list(map(lambda x: x.age,users))
Out[28]: [16, 32, 18]

In [29]: list(filter(lambda x: x.age < 30,users))
Out[29]: [User(name='paggy', age=16), User(name='comyn', age=18)]
```

```python
# map和filter函数的原型：
In [30]: def map_(fn,it):
    ...:     return (fn(x) for x in it)
    ...: 

In [31]: def filter_(fn,it):
    ...:     return (x for x in it if fn(x))
    ...: 
```

---
---


## 装饰器：

例子：

```python 
In [39]: import time

In [40]: def sleep(n):
    ...:     time.sleep(n)
    ...:     

In [44]: start = time.time();sleep(3);time.time()-start
Out[44]: 3.0039782524108887
```

```python 
In [45]: def timeit(fn,*args,**kwargs):  # 接收一个函数参数和若干个位置参数和若干个关键字参数；
    ...:     start = time.time()
    ...:     ret = fn(*args,**kwargs)
    ...:     print(time.time() - start)  # 统计函数执行的时间；
    ...:     return ret
    ...: 

In [46]: timeit(sleep,3)  # 发生在调用的时候；
3.0038766860961914
```

```python 
In [48]: def timeit(fn):   # 定义装饰器；
    ...:     def wrap(*args,**kwargs):    # 定义：可变参数；
    ...:         start = time.time()
    ...:         ret = fn(*args,**kwargs)  # 调用：可变参数解构；
    ...:         print(time.time() - start)
    ...:         return ret
    ...:     return wrap
    ...: 

In [49]: fn = timeit(sleep)   # 可以提前定义好；

In [50]: fn(3)
3.003540277481079


In [51]: @timeit             # 使用装饰器；  等效于：fn = timeit(fn)
    ...: def fn(n):
    ...:         time.sleep(n)
    ...:         return n
    ...: 

In [52]: fn(3)
3.003883123397827
Out[52]: 3

```

装饰器的本质是函数，接收一个**函数作为参数**，**并且返回一个函数；**

装饰器通常会返回一个封装函数，这个封装函数在传入的函数前后做一些事情；

装饰器肯定是高阶函数；


装饰器所装饰的函数即是装饰器所接受的参数；


```python 
@timeit               # 个人理解：@timeit 相当于把后边定义的函数fun()当作参数传递给了timeit；
                      # 并将timeit函数的返回值赋值给fun;
def fun(x):
    time.sleep(x)
    return x

-----二者等效---

def fun(x):
    time.sleep(x)
    return x

fun = timeit(fun)
左边的fun是接收timeit的返回值的变量，返回值是一个函数；
右边的fun是前面刚定义的函数fun，作为参数传递给timeit；

```

f(3) => timeit(fun)(3) => wrap(3) => fun(3) 

![装饰器理解](images/装饰器理解.png)


```python 
In [56]: def timeit(fn):
    ...:     def wrap(*args,**kwargs):
    ...:         start = time.time()
    ...:         ret = fn(*args,**kwargs)
    ...:         print(time.time() - start)
    ...:         return ret
    ...:     wrap.__name__ = fn.__name__    # 手动还原函数的属性；
    ...:     return wrap
    ...: 

In [57]: @timeit
    ...: def fun(x):
    ...:     pass
    ...: 

In [58]: fun.__name__
Out[58]: 'fun'
```

```python 
In [59]: from functools import wraps

In [60]: def timeit(fn):
    ...:     @wraps(fn)    # 保持原函数的属性；
    ...:     def wrap(*args,**kwargs):
    ...:         start = time.time()
    ...:         ret = fn(*args,**kwargs)
    ...:         print(time.time() - start)
    ...:         return ret
    ...:     return wrap
    ...:     
    ...: 

In [61]: @timeit
    ...: def add(x,y):
    ...:     '''x + y'''
    ...:     return x + y
    ...: 

In [62]: add.__name__
Out[62]: 'add'

In [63]: add.__doc__
Out[63]: 'x + y'
```

## 带参数的装饰器：
```python
def timeit(fn):
    @wraps(fn)
    def wrap(*args,**kwargs):
        start = time.time()
        ret = fn(*args,**kwargs)
        print(time.time() - start)
        return ret 
    return wrap 
```

```python 
@timeit 
def add(x,y):
    '''x + y'''
    return x + y
```

```python 
def timeit(cpu_time=False):
    time_func = time.clock if cpu_time else time.time
    def dec(fn):
        @wraps(fn)
        def wrap(*args,**kwargs):
            start = time_func()
            ret = fn(*args,**kwargs)
            print(time_func() - start)
            return ret
        return wrap 
    return dec 
```

```python 
def fun(n):
    time.sleep(n)
    return n
fun = timeit()(fun)
```

```python 
@time()
def fun(n):
    time.sleep(n)
    return n

fun(3)
```

带参数的装饰器是一个函数，**返回一个装饰器；**


带参数的装饰器最多允许一层；


```python
@a
@b
@c 
def fn():
    pass

相当于：
a(b(c(fn)))
```


面向过程编程告一段落；












