# Python中的类详解
## python的类与面向对象：

### 面向对象编程(OOP)
程序 = 指令 + 数据
	代码可以选择以指令为核心或以数据为核心进行编写；
两种泛型：
	以指令为中心：围绕"正在发生什么"进行编写；
		面向过程编程：程序具有一系列线性步骤；主体思想是代码作用于数据；
	以数据为核心：围绕"将影响谁"进行编写；
		面向对象编程(OOP):围绕数据及为数据严格定义的接口来组织程序，用数据控制对代码的访问；
### 面向对象编程的核心概念：
所有编程语言的最终目的都是提供一种抽象方法：
在机器模型("解空间"或"方案空间")与实际解决的问题模型("问题空间")之间，程序员必须建立一种联系；
	面向过程： 程序 = 算法 +　数据结构；
	面向对象： 将问题空间中的元素以及它们在解空间中的表示物抽象为对象，并允许通过问题来描述问题而不是方案。
		可以把实例想象成一种新型变量，它保存着数据，但可以对自身的数据执行操作。
```python
In [1]: l1 = [1,2,3]     # 实例不仅包含数据本身，还包含能对数据施加的操作；

In [2]: l1.pop()
Out[2]: 3

In [3]: print(l1)
[1, 2]
```

类型由状态集合(数据)和转换这些状态的操作集合组成；
类抽象：
	类：定义了被多个同一类型对象共享的结构和行为(数据和代码)
	类的数据和代码：即类的成员
		数据：成员变量或实例变量；
		成员方法：简称为方法，是操作数据的代码，用于定义如何使用成员变量；因此一个类的行为和接口是通过方法来定义的。
	方法和变量：
		私有：内部使用；
		公共：外部可见；

类未被实例化时，是不能对其执行操作的；

### 面向对象的程序设计方法：
- 所有的东西都是对象；
- 程序是一大堆对象的组合；
	通过消息传递，各对象知道自己该做什么；
	消息：即调用请求，它调用的是从属于目标对象的一个方法；
- 每个对象都有自己的存储空间，并可容纳其它对象；
	通过封装现有类，可以制作成新型类；
- 每个对象都属于某一类型：
	类型，也即类；
	对象是类的实例；
	类的一个重要特性为"能发什么样的消息给它"
- 同一个类的所有对象都能接收相同的消息；
```python
In [5]: s1 = 'abcd'

In [6]: s1.pop()   # 因为实例化对象s1并不支持pop这样的消息(方法)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-da63ff21a00b> in <module>()
----> 1 s1.pop()

AttributeError: 'str' object has no attribute 'pop'
```

### 对象的接口：
定义一个类后，可以根据需要实例化多个对象；
如何利用对象完成真正有用的工作？
	必须有一种方法能向对象发出请求，令其做一些事情；
	每个对象仅能接受特定的需求；
		能像对象发送的请求由其"接口"进行定义；
		对象的"类型"或"类"则规定了它的接口形式；

例如：
```
类型名： Light
接口：
	on()
	off()
	brighten()
	dim()
```

类：将同一种物事的共同特性抽象出来的表现；
	状态和转换这些状态的操作；
	数据：(在类被实例化时传递给类)
		变量：就是类属性
	方法：
		函数；操作变量引用的数据的代码；

绑定方法：只能通过实例来调用；


### 类间关系：
- 依赖("uses-a")
	一个类的方法操作另一个类的对象；
- 聚合("has-a")
	类A的对象包含类B的对象；
- 继承("is-a")
	描述特殊与一般关系；只要能被父类接受的操作，子类一定能接受；

### 面向对象编程的元组：

面向对象的模型机制有3个原则：封装、继承及多态；

#### 封装(Encapsulation)
	隐藏实现方案细节；
	将代码及其处理的数据绑定在一起的一种编程机制，用于保证程序和数据不受外部干扰且不会被误用；

#### 继承(Inheritance)
	一个对象获得另一个对象属性的过程；用于实现按曾分类的概念；
	一个深度继承的子类继承了类层次中它的每个祖先的所有属性；
	超类、基类、父类
	子类、派生类；

#### 多态性(Polymorphism)
允许一个接口被多个通用的类动作使用的特性，具体使用哪个动作与应用场合相关；
"一个接口，多个方法"
	用于为一组相关的动作设计一个通用的接口，以降低程序复杂性；
