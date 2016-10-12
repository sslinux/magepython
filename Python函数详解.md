# Python函数详解

函数是Python为了代码最大程度地重用和最小化代码冗余而提供的基本程序结构；

函数是一种设计工具，它能让程序员将复杂的系统分解为可管理的部件；

函数用于将相关功能打包并参数化；

在Python中可以创建4种函数：
	全局函数：定义在模块中；

	局部函数：嵌套于其他函数中；

	lambda函数：表达式；可以出现任何表达式可出现的位置；

	方法：与特定数据类型关联的函数，并且只能与数据类型关联一起使用，
			也就是定义在类中的函数；

Python提供了很多内置函数，例如：help(),type(),len(),int(),str()等；

函数和过程的区别：
	函数应该由return返回，python中返回的是对象，默认返回空对象；

语法：
	def functionName(parameters):
	    suite

一些相关的概念：
	def是一个可执行语句
		因此可以出现在任何能够使用语句的地方，甚至可以嵌套与其他语句；例如if或while中；
	def创建类一个对象并将其赋值给一个变量名(即函数名)
	return用于返回结果对象，其为可选，无return语句的函数自动返回None对象；
		返回多个值是彼此间使用逗号分隔，其组合为元组形式返回一个对象；；
	def语句运行之后，可以在程序中通过函数后附加括号进行调用；

```python
In [2]: def printName():
   ...:     print("Hello")
   ...:     

In [3]: printName()
Hello         # 此为函数的输出，并非返回值；
```

独特的pass语句，占位，后面再补充；
```python
def testFunc():
    pass

testFunc()
```

函数的作用域，函数的使用会导致变量有了作用域；

名称空间：/作用域；
	一个变量所能生效的范围；

变量名解析：
	函数：本地作用域；函数调用结束后，本地变量也就失效了；
	模块：全局作用域；仅限于单个文件；

```python
#!/usr/bin/python3

x = 32

def f1():
    x = 43    # 同名函数，函数内定义的将覆盖全局的；
    print(x)

f1()

print(x)
```

函数内部使用跟全局变量同名的变量，其实是定义了一个局部变量；
函数内部可以读取读取全局变量，但若要改变全局变量则要使用global关键字；
```python
#!/usr/bin/python3

x = 32

def f1():
    global x
    x = 43

    print(x)

f1()

print(x)
```
应该尽量避免在函数中修改全局变量；

### 函数作用域：
Python创建、改变或查找变量名都是在名称空间中进行；
在代码中变量名被赋值的位置决定了其能被访问到的范围；
函数定义了本地作用域，而模块定义了全局作用域；
	每个模块都是一个全局作用域，因此，全局作用域的范围仅限于单个程序文件；
	每次对函数的调用都会创建一个新的本地作用域，赋值的变量除非声明为全局变量，否则均为本地变量；
	所有的变量名都可以归纳为本地、全局和内置的(有__builtin__模块提供).

# 变量名解析：LEGB原则：
变量名引用分三个作用域进行：首先是本地、之后是函数内、接着是全局、最后是内置；

![LEGB](/images/LEGB.png)

作用域越小，优先级越高；

例子：
```python
sslinux@sslinux-pygo:~$ cat tes1.py 
#!/usr/bin/env python3
# 

x = 6
z = "global"

def f1():
    x = "from f1"
    y = 3
    print(x,z)

    def f2():
        x = "from f2"
        print(x,y,z)   # f2函数中没有y、z，则在上一层函数f1中找，如果f1中也没有，则在模块的全局变量中找；
    f2()

print(x)

f1()
```
```bash
sslinux@sslinux-pygo:~$ python tes1.py
6
('from f1', 'global')
('from f2', 3, 'global')
```

函数闭合：工厂函数；python闭包
```python
In [7]: def f1():
   ...:     x = 3
   ...:     def f2():               # 函数嵌套；
   ...:         y = "hello"
   ...:         print(x,y)
   ...:     return f2               # 调用f1时，返回的结果是一个函数：f2
   ...: 

In [8]: f1()						
Out[8]: <function __main__.f1.<locals>.f2>

In [9]: a1 = f1()                  # 将函数f1的返回值赋值给a1，即相当于将函数f2取了个别名叫a1；

In [10]: type(a1)  				   # a1 的类型为function；
Out[10]: function

In [11]: a1()                      # 通过名称对象a1调用函数f2；
3 hello
```

