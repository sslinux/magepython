# Python迭代器、列表解析及生成器


sys.getrefcount() 获取对象引用计数；

 #### 动态语言：
- 增加对象的引用计数：
    - 变量名创建并指向对象时，赋值；
    - 将对象添加进容器时；类似list.append()
    - 当对象被当作参数传递给函数时；
    - 多重目标赋值(为对象创建另外的变量名)：s1 = 'abc'   s4 = s3

- 减少对象的引用次数：
    - 引用此对象的变量名被显式销毁： del x
    - 引用此对象的某变量名重新赋值；
    - 从容器中移除对象时，类似list.pop()
    - 容器本身被销毁；容器中所有引用的对象的引用计数减少；

2、if：

```python
if boolean_expression:
   if_suit
elif boolean_expression:
   suit2...
....
else:
   suit X
```

3、while
```python
while boolean_expression:
    while_suite
    if boolean_expression2: continue
    if boolean_expression3: break
else:
    else_suite
```
4、 for:
```python
for expression in object:
    for_suit
    if boolean_expression2: continue
    if boolean_expression3: break
else:
    else_suite
```

```python
In [42]:
In [50]: d1 = {'x':123,'y':321,'z':734}

In [53]: for (k,v) in d1.items():
    ...:     print(k,v)
    ...:
z 734
y 321
x 123
```
非完备迭代：
```python
for in range(1,len(l1),2):
    print(l1[i])
```
```python
l1 = [1,3,4,6,9]
l2 = [2,3,5,8,9]

l3 = []
for i in l1:
    if i not in l2:
       l3.append(i)
```

完备遍历：for。

非完备遍历： 使用非完全索引的方式来遍历；

#### python迭代：

迭代：重复做一件事

iterable(可迭代)对象；
```python
	支持每次返回自己所包含的一个成员的对象；
	对象实现类__iter__方法
		序列类型：如:list,str,tuple
		非序列类型：如:dict,file
		用户自定义的一些包含了__iter__()或__getitem__()方法的类;
```

```python
list.__iter__()
i1 = l1.__iter__()
i1.next()
```
- 迭代器(iterator)又称游标(cursor)，它是程序设计的软件设计模式，是一种可在容器物件(container,如列表等)上实现元素遍历的接口；

- 迭代器是一种特殊的数据结构，当然在python中，它也是以对象的形式存在的；

- 简单理解方式：对于一个集体中的每一个元素，想要执行遍历，那么针对这个集体的迭代器定义类遍历集体中每一个元素的顺序或者方法；

- 创建迭代器：
```python
	l1 = [1,2,3,4,5,6,7]    # l1 可以是其他类型的可迭代对象；
	i2 = l1.__iter__()      # 通过对象的内置方法；
	i3 = iter(l1)           # iter()函数也是调用对象的__iter__()方法生成的迭代器；
```
for循环中无需手动创建迭代器，因为for可以自动实现对可迭代对象的迭代；


### 迭代器：
- 在python中，迭代器是遵循迭代协议的对象；
- 使用iter()可从任何序列对象中得到迭代器；
- 若要实现迭代器，需要在类中定义next()方法(Python 3中是__next__())
- 要使得迭代器指向下一个元素，则使用成员函数next(),

	在python中，是函数next(),而非成员函数；
- 当没有元素时，则引发StopIteration异常；

- for循环可用于任何可迭代对象；
	for循环开始时，会通过迭代协议传递给iter()内置函数，从而能够从可迭代对象中获得一个迭代器，返回的对象含有需要的next方法；


### python的列表解析：
列表解析是python迭代机制的一种应用，它常用于实现创建新的列表，因此要放置于[]中；

语法：
```python
	[expression for iter_var in iterable]
	[expression for iter_var in iterable if cond_expr]
```

```python
In [58]: l1 = [1,2,3,4,5]

In [59]: l2 = []

In [60]: for i in l1:
    ...:     l2.append(i**2)
    ...:

In [61]: print(l2)
[1, 4, 9, 16, 25]
```

列表解析根据已有列表，高效生成新列表的方式就是列表解析；
```python
l3 = [i**2 for i in l1]   # 比上述通过for完成的要高效；

l4 = [i ** 2 for i in l1 if i >= 3]
```

```python
In [66]: for i in [ i**2 for i in range(1,11) ]: print(i/2)
0.5
2.0
4.5
8.0
12.5
18.0
24.5
32.0
40.5
50.0
```

```python
In [67]: for i in [ i**2 for i in range(1,11) if i % 2 == 0 ]: print(i/2)
2.0
8.0
18.0
32.0
50.0
```

Example:
```python
import os

log_list = [ i for i in os.listdir('/var/log') if i.endswith('.log') ]
print(log_list)

```

```python
In [71]: l1 = ['x','y','z']

In [72]: l2 = [1,2,3]

In [73]: l3 = [ (i,j) for i in l1 for j in l2 ]


In [75]: print(l3)
[('x', 1), ('x', 2), ('x', 3), ('y', 1), ('y', 2), ('y', 3), ('z', 1), ('z', 2),
 ('z', 3)]
```

l3 = [ (i,j) for i in l1 for j in l2 if j != 1 ]


#### 生成器：
生成器表达式并不真正创建数字列表，而是返回一个生成器对象，此对象在每次计算出一个条目后，把这个条目"产生"(yield)出来；
```
	生成器表达式使用类"惰性计算"或称作"延迟求值"的机制；
        序列过长，并且每次只需要获取一个元素时，应当考虑使用生成器表达式而不是列表解析；
	生成器表达式于python2.4引入；
```
语法：
```python
	(expression for iter_ver in iterable)
	(expression for iter_var in iterable if cond_expr)
```

```python
[ i**2 for i in range(1,11) ]   # 列表解析；

g1 = ( i ** 2 for i in range(1,11) )    # 生成器表达式；
g1.next()
g1.next()
```

```python
In [78]: for j in (i**2 for i in range(1,11)): print(j/2)
0.5
2.0
4.5
8.0
12.5
18.0
24.5
32.0
40.5
50.0
```

### 产生偏移和元素：
enumerate：
	range可在非完备遍历中用于生成索引偏移，而非偏移处的元素；
	如果同时需要偏移索引和偏移元素，则可以使用enumerate()函数；
	此内置函数返回一个生成器对象；
```python
In [83]: url = 'www.sslinux.com'

In [84]: enumerate(url)
Out[84]: <enumerate at 0x46ba3a0>

In [85]: g1 = enumerate(url)

In [86]: g1.next()    # python 3.5中，调用next()方法报错，python2.7中正常；
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-86-9066a8f18086> in <module>()
----> 1 g1.next()

AttributeError: 'enumerate' object has no attribute 'next'

In [87]: g1.__next__()    # python2.7中可以直接使用g1.next()方法；
Out[87]: (0, 'w')

In [88]: g1.__next__()
Out[88]: (1, 'w')

In [89]: g1.__next__()
Out[89]: (2, 'w')

In [90]: g1.__next__()
Out[90]: (3, '.')

In [91]: g1.__next__()
Out[91]: (4, 's')
```	

[Blog:Python语言中的各种器具](BlogPython语言中的各种器具.md)