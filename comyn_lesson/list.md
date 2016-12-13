# list，列表

* 初始化
* 索引运算
* 增
* 删
* 改
* 查
* 其他方法
---

## 列表初始化：

### 初始化空列表：
```python 
In [2]: lst = list()   # 使用list的工厂函数；

In [3]: lst
Out[3]: []
```
```python 
In [4]: lst1 = []   # 直接使用[]

In [5]: lst1
Out[5]: []
```

### 初始化的同时，为列表增加元素：
```python 
# 手动增加元素：
In [6]: lst = [1,2,3]

In [7]: lst
Out[7]: [1, 2, 3]
```

```python 
# 通过list函数遍历一个可迭代对象来初始化列表；

In [9]: lst1 = list(range(1,11))

In [10]: lst1
Out[10]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## 索引运算：
- 索引从0开始；
- 索引应包含在[]中；
- 负数索引表示从后往前，由-1开始，-1表示最后一个元素；
- 如果引用索引超出范围，将引发IndexError；

```python 
In [14]: lst = list(range(10))    # 使用list函数遍历一个可迭代对象来初始化列表；

In [15]: lst
Out[15]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [17]: lst[4]    # 正数索引；
Out[17]: 4

In [18]: lst[-1]   # 负数索引，-1为最后一个元素；
Out[18]: 9

In [19]: lst[11]   # 引用的索引超出范围，引发IndexError；
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-19-98fb25789163> in <module>()
----> 1 lst[11]

IndexError: list index out of range
```

## 增加元素：
* append()

    在list末尾增加，返回值为None；

```python 
In [20]: help(lst.append)
append(...) method of builtins.list instance
    L.append(object) -> None -- append object to end
```

```python 
In [21]: lst
Out[21]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [22]: lst.append(10)

In [23]: lst
Out[23]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

* insert()

    insert方法需要提供两个参数，一个为索引号，一个为对象，在指定的索引号前插入指定的对象；没有返回值；

```python 
insert(...) method of builtins.list instance
    L.insert(index, object) -- insert object before index
```

```python 
In [27]: lst
Out[27]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

In [28]: lst.insert(0,100)

In [29]: lst
Out[29]: [100, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**注意：**

    insert操作的索引超出范围：

        如果是正索引，等效于append；

        如果是负索引，等效于insert(0,object)


* extend()

    将一个可迭代对象中的元素追加到list的末尾；返回值为None；

```python 
extend(...)
    L.extend(iterable) -> None -- extend list by appending elements from the iterable
```

```python 
In [32]: lst = [1,2,3]

In [33]: l1 = ('a','b','c')

In [34]: l2 = ['x','y','z']

In [35]: lst.extend(l1)  # l1是一个元组

In [36]: lst             # list是原处修改；
Out[36]: [1, 2, 3, 'a', 'b', 'c']

In [37]: lst.extend(l2)  # 此处extend的是一个列表；

In [38]: lst
Out[38]: [1, 2, 3, 'a', 'b', 'c', 'x', 'y', 'z']
```

* lst + ['a','b','c']   # 拼接，返回一个新的list，不修改原有list；

---

## 删： 删除list中的元素
* pop([index])
    删除并返回指定索引的元素，默认索引号为-1，即last one item；

    当list为空时或给定的index超出范围时，会引发IndexError;

```python 
pop(...)
    L.pop([index]) -> item -- remove and return item at index (default last).
    Raises IndexError if list is empty or index is out of range.
```

```python 
In [40]: lst
Out[40]: [1, 2, 3, 'a', 'b', 'c', 'x', 'y', 'z']

In [41]: lst.pop()  # 不指定index，默认删除最后一个元素；
Out[41]: 'z'

In [42]: lst.pop(3) # 删除指定索引号对应的元素；
Out[42]: 'a'

In [43]: lst
Out[43]: [1, 2, 3, 'b', 'c', 'x', 'y']
```

- pop不传递参数，时间复杂度是O(1)
- pop传递index参数，时间复杂度是O(n)

   
* remove(value)

    原地修改，返回None，根据值来删除元素；

    从左到右，删除第一个；当值不存在时，抛出ValueError；

```python 
remove(...)
    L.remove(value) -> None -- remove first occurrence of value.
    Raises ValueError if the value is not present.

# occurrence [ə'kʌr(ə)ns] n.发生；出现；事件；发现；
# present ['prez(ə)nt]
    vt. 提出；介绍；呈现；赠送
    vi. 举枪瞄准
    adj. 现在的；出席的
    n. 现在；礼物；瞄准
```

```python 
In [45]: lst
Out[45]: [1, 2, 3, 'b', 'c', 'x', 'y']

In [46]: lst.remove(3)   # 删除的是指定Value的元素；