闭包（Closure）是词法闭包（Lexical Closure）的简称，是引用了自由变量的函数。这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。所以，有另一种说法认为闭包是由函数和与其相关的引用环境组合而成的实体。

### 函数参数：
def funcName(arg1,arg2,...):
    print(arg1,arg2,...)

funcName(arg1,arg2,...)

def f2(x,y):
    print(x+y)

f2(3,4)
f2('hello ','world')

m =3 ; n = 4
def f3(x,y):
    x -= 1
    print(x,y)
f3(m,n)        # 
print(m,n)


```python
In [12]: l1 = [1,2,3]

In [14]: def f4(x):
    ...:     x.pop()      # 因为列表是可变对象，所以会在原处修改；
    ...:     print(x)
    ...:     

In [15]: f4(l1)   # 传入的是一个列表，列表是可变对象；相当于浅复制；
[1, 2]

In [16]: print(l1)   # l1 已经被函数f4修改了；
[1, 2]
```
### 建议：
	尽量不要在函数中修改调用该函数时传递过来的可变对象；

```python
In [17]: l1 = [1,2,3]

In [18]: def f5(x):
    ...:     x.pop()
    ...:     print(x)
    ...:     

In [19]: f5(l1[:])     # 切片操作，生成的是一个新的对象，这样f5函数的修改操作不会影响l1对象；
[1, 2]

In [20]: print(l1)    # 我还是原来的我；
[1, 2, 3]
```

在python中，函数调用传递参数时，若传递的参数是可变对象，函数的修改操作会影响原对象的值；
若传递的参数是不可变对象，则函数的修改操作不会影响原对象的值；
因此，建议在向包含修改操作的函数传参数时，若参数是可变对象，应该使用深复制的方式，或生成新的对象来传递；

### 参数传递：
有两种方式可避免可变参数被函数修改：
	直接传递可变对象的副本，testFunc(A,B[:])
	在函数内部创建可变参数的副本：B = B[:]
```python
In [21]: l = [1,2,3,4]

In [22]: def changer(X):
    ...:     X[2] += 10
    ...:     return X
    ...: 

In [23]: changer(l)
Out[23]: [1, 2, 13, 4]

In [25]: print(l)    # 可变参数已经被修改；
[1, 2, 13, 4]
```	

```python
In [28]: L = [1,2,3,4]

In [29]: def changer(X):
    ...:     X[2] += 10
    ...:     return X
    ...:     
    ...: 

In [30]: changer(L[:])    # 因为传递的是副本，所以L不会被修改；
Out[30]: [1, 2, 13, 4]

In [31]: print(L)
[1, 2, 3, 4]

```

### 参数匹配模型：
默认情况下，参数通过其位置进行传递，从左至右，这意味着，必须精确地传递和函数头部参数一样多的参数；

但也可以通过关键字参数、默认参数或参数容器等改变这种机制；
	位置：从左至右；
	关键字参数：使用"name=value"的语法通过参数名进行匹配；
	默认参数：定义函数时使用"name=value"的语法直接给变量一个值，从而传入的值可以少于参数个数；
	**可变参数**：定义函数时使用*开头的参数，可用于收集任意多基于位置或关键字的参数；
	可变参数解包：调用函数时，使用*开头的参数，可用于将参数集合打散，从而传递任意多基于位置或关键字的参数；

```python
In [34]: def f6(x,y):        # 定义时有两个参数；
    ...:     print(x,y)
    ...:     

In [35]: f6(m,n,8)           # 传递的参数个数，需要与定义时的参数个数一致；
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-35-4db70ef07432> in <module>()
----> 1 f6(m,n,8)

TypeError: f6() takes 2 positional arguments but 3 were given

In [36]: print(m,n)          
3 4
# 传递的参数，位置与定义参数时一致；
In [37]: print(n,8)
4 8
```