```python
In [7]: def plus(x,y):
   ...:     print(x+y)
   ...:     

In [8]: plus(1,3)
4

In [9]: plus('a','b')
ab

In [10]: plus([1,2,3],['a','b','c'])
[1, 2, 3, 'a', 'b', 'c']
```

### python类和实例：
类是一种数据结构，可用于创建实例；
	一般情况下，类封装类数据和可用于该数据的方法；
python类是一个可调用对象，即类对象；
python2.2之后，类是一种自定义类型，而实例则是声明某个自定义类型的变量；

实例初始化：
	通过调用类来创建实例；
		instance = ClassName(args...)
	类在实例化时可以使用__init__ 和 __del__两个特殊的方法；

class class_name   会在内存中生成一个class_name的对象，其后的语句在实例化时执行；类中的函数也是在调用实例的方法时执行；

### Python中创建类：
Python使用class关键字创建类，语法格式如下：
class ClassName(bases):
    'class document string'
    class_suite

超类是一个或多个用于继承的父类的集合；
类体可以包含：声明语句、类成员变定义、数据属性、方法

注意：
	如果不存在继承关系，ClassName后面的"(bases)"可以不提供；
	类文档为可选；

class语句的一般形式：
```python
class ClassName(bases):
    data = value                # 定义数据属性；类属性；
    def method(self,...):       # 定义方法属性；
        self.member = value     # 定义实例属性；

    # 类中的方法定义：第一个参数必须是self。
```

类名：所有单词的首字母大写；

例子：
	在python中，class语句类似def，是可执行代码；直到运行class语句后类才会存在：
![class_define](/images/class_define.png)

class语句内，任何赋值语句都会创建类属性；
每个实例对象都会继承类的属性并会的自己的名称空间；

```python
In [1]: class FirstClass():
   ...:     data = 'hello class'
   ...:     def printData(self):
   ...:         print(self.data)
   ...:         

In [2]: ins1 = FirstClass()

In [3]: ins1.data
Out[3]: 'hello class'

In [4]: ins1.printData()
hello class
```

```python
In [5]: class SecClass():
   ...:     data = 'hello SecClass'
   ...:     def printdata(self):
   ...:         print("Content from method: %s" % self.data)
   ...:         

In [6]: ins2 = SecClass()

In [7]: ins2.data
Out[7]: 'hello SecClass'

In [8]: ins2.printdata()
Content from method: hello SecClass

In [9]: ins3 = SecClass()

In [10]: ins3.data
Out[10]: 'hello SecClass'

In [11]: ins3.printdata()
Content from method: hello SecClass
```

```python
In [12]: class ThirdClass():
    ...:     data = 'hello ThirdClass'
    ...:     def setdata(self,x):
    ...:         self.str1 = x
    ...:     def printdata(self):
    ...:         print(self.str1)
    ...:         

In [13]: ins4 = ThirdClass()

In [14]: ins4.data
Out[14]: 'hello ThirdClass'

In [15]: ins4.setdata('abcd')

In [16]: ins4.printdata()
abcd

In [17]: ins5 = ThirdClass()

In [18]: ins5.data     # 类属性是供所有实例所共享的；
Out[18]: 'hello ThirdClass'

In [19]: ins5.setdata('xyz')

In [20]: ins5.printdata()   # 实例属性，是每个实例所私有的；
xyz

In [21]: ins4.printdata()
abcd
```

Python类方法及调用：
实例(对象)通常包含属性；
	可调用的属性：方法；
		object.method()
	数据属性；
在OOP中，实例就像是带有"数据"的记录，而类是处理这些记录的"程序"
	通过实例调用方法相当于调用所属类的方法类处理当前实例；
		类似instance.method(args...)会被自动转换为：
		class.method(instance,args...)
			如前面的例子,x.display()会被自动转换为FirstClass.display(x),即调用类的方法来处理实例x；
		因此，类中每个方法必须具有self参数，它隐含当前实例之意；
		在方法内对self属性做赋值运算会产生每个实例自己的属性；
		python规定，没有实例，方法不允许被调用，此即为"绑定"。

### python类和实例的属性：
class语句中的赋值语句会创建类属性，如前面例子中的spam；
在类方法中对传给方法的特殊参数self进行赋值会创建实例属性；
```python
In [22]: class MyClass():
    ...:     gender = 'Male'
    ...:     def setName(self,who):
    ...:         self.name = who
```
![class_instance](/images/class_instance.png)


