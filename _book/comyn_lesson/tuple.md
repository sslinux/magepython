## 元组

### 定义和初始化：

```python 
In [6]: t = tuple()    # 使用工厂函数tuple()初始化空元组；

In [7]: t
Out[7]: ()


In [8]: t = ()         # 直接使用()，定义空元组；

In [9]: t
Out[9]: ()

In [10]: t = (1,2,3)  # 定义时，赋值；

In [11]: t
Out[11]: (1, 2, 3)

In [12]: t = tuple(range(3))    # 使用tuple工厂函数，通过可迭代对象初始化元组；

In [13]: t
Out[13]: (0, 1, 2)
```

```python 
class tuple(object)
 |  tuple() -> empty tuple
 |  tuple(iterable) -> tuple initialized from iterable's items
 |  
 |  If the argument is a tuple, the return value is the same object.
```

**注意：**
    在初始化元组时，若元组只有一个元素，则需要在该元素后加一逗号；

Example：
```python
In [91]: t = (5)    # 若不加逗号，则定义成了整型；

In [92]: type(t)
Out[92]: int

In [93]: t
Out[93]: 5

In [94]: t = (5,)   # 单个元素的元组，在元素后添加逗号；

In [95]: type(t)
Out[95]: tuple

In [96]: t
Out[96]: (5,)
```


## 元组的操作：元组是不可变序列;

        元组是可hash的，列表不可hash；

### 查询：

**索引操作(下标)**

```python 
In [15]: t[-1]
Out[15]: 2

In [16]: t[-1] = 2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-16-47356e648374> in <module>()
----> 1 t[-1] = 2
# 元组是不可变序列，不能修改其元素的值；
TypeError: 'tuple' object does not support item assignment
```

**index、count方法和list的表现一致**

```python 
index(...)
    T.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.
```

```python 
count(...)
    T.count(value) -> integer -- return number of occurrences of value
```

因为不可变，所以是可hash的，可以做字典的key，可以做set的元素；

---

### 命名元组：

```python
In [21]: from collections import namedtuple

In [22]: User = namedtuple('User',['name','age'])

In [23]: me = User('sslinux',18)

In [24]: me
Out[24]: User(name='sslinux', age=18)

In [25]: me.name
Out[25]: 'sslinux'

In [26]: me.age
Out[26]: 18

In [27]: me[0]
Out[27]: 'sslinux'

In [28]: me[1]
Out[28]: 18
```