In [47]: lst
Out[47]: [1, 2, 'b', 'c', 'x', 'y']

In [49]: lst.remove('b')

In [50]: lst
Out[50]: [1, 2, 'c', 'x', 'y']
```

### pop和remove的对比：
* pop是弹出索引对应的元素；remove是删除与指定值对应的最左边的一个元素；
* pop针对的是索引；remove针对的是值；

* clear()

    清空list中的所有元素；返回值为None；

 ```python 
clear(...)
    L.clear() -> None -- remove all items from L
 ```   
---


## 改：列表是可变序列，索引支持原处修改：

* lst[0] = 5

    通过对列表的索引引用进行重新赋值；如果引用的索引超出范围，会引发IndexError；

```python
In [53]: lst
Out[53]: [1, 2, 'c', 'x', 'y']

In [54]: id(lst[2])          # 赋值前的内存引用；
Out[54]: 139854584522040

In [55]: lst[2] = 'i'   # 通过赋值修改元素；

In [56]: lst          
Out[56]: [1, 2, 'i', 'x', 'y']

In [57]: id(lst[2])  # 与修改前的内存引用不一致，说明list元素的重新赋值，是修改的内存引用；
Out[57]: 139854584075520
```

* sort(key=None,reverse=False)

    返回值为None，对列表中的元素进行排序；

```python 
sort(...)
    L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
```

```python 
In [61]: lt = [3,5,2,8,1,6]

In [62]: lt
Out[62]: [3, 5, 2, 8, 1, 6]

In [63]: lt.sort()   # 默认为正向排序，即从小到大；

In [64]: lt
Out[64]: [1, 2, 3, 5, 6, 8]

In [65]: lt.sort(reverse=True)    # reverse参数默认为False；

In [66]: lt
Out[66]: [8, 6, 5, 3, 2, 1]
```

```python 
In [67]: str_list = ['a','d','g','b','A','e','C']

In [69]: str_list.sort()    # 排序的list中的元素必须是相同的类型，否则触发TypeError；

In [70]: str_list
Out[70]: ['A', 'C', 'a', 'b', 'd', 'e', 'g']
```

* reverse() 

    原地反转列表；

```python 
reverse(...)
    L.reverse() -- reverse *IN PLACE*
```

```python 
In [74]: lt
Out[74]: [8, 6, 5, 3, 2, 1]

In [75]: lt.reverse()  # 原地反转；

In [76]: lt
Out[76]: [1, 2, 3, 5, 6, 8]

In [77]: lt[::-1]
Out[77]: [8, 6, 5, 3, 2, 1]
```

---

## 查：
* index(value,[start,[stop]])

    在索引号start与stop之间，查找第一个值为value的元素的索引号，返回值为索引号(int);

    索引号的区间：包含start，不包含stop，数学表示区间为：[start,stop)

    如果指定的值不存在于start到stop之间，则引发ValueError；

```python 
index(...)
    L.index(value, [start, [stop]]) -> integer -- return first index of value.
    Raises ValueError if the value is not present.
```

```python 
In [79]: lst
Out[79]: [1, 2, 'i', 'x', 'y']

In [80]: lst.index('i')   # 返回值为：与指定值匹配的第一个元素的索引号；
Out[80]: 2
```

* count(value)

    统计列表中值为value的元素个数；

```python 
count(...)
    L.count(value) -> integer -- return number of occurrences of value
```

```python 
In [82]: lst
Out[82]: [1, 2, 'i', 'x', 'y']

In [83]: lst[::-1]
Out[83]: ['y', 'x', 'i', 2, 1]

In [84]: ltt = lst[::-1]

In [85]: lst.extend(ltt)

In [86]: lst
Out[86]: [1, 2, 'i', 'x', 'y', 'y', 'x', 'i', 2, 1]

In [87]: lst.count('y')  # 返回字符串'y'在列表中出现的次数；
Out[87]: 2
```


* 内置函数len(object)，查看给定对象中包含的元素个数；
```python 
In [88]: len(lst)
Out[88]: 10
```

```python 
len(obj, /)
    Return the number of items in a container.
```

### BOOK推荐：

    《sicp》  计算机程序的构造和解释

    《aupe》  高级Unix环境编程；

    《算法导论》

---

## 其他操作：

* 复制：

lst2 = lst   默认为浅复制；或者叫 引用传递；浅拷贝；

list.copy()

    copy(...)   影子拷贝:只对第一层做copy操作，无法递归；
        L.copy() -> list -- a shallow copy of L

copy()原型：

```python
def copy(lst):
    tmp = []
    for i in lst:
        tmp.append(i)
    return tmp
```

赋值操作，对可变对象是引用传递，对不可变对象是值传递；

如果要对嵌套的容器做深拷贝，可以引用copy模块中的deepcopy函数；


---
