# set(集合)

## 定义(初始化)
set() -> new empty set object
set(iterable) -> new set object
s = {item1,item2,....}

初始化时，若使用s = {itme,item...}的方式定义时，千万不能省略itme，试图定义一个空集合，
s = {}  会将s定义为一个字典；


## 删除：
* remove 删除给定元素，元素不存在抛出KeyError；
* discard 删除给定的元素，元素不存在，什么也不做； 
* pop 随机删除一个元素并返回，集合为空时，抛出KeyError；
* clear 清空集合；


## 修改：
集合不能修改单个元素；


# 查找：

    集合不能通过索引访问；

    集合没有访问单个元素的方法；

**集合不是线性结构，集合元素没有顺序**


## 增加
* add
```python
add(...)
    Add an element to a set.
    
    This has no effect if the element is already present.
```

* update
```python 
update(...)  # 将一个可迭代对象中的元素加入到set中；
    Update a set with the union of itself and others.
```

## 成员运算符：
* in
* not in 

用于判断一个元素是否在容器中；

```python 
In [48]: lst = list(range(5))

In [49]: lst
Out[49]: [0, 1, 2, 3, 4]

In [50]: lst.append(('hello','python'))

In [51]: lst
Out[51]: [0, 1, 2, 3, 4, ('hello', 'python')]

In [52]: 'hello' in lst
Out[52]: False
```

集合的成员运算符和其他线性结构的时间复杂度不同；


```python 
In [55]: s = set(range(10000000))

In [56]: -10 in s
Out[56]: False

In [57]: %%timeit   # ipython提供的功能，循环执行后续语句，计时；
    ...: -10 in s
    ...: 
The slowest run took 29.13 times longer than the fastest. This could mean that an intermediate result is being cached.
10000000 loops, best of 3: 53.1 ns per loop
```

做成员运算符的时候，集合的效率远高于列表；

做成员运算时，列表的效率和列表的规模有关；

做成员运算时，集合的效率和结合的规模无关；


成员运算效率：

*    集合的效率： O(1)

*    列表(线性结构) O(n)


## 集合运算：

* 交集：
    - intersection
```python 
# 存在结合A和B，对于集合C，如果C的每个元素既是A的元素，又是B的元素，并且A和B的所有相同的元素都在C中找到，那么C是A和B的集合；
intersection(...) method of builtins.set instance
    Return the intersection of two sets as a new set.   # 返回的是新的集合，不改变原有集合；
    
    (i.e. all elements that are in both sets.)
```

    - intersection_update
```python 
# 求交集，修改原有集合；
intersection_update(...) method of builtins.set instance
    Update a set with the intersection of itself and another.
```

```python
In [63]: s1 = {1,2,3}

In [64]: s2 = {2,3,4}

In [66]: s1 & s2  # set 重载按位与运算符，为求交集运算，等效于s1.intersection(s2)
Out[66]: {2, 3}
```

* 差集：
    - difference
```python 
# 集合A和B,当集合C中的元素仅存在于A中，但不存在于B中，并且A中存在B中不存在的元素全部存在于C中，那么C是A和B的差集；
difference(...) method of builtins.set instance
    Return the difference of two or more sets as a new set.
    
    (i.e. all elements that are in this set but not the others.)
```

    - difference_update
```python 
# _update 版本原地修改，返回None，相当于s1 = s1.difference(s2)
difference_update(...) method of builtins.set instance
    Remove all elements of another set from this set.
```

    - "-"重载运算符

        # set 重载了运算符，- 执行了差集计算，相当于 s1.difference(s2)


* 对称差集：

```python 
# 如果把两个集合A和B看成是一个全集，对称差集是交集的补集；
symmetric_difference(...) method of builtins.set instance
    Return the symmetric difference of two sets as a new set.
    
    (i.e. all elements that are in exactly one of the sets.)
```

```python 
In [71]: s2.symmetric_difference(s1)   # 对称差集具有交换律；
Out[71]: {1, 4}

In [72]: s1.symmetric_difference(s2)
Out[72]: {1, 4}
```

```python 
# 原地修改，返回None，相当于 s1 = s1.symmetric_difference(s2)
symmetric_difference_update(...) method of builtins.set instance
    Update a set with the symmetric difference of itself and another.
```

    - "^" 重载运算符：
```python 
In [74]: s1 = {1,2,3}

In [76]: s2 = {2,3,4}

In [77]: s1 ^ s2
Out[77]: {1, 4}
```

* 并集：

    - union

```python 
union(...) method of builtins.set instance
    Return the union of sets as a new set.
    
    (i.e. all elements that are in either set.)
```

    - update 

    update方法其实是union的update版本；

```python 
In [79]: s1 + s2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-79-1659087814e1> in <module>()
----> 1 s1 + s2   # 集合并没有重载加法运算符；

TypeError: unsupported operand type(s) for +: 'set' and 'set'
```

```python
In [80]: s1 | s2  # set重载了按位或运算符，用于并集计算；
Out[80]: {1, 2, 3, 4}
```

* 补集

    补集的定义依赖于全集；

    所以无法求补集；

    全集不是运算，而是一个定义出来的集合；


## 集合相关的判断:

子集、超集：

    集合A中的所有元素都能在集合B里找到，那A是B的子集，B是A的超集；

* issubset()
* issuperset()

```python 
In [93]: s1 = {1,2,3,4}

In [94]: s2 = {2,3}

In [95]: s2.issubset(s1)
Out[95]: True

In [96]: s1.issubset(s2)
Out[96]: False

In [97]: s1.issuperset(s2)
Out[97]: True

In [98]: s2.issuperset(s1)
Out[98]: False
```    

原型：

```python 
In [99]: def issubset(s1,s2):
    ...:     for x in s1:
    ...:         if x not in s2:
    ...:             return False
    ...:     return True
    ...: 

In [100]: def issuperset(s1,s2):
     ...:     for x in s2:
     ...:         if x not in s1:
     ...:             return False
     ...:     return True
     ...: 
```

* isdisjoint()  

    判断两个集合是否有交集，如果有交集返回False，没有交集返回True；

```python 
In [101]: s1.isdisjoint(s2)
Out[101]: False

In [102]: s2.isdisjoint(s2)
Out[102]: False

In [103]: s2.isdisjoint({100,200,300})
Out[103]: True
```

## 集合的应用：

1、有一个API，它要求有认证，并且有一定权限的用户才可以访问，例如：要求满足权限A，B，C中任意一项，有一个用户具有权限B，C，D，那么此用户是否有权限反问此API？
    s1.isdisjoint(s2)

2、有一个任务列表，存储全部的任务，有一个列表，存储已完成的任务，找出未完成的任务；
    求差集；difference


## 集合的限制：

对元素有限制的数据结构：

    bytes

    str

    bytearray

限制：

    8位 int 

    bytearray是0-255的整数；


集合的限制：

    元素不能重复；

    不能存放无法比较的元素；

    可变对象不能作为set的元素：
        
        list、bytearray,set不能作为set的元素；

        tuple、byte，int可以作为set的元素；

**集合元素必须是可hash的**

目前我们所知道的所有的类型都是不可hash的，所有的不可变类型都可hash的；


