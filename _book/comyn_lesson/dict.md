# 字典(dict)

字典是一种key-value结构

---

## 定义及初始化：
d = {}

d = dict()

d = {'a': 1,'b':2}

d = dict([('a':1),('b':2)])   # 可迭代对象的元素必须是一个二元组，二元组的第0个元素为字典的key，第一个元素为字典的value；

d = dict({'a':1,'b':2})  # 不建议使用此种方式定义dict；

d = dict.fromkeys(range(5))   # 传入的可迭代对象为key，值为None；

d = dict.fromkeys(range(5),'abc')   # 传入的可迭代对象的元素为key，值为'abc'

---
---

## 字典的基本操作：

### 增加与修改：
* dict[key] = value 
* dict.update() 
    当key已经存在于字典中时，仅修改该key的value；
    当key不存在于字典中时，则添加一对key-value；

    update方法接受的参数：
        可以是一个字典；{'a':1,'b':2}
        也可以是一个二元组： [('a',1),('b',2)]
    


```python
In [110]: d = dict.fromkeys(range(5),'abc')

In [111]: d
Out[111]: {0: 'abc', 1: 'abc', 2: 'abc', 3: 'abc', 4: 'abc'}

In [112]: d['a'] = 1  # 可以直接使用key作为下标，对某个不存在的key赋值，会增加kv对；

In [113]: d
Out[113]: {0: 'abc', 1: 'abc', 2: 'abc', 3: 'abc', 4: 'abc', 'a': 1}

In [114]: d.update([('c',3),('p',0)]) # update 传入参数和dict一样；

In [115]: d
Out[115]: {0: 'abc', 1: 'abc', 2: 'abc', 3: 'abc', 4: 'abc', 'a': 1, 'p': 0, 'c': 3}

# update方法也可以传入一个字典；
In [116]: d.update({'x':10,'y':20})   # 合并两个字典；如果key已存在，则修改该key的值；

In [117]: d
Out[117]: 
{0: 'abc',
 1: 'abc',
 2: 'abc',
 3: 'abc',
 4: 'abc',
 'y': 20,
 'a': 1,
 'p': 0,
 'x': 10,
 'c': 3}

d.update([('r',2),('d',2)])   等效于：
d.update({'r':2,'d':2})
```

d['a'] = 2 # 当key存在，对下标赋值的时候，会修改这个key对应的value；
           # 当key不存在，则增加元素；

### 删除：

* pop()   

```python 
pop(...)
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    If key is not found, d is returned if given, otherwise KeyError is raised
```

        d.pop(0)  # 从字典删除一个key，并返回其value；删除不存在的key时，会抛出KeyError；

        d.pop(0,'Default')  # 当删除不存在的key，在指定了默认值时，不会抛出KeyError，并且返回默认值；

        有没有default值，只有在key不存在时有区别；

* popitem()

    **随机返回一个kv对的二元组；**

    **对空字典popitem,将抛出KeyError；
    
```python
popitem(...)
    D.popitem() -> (k, v), remove and return some (key, value) pair as a
    2-tuple; but raise KeyError if D is empty.
```

* clear()   # 清空一个字典；

* del d[key]  # del语句；

        修改key：先删除，再添加；

### 访问：

#### 单个元素的访问：
* 通过key访问value，d[key] 

    当key不存在时，抛出KeyError；

* get

    get方法通过key访问value，

    get方法访问不存在的key时，返回默认值，默认值如果未指定则为None；

```python 
get(...)
    D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
```

```python 
In [125]: d.get('a')
Out[125]: 1

In [126]: d.get('a','python')
Out[126]: 1

In [127]: d.get(10)

In [128]: d.get(10,'python')
Out[128]: 'python'
```

* setdefault

    先调用get(k,default),如果k不在字典中，则执行dict[k] = d (新增加一个元素)
```python 
    def setdefault(d,k,default):
        value = d.get(k,default)
        d[k] = value
        return value 
```