```python
In [34]: def f6(x,y):        # 定义时有两个参数；
    ...:     print(x,y)
    ...:     

In [38]: f6(x=m,y=n)     # 使用关键字参数时，则可以忽略自左至右的顺序；
3 4

In [39]: f6(y=n,x=m)
3 4
```

参数传递形式：
	位置参数：从左向右；
	关键字参数：按关键名称匹配；
	定义时默认参数：有默认值的参数；
		混用有默认值和无默认值的参数时，无默认值的放前面；

```python
In [40]: m = 3 ; n = 4 ; o = 7

In [41]: def f7(x,y,z):
    ...:     print(x,y,z)
    ...:     

In [42]: f7(m,n,o)
3 4 7

In [43]: f7(x=m,y=n,z=o)
3 4 7

In [44]: f7(m,y=n,z=o)
3 4 7

In [45]: f7(m,z=o,y=n)
3 4 7

In [46]: f7(z=o,y=n,m)    # 混用位置参数和关键字参数时，位置参数在前，关键字参数在后；
  File "<ipython-input-46-f8a8c567d77a>", line 1
    f7(z=o,y=n,m)
              ^
SyntaxError: positional argument follows keyword argument  # 位置参数在关键字参数后了，错了；
```

混用位置参数和关键字参数时：所有位置参数，所有的关键字参数；

#### 默认参数：
```python
In [47]: m = 3 ; n = 4 ; o = 7

In [48]: def f8(x,y,z=9):    # 定义函数时，给z定义了默认值；
    ...:     print(x,y,z)
    ...:     

In [49]: f8(m,n,o)     # 若给z传递了值，则使用传递过来的值o
3 4 7

In [50]: f8(m,n)       # 未传递参数给z，所以z使用自己的默认值；
3 4 9

In [51]: f8(m)         # 参数个数不匹配
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-51-7d2733874ff5> in <module>()
----> 1 f8(m)

TypeError: f8() missing 1 required positional argument: 'y'   # 缺少一个位置参数'y'
```


**可变参数**：定义函数时使用*开头的参数，可用于收集任意多基于位置或关键字的参数；
```python
In [52]: def f10(*x):     # 定义了可变参数；
    ...:     print(x)
    ...:     

In [53]: f10(m)            # 传递了一个位置参数；
(3,)

In [54]: f10(m,n)          # 传递了两个位置参数；
(3, 4)

In [55]: f10(m,n,o)        # 传递了三个位置参数；
(3, 4, 7)

In [56]: f10(m,n,9)
(3, 4, 9)

In [57]: f10(m,n,z=9)      # 传递了两个位置参数和一个关键字参数；
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-57-1f491f997557> in <module>()
----> 1 f10(m,n,z=9)

TypeError: f10() got an unexpected keyword argument 'z'   
# 此处将传递过来的关键字参数z识别为字典了；
```

调用函数时使用可变参数要求：
	定义函数时使用*，收集位置函数；
	定义函数时使用**，收集关键字参数；

```python
In [60]: def f11(**x):   # 定义函数是使用**，收集关键字函数；
    ...:     print(x)
    ...:     

In [61]: f11(x=1,y=2,z=9)
{'y': 2, 'z': 9, 'x': 1}
```

```python
In [62]: def f12(x,*y):			# 混用位置参数和可变参数
    ...:     print(x,y)         
    ...:     

In [63]: f12(m,n,o)             # 收集到的可变参数，表现为一个元组；
3 (4, 7)

In [64]: def f13(*x,y): 		# 可变参数在位置参数前面；在python2版本中，定义时就会报错；
    ...:     print(x,y)			# 此处是python3，居然没报错；
    ...:     

In [65]: f13(m,n,10)            # 但python3 也在调用时报错了
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-65-ba88835e308b> in <module>()
----> 1 f13(m,n,10)

TypeError: f13() missing 1 required keyword-only argument: 'y'
# 缺少一个关键字参数'y'？

In [66]: f13(m,n,10,y=9)   
# 原来在python3中，若可变参数在前面的话，其后的只能是关键字参数，不能是位置参数；
(3, 4, 10) 9

```

