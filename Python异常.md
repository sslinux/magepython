# Python异常：

# 异常：

Python的运行时错误称作异常：
- 语法错误：软件的结构上有错误而导致不能被解释器解释或不能被编译器编译；

- 逻辑错误：由于不完整或不合法的输入导致，也可以是逻辑无法生成、计算或者输出结果需要的过程无法执行等。
```python
In [1]: f1 = open('/tmp/a.txt')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-1-16a084dd29a2> in <module>()
----> 1 f1 = open('/tmp/a.txt')

FileNotFoundError: [Errno 2] No such file or directory: '/tmp/a.txt'
```

```python
In [2]: print('a'+3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-2ac73431b0b1> in <module>()
----> 1 print('a'+3)

TypeError: Can't convert 'int' object to str implicitly
```
异常的发生，会导致程序执行终止；

### python异常：
python异常是一个对象，表示错误或意外情况；
在python检测到一个错误时，将触发一个异常；
- python可以通过异常传导机制传递一个异常对象，发出一个异常情况出现的信号；
- 程序员也可以在代码中手动触发异常；

Python异常也可以理解为：程序出现了错误而在正常控制流以外采取的行为；
- 第一阶段：解释器触发异常，此时当前程序流将被打断；
- 第二阶段：异常处理，如忽略非致命性错误、减轻错误带来的影响等；

### 异常的公用：
- 错误处理：
	python的默认处理：停止程序，打印错误信息；
	使用try语句处理异常并从异常中恢复；
- 事件通知：
	用于发出有效状态信号；
- 特殊情况处理：
	无法调整代码去处理的场景；
- 终止行为：
	try/finally语句可确保执行必需的结束处理机制；
- 非常规控制流程：
	异常是一种高级跳转(goto)机制；

### 检测和处理异常：
- 异常通过try语句来检测：
	任何在try语句块里的代码都会被检测，以检查有无异常发生；
- try语句有两种形式：
  - try-except:检测和处理异常
  	可以有多个except；
  	支持使用else子句处理没有探测异常时的执行的代码；
  - try-finally: 仅检查异常并做一些必要的清理工作；不对异常本身进行处理；
  	仅能有一个finally

- try语句的复合形式：
	try-except-finally

### try-except语句
定义了进行异常监控的一段代码，并且提供了处理异常的机制；

语法：
try:
    try_suite
except Exception[,reason]:
	except_suite

Example:(python2.7.12)
```python
In [1]: try:
   ...:     f1 = open('/tmp/a.txt','r')
   ...: except IOError,e:
   ...:     print('Could not open file:',e)  # e保存的是前面异常的原因(reason)
   ...:     
('Could not open file:', IOError(2, 'No such file or directory'))
```
```python
In [3]: try:
   ...:     f1 = open('/tmp/abc.txt','r')
   ...: except IOError,reason:
   ...:     print("Could not open file: /tmp/abc.txt",reason)
   ...: 
('Could not open file: /tmp/abc.txt', IOError(2, 'No such file or directory'))
```

### try-except-else语句：
try语句可以带多个except子句，还可以有一个可选的else子句，语法格式如下：
```python
try:
    try_suite
except Exception1[,reason]:
    suite_exception1
except (Exception2,Exception3,...)[,reason]:     # 一次捕获多个异常时要定义为元组；
	suite_
...
except:           # 空except语句用于捕获一切异常；
	suite_
else:
    else_suite
```

except分句个数没有限制，但else只能有一个；
没有异常发生时，else分句才会执行；
没有符合的except分句时，异常会向上传递到程序中的之前进入的try语句中或者到进程的顶层(解释器)；

### try-finally语句
无论异常是否发生，finally子句都会执行；
	常用语定义必须进行的清理动作，如关闭文件或断开服务器连接等；
finally中的所有代码执行完毕后会继续向上一层引发异常；

语法：
try:
    try_suite
finally:
    finally_suite

```python
In [5]: try:
   ...:     f1 = open('/tmp/a.txt','r')
   ...:     f1.write('hello world')
   ...: except IOError,reason:
   ...:     print("There is some problem for write statement to file /tmp/a.txt.",reason)
   ...: finally:
   ...:     f1.close()
   ...:     
   ...:     
('There is some problem for write statement to file /tmp/a.txt.', IOError(2, 'No such file or directory'))
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-5-04febf19ca2a> in <module>()
      5     print("There is some problem for write statement to file /tmp/a.txt.",reason)
      6 finally:
----> 7     f1.close()
      8 
      9 

NameError: name 'f1' is not defined   # 此处出现NameErro是因为文件不存在所以创建f1对象失败；
```

Example:
```python
#!/usr/bin/env python
# 
try:
    while True:
        d1 = input("An integer:")
        if d1 == 'quit': break
        d2 = input("Another integer:")
        print( int(d1) / int(d2))
except ZeroDivisionError,reason:
    print("Not 0",reason)
except ValueError:
    print("Not 'quit'")
except:
    print("Unknow error")
```

### try-except-else-finally语句:
语法：
```python
try:
    try_suite
except Exception1:
    suite1_exception1
except (Exception2,Exception3):
    suite23_exception23
...
else:
	else_suite
finally:
	finally_suite
```
可以替换为在try-finally语句中嵌套try-except语句的形式；

