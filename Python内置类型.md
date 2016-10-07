# Python内置类型

### Python对象的相关术语：
Python程序中保存的所有数据都是围绕**对象**这个概念展开的：
	程序中存储的所有数据都是对象；
	每个对象都有一个**身份**、一个**类型**和一个**值**；
		例如：school="MaGe Linux"会以"MaGe Linux"创建一个字符串对象，其身份是指向它咋ineicun中所处位置的指针(其在内存中的地址),而school就是引用这个具体位置的名称。
	对象的类型也称对象的类别，用于描述对象的内部表示及它支持的方法和操作；
	创建特定类型的对象时，有时也将该对象称为该类型的实例；
	实例被创建后，其身份和类型就不可改变；
		如对象值是可改变的，则成为**可变对象**；
		如果对象的值是不可改变的，则称为**不可变对象**；
	如果某个对象包含对其他对象的引用，则将其称为**容器**；
	大多数对象都拥有大量特有的数据属性和方法：
		属性：与对象相关的值；
		方法：被调用时将在对象上执行某些操作的函数；
		使用点(.)运算符可以访问属性和方法；

class：在自定义类型时使用；
type：

instance：实例化；

类：数据和方法组成；
	数据：变量；
	方法：函数；

类：实例化成对象；
	CA：
		IA：
		IB：

### 对象的身份与类型：
Python内置函数id()可返回一个对象的身份，即该对象在内存中的位置；
	is运算符用于比较两个对象的身份；
	type()用于返回一个对象的类型；
	对象类型本身也是一个对象，称为对象的类；
		该对象的定义是唯一的，且对于某类型的所有实例都是相同的；
		所有类型对象都有一个指定的名称，可用于执行类型检查，如list,dict
```python
if a is b:
    statements
if a == b:
    statements
if type(a) is type(b):
    statements
```

两个对象比较：
-	1、值比较：对象中的数据是否相同； num1 == num2
-	2、身份比较：两个变量名引用是否为同一对象；  num1 is num2
-	3、类型比较：两个对象的类型是否相同；   type(num1) is type(num2)

### Python核心数据类型：
- 数字：int,long,float,complex,bool
	3077，3.14，300000
- 字符: str,unicode
	'mageedu.com',"spam"
- 列表：list
	['one','two','three']
- 字典：dict
	{'course':'linux','language':'python'}
- 元组：tuple
	(32,'spam','eggs')
- 文件: file
	myFile=open('/tmp/tfile','r')
- 集合：set,frozenset(冻结集合)
	set('abc'),{'a','b','c'}
- 其他类型：
	类类型，None，布尔型；
- 编程单元类型：
	函数、模块、类
- 与实现相关的类型：
	编译的代码堆栈跟踪；
- 其他文件类工具：pipes,fifos,sockets

### 类型转换：
- str(),repr()或format()：将非字符型数据转换为字符；
	str1 = repr(num1)
- int():转换为整数；
- float():转换为浮点数；
- list(s): 将字串s转换为列表；
- tuple(s):将字串转换为元组；
- set(s): 将字串s转换为集合；
- frozenset(s)：将字串s转换为不可变集合；
- dict(d): 根据指定的键值对，创建字典，d必须是(key,value)的元组序列；
- chr(x): 将整数转换为单个字符；
- ord(x): 将字符转换为整数值；
- hex(x): 将整数转换为16进制字符；
- bin(x): 将整数转换为2进制字符；
- oct(x): 将整数转换为8进制字符；

### 数字类型：
	库：
		numpy：科学运算相关；
		math：数学相关的运算；

	python的数字字面量：布尔型，整数，浮点数，复数；
		布尔型：
			True：1
			False：0
	数字类型的算术运算：
		x + y	加法
		x - y 	减法
		x * y 	乘法
		x / y	除法
		x // y	截断除法
		x ** y	乘方；
		x % y 取模(x mod y)
		-x		一元减法(负数)
		+x		一元加法(正数)

	位移运算：
		正数：
			向左移，数字增大；
			向右移，数字变小；

		x << y 左移
		x >> y 右移
		x & y  按位与
		x | y  按位或
		x ^ y  按位抑或
		~x	   按位求反