```python
setdefault(...)
    D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
```

#### 字典的遍历：

        字典的元素成对出现；

        直接用 for in遍历字典，遍历的是key；


* items
```python
items(...)
    D.items() -> a set-like object providing a view on D's items
```

items 方法返回一个可迭代对象，元素是字典的所有(k,v)对；

```python 
In [133]: for k,v in d.items():
     ...:     print(k,v)
     ...:     
0 abc
1 abc
2 abc
3 abc
4 abc
y 20
a 1
p 0
x 10
c 3
```

* keys

    返回一个可迭代对象，元素是字典所有的key；

* values

    返回一个可迭代对象，元素是字典的所有values；

```python 
values(...)
    D.values() -> an object providing a view on D's values
```

py2 和 py3 的区别：

    py2中，keys、values、items三个方法返回的都是列表；会复制一份内存；

        替代使用：iterkeys(),iteritems(),itervalues()

    py3中，keys、values、items返回的都类似生成器，它并不会复制一份内存；


* copy

```python 
copy(...)
    D.copy() -> a shallow copy of D
    # 影子复制；
```

---
---


### 字典的限制：

    字典的key不能重复；

    **字典的key需要可hash**

    字典本身也是不可hash的，所以字典不能作为字典的key；


```pytyhon 
In [134]: d = {}

In [135]: d[[1,2,3]] = 3
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-135-3fa7e951a0ef> in <module>()
----> 1 d[[1,2,3]] = 3

TypeError: unhashable type: 'list'

In [136]: d[(1,2,3)] = 3

In [137]: d
Out[137]: {(1, 2, 3): 3}
```


## 字典变体：

### 默认字典：

```python 
from collection import defaultdict
d1 = {}
d2 = defaultdict(list)
```

defaultdict初始化的时候，需要传入一个函数，这个函数也叫工厂函数，

当我们使用下标访问一个key的时候，如果这个key不存在，defaultdict会自动调用初始化时传入的函数，

生成一个对象作为这个key的value；

```python 
def f():
    print('f is called')
    return 'a'

d = defaultdict(f)

d['xxx'] = 10
```


```python 
d = {}

for k in range(10):
    for v in range(10):
        if k not in d.keys():
            d[k] = []
        d[k].append(v)


d = defaultdict(list)

for k in range(10):
    for v in range(10):
    d[k].append(v)
```

### 有序字典：

    既要求要存储k-v值，又要有顺序；

```python 
from collection import OrderedDict

d = OrderedDict()
d[0] = 3
d[3] = 4
d[1] = 5

print(d)

for k,v in d.items():
    print(k,v)

# 有序字典，会保持插入顺序；
```



## 字典的实现：

* 拉链法

        i = hash(key) % solt 

        key重复时，就是hash冲突；

        字典攻击(map攻击)

```python 
class Dict:
    def __init__(self,num):
        self.__solts__ = []
        self.num = num
        for _ in range(num):
            self.__solts__.append([])
            
    def put(self,key,value):
        i = hash(key) % self.num
        for p,(k,v) in enumerate(self.__solts__[i]):
            if k == key:
                break
            else:
                self.__solts__[i].append((key,value))
                return 
            solts[i][p] = (key,value)
            
    def get(self,key,value):
        i = hash(key) % self.num
        for k,v in self.__solts__[i]:
            if k == key:
                return v
            raise KeyError(key)

    def keys(self):
        ret = []
        for solt in self.__solts__:
            for k,_ in solt:
                ret.append(k)
        return ret
```




* 开地址法

计算索引位置：

    i = hash(key) % solt 

    i = fn(key,i) 若重复，重新计算其位置；


## 集合的实现：

    集合在底层的实现，就是一个忽略了value的字典；


各种语言对字典的定义：

        golang中只有map类型；
        perl,ruby : hash
        python : dict
        php: 关联数组
        js: object 
        other: map 