```python
In [67]: def f14(x,y=10,*z):
    ...:     print(x)
    ...:     print(y)
    ...:     print(z)
    ...:     

In [68]: f14(m,n,o)     # 因为是自左至右的匹配，所以n匹配给了y；
3
4
(7,)
```

```python
# 混用 * 和 **
In [69]: def f15(*x,**y):
    ...:     print(x)
    ...:     print(y)
    ...:     

In [70]: f15(m,n,o,i=3,j=6)
(3, 4, 7)                    # * 收集了位置参数；
{'j': 6, 'i': 3}             # ** 收集类关键字参数；
```


### 可变参数解包：调用函数时，使用*开头的参数，可用于将参数集合打散，从而传递任意多基于位置或关键字的参数；也可称为参数分解；

```python
# 分解赋值；
In [71]: l1 = ['Sun','Mon','Tus']

In [72]: x,y,z = l1      # 将l1中的所有元素一一对应的赋值给=前面的三个变量，前后数量必须一致；

In [73]: print(x,y,z)
Sun Mon Tus

In [74]: print(x)
Sun

In [75]: print(y)
Mon

In [76]: print(z)
Tus
```

```python
# 可变参数解包，是分解赋值的另一种表现形式；
In [77]: def f17(x,y,z):
    ...:     print(x,y,z)
    ...:     

In [78]: f17(*l1)   # 调用时使用*号；将一个对象打散至函数中的各个变量；
Sun Mon Tus

In [79]: l2 = ['a','b','c','d']

In [80]: f17(*l2)    
# 可变参数解包时，定义函数是参数的个数必须与调用时所传递的随想能分解出来的元素个数一致；
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-80-11c8d83d4d4d> in <module>()
----> 1 f17(*l2)

TypeError: f17() takes 3 positional arguments but 4 were given

# 只给两个参数：
In [81]: l3 = ['a','b']

In [83]: f17(*l3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-83-2be8b96b22ad> in <module>()
----> 1 f17(*l3)

TypeError: f17() missing 1 required positional argument: 'z'
# 报错说：缺少一个位置参数'z'

In [84]: f17(m,*l3)     # 函数调用时，也可以使用位置参数，关键字参数和参数解包的形式；
3 a b

```

#### 可变参数解包时，要求定义时与调用时，参数个数必须一致；这样不容易控制；
定义时使用*，调用时也使用* ：

```python
In [85]: def f18(x,*y):
    ...:     print(x)
    ...:     print(y)
    ...:     

In [86]: f18(m,*13)   # 手误写成了数字13
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-86-64503ea71e5d> in <module>()
----> 1 f18(m,*13)

TypeError: f18() argument after * must be an iterable, not int
# 错误： f18()函数*号后面的参数必须是一个可迭代对象，不能是整数；

In [87]: f18(m,*l3)          # 正确调用；m传递给了x，*l3(前文中定义的列表L3)
3
('a', 'b')					# 使用*L3传递的可迭代对象，在函数中被组合成了一个元组；
```

#### 函数调用时，也可以使用**传递任意关键字参数；
```python
In [88]: d1 = {'key1':'v1','key2':'v2','key3':77}

In [89]: def f19(x,*y,**z):
    ...:     print(x)
    ...:     print(y)
    ...:     print(z)
    ...:     

In [90]: f19(m,*l3,**d1)        # 无论定义函数调用，都需要按照{位置、任意位置、任意关键字}的顺序；
3                      # 位置参数；
('a', 'b')             # 任意位置参数；
{'key3': 77, 'key1': 'v1', 'key2': 'v2'}      # 任意关键字参数；

In [91]: f19(m,n,o,**d1)   # 定义时使用任意位置参数，调用时不使用；
3
(4, 7)
{'key3': 77, 'key1': 'v1', 'key2': 'v2'}

In [92]: f19(m,n,o,key1='v1',key2='v2')    
# 定义时使用了任意关键字参数，调用时直接传递关键字参数也是可以的；
3
(4, 7)
{'key1': 'v1', 'key2': 'v2'}

```

### 匿名函数：