### try语句嵌套：
try:
    try:
        try_suite
    except:
    except:
    else:
finally:
	suite_finally


### 自定义异常：
raise语句可显式触发异常：
raise [SomeException [, args [, traceback]]]
- SomeException: 可选，异常的名字，仅能使用字符串、类或实例；
- args：可选，以元组的形式传递给异常的参数；
- traceback：可选，异常触发时新生成的一个用于异常-正常化的跟踪记录，多用于重新引发异常时；

```python
In [14]: def f1(seq1,seq2):
    ...:     if not seq1 or not seq2:
    ...:         raise ValueError,"Seq must not be empty."
    ...:     return [(x1,x2) for x1 in seq1 for x2 in seq2 ]
    ...: 

In [15]: l1 = [1,2,3]

In [16]: l2 = ['a','b','c']

In [17]: f1(l1,l2)
Out[17]: 
[(1, 'a'),
 (1, 'b'),
 (1, 'c'),
 (2, 'a'),
 (2, 'b'),
 (2, 'c'),
 (3, 'a'),
 (3, 'b'),
 (3, 'c')]

In [18]: l3 = []

In [19]: f1(l1,l3)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-19-b10a9547762f> in <module>()
----> 1 f1(l1,l3)

<ipython-input-14-e7b8e85b8520> in f1(seq1, seq2)
      1 def f1(seq1,seq2):
      2     if not seq1 or not seq2:
----> 3         raise ValueError,"Seq must not be empty."
      4     return [(x1,x2) for x1 in seq1 for x2 in seq2 ]

ValueError: Seq must not be empty.

```

### raise语句的用法大全；
![raise_usage](/images/raise_usage.png)

### 异常对象：
Python异常时内置的经典类Exception的子类的实例：
	为了向后兼容，Python还允许使用字符串或任何经典类实例；
	Python2.5之后，Exception是从BaseException继承的新式类；

Python自身引发的所有异常都是Exception的子类的实例；
大多的标准异常都是由StandardError派生的，其有3个抽象的子类；
- ArithmeticError
	由于算术错误而引发的异常基类；
	OverflowError，ZeroDivisonError，FloatingPointError
- LookupError
	容器在接收到一个无效键或索引是引发的异常的基类；
	IndexError,KeyError
- EnvironmentError
	由于外部原因而导致的异常的基类；
	IOError,OSError,WindowsError


### 标准异常类：
- AssertionError
	断言语句失败
- AttributeError
	属性引用或赋值失效
- FloatingPointError
	浮点型运算是被；
- IOError
	I/O操作失败
- ImportError
	import语句不能找到要导入的模块，或者不能找到该模块特别请求的名称；
- IndentationError
	解析器遇到类一个由于错误的缩进而引发的语法错误；
- IndexError
	用来索引序列的整数超出了范围；
- KeyError
	用来索引映射的键不在映射中；
- KeyboardInterrupt
	用户按类中断键(Ctrl+c,Ctrl+Break或Delete键)
- MemoryError
	运算耗尽内存
- NameError
	引用类一个不存在的变量名；
- NotImplementedError
	由抽象基类引发的异常，用于指示一个具体的子类必须覆盖一个方法；
- OSError
	由模块os中的函数引发的异常，用来指示平台相关的错误；
- OverflowError
	整数运算的结果太大导致溢出；
- SyntaxErro
	语法错误
- SystemError
	Python本身或某些扩展模块中的内部错误；
- TypeError
	对某对象执行了不支持的操作；
- UnboundLocalError
	引用未绑定值得本地变量；
- UnicodeError
	在Unicode的字符串之间进行转换时发生的错误；
- ValueError
	应用于某个对象的操作或函数，这个对象具有正确的类型，但却有不适当的值；
- WindowsError
	模块os中的函数引发的异常，用来指示与Windows相关的错误；
- ZeroDivisionError
	除数为0


### 自定义异常类
#### 自定义异常和多重继承
较有效的方法是从自定义异常类和标准异常类进行多重继承，例如：
class CustomAttributeError(CustomException,AttributeError):
	pass

#### 标准库中使用的其他异常
python标准库中的许多模块都定义了自己的异常类，如socket中的socket error
	等同于自定义的异常类；


### assert语句
assert语句用于在程序中引入调试代码
assert condition[,expression]
	如果condition条件满足，则assert不做任何操作；
	如果condition条件不满足，则assert使用expression作为参数实例化，AssertionError并引发结果实例；

注意：如果运行Python是使用了-O优化选项，则assert将是一个空操作：编译器不为assert语句生成代码；

运行Python是不使用-O选项，则__debug__内置变量为True，否则其值为False；

assert语句相当于下面的代码：
if __debug__:
    if not condition:
        raise AssertionError,<expression>

assert实现:	手动触发异常；
	assert condition[,expression]

	if __debug__:
	    if not condition:
	        raise AssertionError,expression

Python异常对象：
	BaseException：
		三个基本抽象类；
raise手动触发异常；
assert断言(raise的特殊表现)









