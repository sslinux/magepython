# Python中的正则表达式

回顾：

文件对象：

	open('file','mode','bufsize')
	read,readline,readlines,write,writelines,flush,seek,tell

	模块：os
		文件系统接口；
	模块：os.path

	对象流式化，持久化：
		pickle,数据流式化存储模块；

	文件是可迭代对象：
		iter(),__iter__(),


## 正则表达式：
python本身不支持正则表达式，通过re模块实现；

查看当前系统上有哪些模块可用：

In [7]: help('modules')

help支持交互式模式：help()


python正则表达式：类似于扩展正则表达式；

import re

- 元字符：
```
	.       任意单个字符；
	[...]   指定范围内的任意单个字符；
	[^...]  指定范围外的任意单个字符；
```

- 次数：
```
	?: 0次或1次；
	+: 1次或多次；
	{m}: 指定次数；
	{m,n}
	{0,n}
	{m,}
```

- 锚定：
```
	^   行首；
	$   行尾
	pat1|pat2
	(...)  分组，方便后面引用；
	\b   词首、词尾；
```

- 字符集：

```
	[0-9]: \d
	[0-9a-zA-Z]: \w   <==取反==> \W
	\s : 任意空白字符； <==>  [\n\t\f\v\r]   <==取反==> \S
	\nn: 后向引用；引用后边()中匹配到的字符；
```

正常情况是工作在贪婪模式下的：

要使用非贪婪模式，在指定次数的字符后加?

(*|+|?|{})?:  表示使用非贪婪模式；


#### match对象： 根据正则表达式匹配到的结果对象；

match(pattern, string, flags=0)

```python
In [8]: import re        # 导入正则表达式的模块；

In [9]: help(re.match)

In [14]: re.match('a','abc')    # 使用re.match()函数在字符串'abc'中匹配字符'a'，返回结果为一个match对象；
Out[14]: <_sre.SRE_Match at 0x7f6906323f38>

In [15]: match = re.match('a','abc')  

In [16]: match. 					# match对象支持的方法和属性；
        match.end       match.group     match.lastgroup match.re        match.start     
        match.endpos    match.groupdict match.lastindex match.regs      match.string    
        match.expand    match.groups    match.pos       match.span  
```

```python
match.string      # 匹配的字符串本身；
match.re          # 匹配时使用的条件；
match.group()     # 返回此次模式匹配到的结果；
In [21]: match = re.match('a.','abc')

In [22]: match.group()
Out[22]: 'ab'

match.groups([index])    # 返回匹配到的结果组成的元组；
match.pos                # 指定match开始匹配的位置；
match.endpos   			 # 使用match结束搜索位置；
match.start()			 # 返回pattern所匹配到的字符串在原字符串中的起始位置；
match.end()			     # 返回pattern所匹配到的字符串在原字符串中的结束位置；
```

```python
In [17]: match.re
Out[17]: re.compile(r'a')

In [18]: pat = re.compile('bc')   # 手动编译匹配条件；

In [19]: match = pat.match('abcdefg')   # 使用手动编译的条件对象去从指定的字符串中匹配；

In [20]: match = re.match('bc','abcdefg')   # 二者是等价的；
```

re.search()   # 匹配并返回match 对象；
re.findall()  # 使用pattern匹配string，若匹配多次，则用列表的方式返回所有匹配对象；


pattern = re.compile(r'ma.')
mat = pattern.search(url)
mat.group()
mat.pos
mat.endpos
mat.start()
mat.end()

mat2 = re.findall('m',url)    # 返回的是一个列表；
print mat2

re.finditer(pattern,string,flags=0)
和findall() 相同，但返回的是迭代器；
iter1 = re.finditer('m',url)
iter1.next()   # 依然是一个match对象；
iter1.next()

re.split(pattern,string,maxsplit=0,flags=0)
re.splite('\.',url)   # 把字符串url,按指定字符串或pattern进行切割；

```python
f1 = open('/etc/passwd','r')
re.split(':'.reline())
```

re.sub(pattern,repl,string,count,flags=0)
查找替换，返回由replace替换后的字符；

url = 'www.magedu.com'
re.sub('ma','MA',url)

re.subn    # 返回元组，包含被pattern替换的次数；


总结：
re.search ： 返回一个match对象；
	match对象的；   # 应该对返回的值进行判断，否则容易引发异常；
		属性：
			string
			re
			pos
			endpos
		方法：
			group()
			start()
			end()

re.findall : 返回一个列表；

re.sub:  查找替换，返回替换后的整个串；
re.subn:　返回元组，替换后的串及替换次数；

re.compile: 手动编译匹配条件；

思考： 复制/etc/passwd到/tmp,如何替换/tmp/passwd中的/bin/bash为/BIN/BASH?


# match对象的group()
```python
In [24]: str1 = 'hellopat world'

In [25]: pat1 = re.compile('.(o(.))')    # 手动编译一个匹配条件；

In [26]: mat1 = pat1.search(str1)        # 根据匹配条件在字符串中匹配；

In [27]: if mat1:
    ...:     print mat1.group()          # 输出整个匹配到的内容；
    ...:     
lop

In [28]: if mat1:
    ...:     print mat1.group(1)         # 输出匹配条件中第1个()匹配到的内容；
    ...:     
op

In [29]: if mat1:
    ...:     print mat1.group(2)         # 匹配条件中第2个()匹配到的内容；
    ...:     
p

In [30]: print mat1.groups()             # 以元组的方式返回匹配条件中多个()匹配到的内容；
('op', 'p')

In [31]: pat1.findall(str1)              # 返回列表，每次匹配到时，多个()匹配到内容组成一个元组的元素；多次匹配到的内容组成的元组形成一个列表；
Out[31]: [('op', 'p'), ('or', 'r')]

```

flags: 标记：
	I或IGNORECASE：忽略字符大小写；
	M或MULTILINE：可以跨行匹配；
	A或ASCII：仅执行8位ascii码匹配；
	U或UNICODE： 使用\w,\W

```python
In [32]: pat2 = re.compile('.(o(.))',re.I)     # 忽略大小写

In [33]: pat2 = re.compile('.(o(.))',re.I|re.M)   # 忽略大小写或可以跨多行；

In [34]: pat2 = re.compile('.(o(.))',re.I)

In [35]: str2 = 'hellOxyz world'

In [36]: mat2 = pat2.search(str2)

In [37]: print mat2.group()
lOx

In [38]: print mat2.groups()
('Ox', 'x')

In [39]: print pat2.findall(str2)
[('Ox', 'x'), ('or', 'r')]

In [40]: for mat in pat2.finditer(str2):
    ...:     print mat
    ...:     
<_sre.SRE_Match object at 0x7f69062a07a0>
<_sre.SRE_Match object at 0x7f69062a0828>

In [41]: for mat in pat2.finditer(str2):
    ...:     print mat.group()
    ...:     
lOx
wor

In [42]: print pat2.findall(str2)
[('Ox', 'x'), ('or', 'r')]

In [43]: for mat in pat2.finditer(str2):
    ...:     print mat.groups()
    ...:     
('Ox', 'x')
('or', 'r')
```
