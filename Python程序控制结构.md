# Python程序控制结构

流程控制：


### Python的比较操作：
所有的Python对象都支持比较操作：
	可用于测试相等性、相对大小等；
	如果是复合对象，python会检查其所有部分，包括自动遍历各级嵌套的对象，知道可以得出最终结果；

测试操作符：
	"=="操作符测试值的相等性；
	"is"表达式测试对象的一致性；

python中不同类型的比较方法：
	数字：通过相对大小进行比较；
	字符串：按照字典次序逐字符进行比较；
	列表和元组：自左至右比较个部分内容；
	字典：对排序之后的(键、值)列表进行比较；

python中真和假的含义：
	1、任何非0数字和非空对象都为真；
	2、数字0、空对象和特殊对象均为假；
	3、比较和相等测试会递归应用到数据结构中；
	4、返回值为True或False；

	非零数字为真，否则为假；
	非空对象为真，否则为假；
	None则始终为假；

组合条件测试：
	and：逻辑与；短路与；
	or：或运算；
	not：非运算；返回True或False

注意：
	Python中，and和or运算会返回真或加的对象，而不是True或False；

	对象在本质上不是"真",就是"假"
and和or是短路操作符；


条件测试：

if测试的语法结构：
```
if boolean_expression1:
    suit1
elif boolean_expression2:
    suite2
...
else:
    else_suite
```
elif语句是可选的，仅用于占位，而后再填充相关语句时，可以使用pass；

```
x = 1 
y = 2
if x > y:
    print "the max number is %d." % x
else:
    print "the max nuber is %d." % y
```

if三元表达式：
	A = X if Y else z   
	<==>     
	if Y:
	    A = X
	else:
	    A = Z

格式：expression1 if boolean_expression else expression2
```python
In [1]: A = 7

In [2]: B = 9

In [3]: max = A if A > B else B

In [4]: print(max)
9
```

### while循环：
用于编写通用迭代结构；
顶端测试未真即会执行循环体，并会重复测试知道为假后执行循环后的其他语句；

for循环：
	一个通用的序列迭代器，用于遍历任何有序的序列对象内的元素；
	可用于字符串、元组、列表和其他的内置可迭代对象，以及通过类所创建的新对象；

python也提供类一些能够进行隐性迭代的工具：
	in成员关系测试；
	列表解析；
	map、reduce和filter函数；


while循环：
语法格式：

while boolean_expression:
    while_suite
else:
    else_suite  

else分支为可选部分；
只要boolean_expression的结果为True，循环就会执行；
boolean_expression的结果为False是终止循环，此时如果有else分支，则会执行；即：循环正常结束时执行else语句；

break: 跳出最内层的循环；
continue：跳到所处的最近曾循环的开始处；
pass：占位语句；
else代码块：循环正常终止才会执行；如果循环终止时break跳出导致的，则else不会执行；


```python
In [8]: url = 'www.sslinux.com'

In [9]: while url:
   ...:     print(url)
   ...:     url = url[1:]
   ...:
www.sslinux.com
ww.sslinux.com
w.sslinux.com
.sslinux.com
sslinux.com
slinux.com
linux.com
inux.com
nux.com
ux.com
x.com
.com
com
om
m

In [10]:
```

```python
In [15]: x = 0;y = 100

In [16]: while x < y:
    ...:     print(x)
    ...:     x += 1
    ...:
```


```python
In [17]: l1 = [1,2,3,4]
In [18]: count = 2

In [21]: while l1:
    ...:     print(l1[0])
    ...:     l1 = l1[1:]
    ...:
1
2
3
4
```
```python
In [22]: l1 = [1,2,3,4]

In [23]: while l1:
    ...:     print(l1[-1])
    ...:     l1.pop()
    ...:
4
3
2
1
```

死循环：
	while True:
		suite

for循环格式；

for expression1 in iterable:
    for suite
else:
    else_suite

通常，expression或是一个单独的变量，或是一个变狼序列，一般以元组的形式形式给出；

如果以元组或列表用于expression，则其中的每个数据项购汇拆分到表达式的项；

```python
In [24]: sum = 0

In [25]: for i in range(1,101):
    ...:     sum += i
    ...:

In [27]: print(sum)
5050
```

### for循环形式扩展：
语法格式：
for expression in iterable:
    for_suite
    if boolean_expression2: break
    if boolean_expression3: continue
else:
    else_suite

### 编写循环的技巧；
for循环比while循环执行速度快；
python提供类两个内置函数，用于在for循环中定制特殊的循环；
	range和xrange
		range：一次性地返回连续的整数列表；
		xrange：一次产生一个数据元素，相较于range更节约空间；
	zip：
		返回并行的元素元组的列表，常用于在for循环中遍历数个序列；

range函数：
非完备遍历：
	用于每隔一定的个数挑选一个元素；
```python
In [28]: S = 'How are you these days?'
In [30]: range(0,len(S),2)
Out[30]: range(0, 23, 2)
In [32]: for i in range(0,len(S),2):
    ...:     print(S[i])
    ...:
H
w
a
e
y
u
t
e
e
d
y
?
```

修改列表：
```python
In [33]: L = [1,2,3,4,5]

In [34]: for i in range(len(L)):
    ...:     L[i] += 1
    ...:

In [35]: print(L)
[2, 3, 4, 5, 6]
```


### 并行遍历：
zip:
取得一个或多个序列为参数，将给定序列中的并排的元素配成元组，返回这些元组的列表；
	当参数长度不同时，zip会以最短序列的长度为准；

可在for循环中用于实现并行迭代：
```python
In [42]: L1 = [1,2,3,4,5,6,7]

In [43]: L2 = ['a','b','c','d','e','f','g']

In [44]: zip(L1,L2)
Out[44]: <zip at 0x4719350>

python2中应该返回的是一个有元组构成的列表，如下：
[(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e'),(6,'f'),(7,'g')]

```

zip也常用语动态构造字典：
```python
In [45]: keys = [1,2,3,4,5,6,7]

In [46]: values = ['Mon','Tus','Wed','Thu','Fri','Sta','Sun']

In [47]: D = {}

In [48]: for (k,v) in zip(keys,values):
    ...:     D[k] = v
    ...:

In [49]: D
Out[49]: {1: 'Mon', 2: 'Tus', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sta', 7: 'Sun'}
```