### 序列类型：
序列类型表示索引为非负整数的有序对象集合，包括字符串、列表和元组；
	字符串是字符的序列；
	列表和元组是任意python对象的序列；
字符和元组属于不可变序列，而列表则支持插入、删除和替换元素；
所有序列都支持迭代；

	字符类型：
		字符串字面量：把文本放入单引号、双引号、三引号中；三(单|双)引号可以实现跨行定义；

		如果要使用unicode编码，则在字符之前使用字符u进行标识，如: u"magedu.com"

		文档字串：模块、类或函数的第一条语句是一个字符的话，该字符串就成为文档字符串，可以通过__doc__变量引用；

```python
In [14]: def printName():
    ...:     "test function"
    ...:     print "Hello,sslinux.com"
    ...:     

In [15]: printName()     #使用括号()运算符，表示调用函数；
Hello,sslinux.com

In [16]: printName().__doc__  
Hello,sslinux.com

In [17]: printName.__doc__     #不适用括号运算符()表示调用函数对象本身；
Out[17]: 'test function'
```

### 适用于所有序列的操作和方法：
运算符：
-	s[i]: 索引运算符；
-	s[i:j]: 为切片运算符；
-	s[i:j:stride] 为扩展切片运算符；
-	切片运算，切片后的结果会生成新对象；

内置函数：
-	min(s)和max(x)，只适用于能够对元素排序的序列；按ASCII码排序；
-	sum(s)只适用于数字序列；求各项之和；
-	all(s) 检查序列中的各项是否都为True；
-	len(s) 序列s中的元素个数；
-	any(s) 检查序列s中的任意项是否为true；

### 适用于字符串的操作：
Python2 提供两种字符串对象类型；
	字节字符串：字节(8bit数据)序列；
	Unicode字符串：Unicode字符(16bit数据)序列；
		Python可以使用32 bit整数保存Unicode字符，但此为可选特性；
- s.captitalize()			首字符变大写；
- s.index(sub [, start [,end]])	找到指定字符串sub首次出现的位置，否则报错；
- s.join(t)				使用s作为分隔符,连接序列t中的字符串；

```python
In [18]: str1 = "www.sslinux.com"

In [19]: l1 = list(str1)

In [20]: print l1
['w', 'w', 'w', '.', 's', 's', 'l', 'i', 'n', 'u', 'x', '.', 'c', 'o', 'm']

In [21]: ''.join(l1)
Out[21]: 'www.sslinux.com'
```

- s.lower()				转换为小写形式；
- s.replace(old,new [,maxreplace]) 	替换一个子字符串；
- s.split([sep [,maxaplit]])  	使用sep作为分隔符对一个字符串进行划分。maxsplit是划分的最大次数；
- s.strip([chrs])			删掉chrs开头和结尾的空白或字符；
- s.upper()				将一个字符串转换为大写形式；





### 适用于可变序列的操作：
- s[i] = v   			元素赋值；
- s[i:j] = t 			切片赋值；
- s[i:j:stride] = t   扩展切pain赋值；
- del s[i]			元素删除；
- del s[i:j]			切片删除；
- del s[i:j:stride]	扩展切片删除；

### 适用于列表的方法：
list(s)可将任意可迭代类型转换为列表，而如果s已经是一个列表，则该函数构造的新列表是s的一个浅复制；

- list(s)			将s转换为一个列表；
- s.append(x)		将一个新元素x追加到s末尾；
- s.extend(t)		将一个新列表t追加到s末尾；
- s.count(x)		计算s中x的出现次数；
- s.index(x,[,start[,stop]])	当s[i] == x.strt是返回最小的i，可选参数stop用于指定搜索的起始和结束索引；
- s.insert(i,x) 	在索引i处插入x
- s.pop([i])		返回元素i并从列表中移除它。如果省略i，则返回列表中最后一个元素；
- s.remove(x)		搜索x并从s中移除它
- s.reverse()		颠倒s中的所有元素的顺序；
- s.sort([key [,reverse]])   	对s中的所有元素进行排序。key是一个键函数。reverse是一个标志，表明以倒序对列表进行排序。key和reverse应该始终以关键字参数的形式指定；


