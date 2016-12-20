# bytes  bytearray

**str是文本序列**

## bytes是字节序列

* 文本是有编码的(utf-8,gbk,GB18030等)
* 字节没有编码这种说法
* 文本的编码指的是字符如何使用字节来表示


## pytho3字符串默认使用utf-8编码：

```python
In [1]: s = "马哥教育"

In [2]: type(s)
Out[2]: str

In [3]: s
Out[3]: '马哥教育'

In [4]: s.encode()  # 把字符串编码为bytes
Out[4]: b'\xe9\xa9\xac\xe5\x93\xa5\xe6\x95\x99\xe8\x82\xb2'

In [5]: b = s.encode()  # 把字符串编码为bytes

In [6]: b
Out[6]: b'\xe9\xa9\xac\xe5\x93\xa5\xe6\x95\x99\xe8\x82\xb2'

In [7]: b.decode()
Out[7]: '马哥教育'

In [8]: '马'.encode()
Out[8]: b'\xe9\xa9\xac'

In [9]: bin(0xe9)
Out[9]: '0b11101001'

In [10]: bin(0xa9)
Out[10]: '0b10101001'

In [11]: bin(0xac)
Out[11]: '0b10101100'
```

```python 
bin(number, /)   # 将一个整数转换为二进制；
    Return the binary representation of an integer.
    
    >>> bin(2796202)
    '0b1010101010101010101010'
```

```python 
encode(...) method of builtins.str instance  # 按指定编码方式将字符串转换为bytes；
    S.encode(encoding='utf-8', errors='strict') -> bytes
    
    Encode S using the codec registered for encoding. Default encoding
    is 'utf-8'. errors may be given to set a different error
    handling scheme. Default is 'strict' meaning that encoding errors raise
    a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
    'xmlcharrefreplace' as well as any other name registered with
    codecs.register_error that can handle UnicodeEncodeErrors.
```

```python 
In [14]: s.encode('GBK')
Out[14]: b'\xc2\xed\xb8\xe7\xbd\xcc\xd3\xfd'
# 使用不同的编码方式，得到的结果明显不一样；
In [15]: s.encode()
Out[15]: b'\xe9\xa9\xac\xe5\x93\xa5\xe6\x95\x99\xe8\x82\xb2'

In [16]: b = s.encode()

In [17]: b
Out[17]: b'\xe9\xa9\xac\xe5\x93\xa5\xe6\x95\x99\xe8\x82\xb2'
```

## 解码：
```python
In [16]: b = s.encode()   

In [17]: b
Out[17]: b'\xe9\xa9\xac\xe5\x93\xa5\xe6\x95\x99\xe8\x82\xb2'

In [18]: type(b)
Out[18]: bytes

In [19]: b.decode()   # bytes.decode()  把bytes转化为str；
Out[19]: '马哥教育'

In [20]: b.decode('GBK')   # 因为由s编码到b的时候，使用的编码方式不是GBK，所以此处无法使用GBK解码；
---------------------------------------------------------------------------
UnicodeDecodeError                        Traceback (most recent call last)
<ipython-input-20-041bea7b9d7a> in <module>()
----> 1 b.decode('GBK')

UnicodeDecodeError: 'gbk' codec can't decode byte 0xac in position 2: illegal multibyte sequence
```

```python
In [21]: b = s.encode('GBK')

In [22]: type(b)
Out[22]: bytes

In [23]: b
Out[23]: b'\xc2\xed\xb8\xe7\xbd\xcc\xd3\xfd'

In [24]: b.decode('GBK')   # 此处编码、解码使用相同的编码格式，是可以的，也是推荐的；
Out[24]: '马哥教育'
```

## bytes
* bytes 由str通过encode方法转化得到；
* 通过b前缀定义bytes；

```python 
In [25]: b = b'\xe9\xa9\xac'

In [26]: type(b)
Out[26]: bytes

In [27]: b
Out[27]: b'\xe9\xa9\xac'

In [28]: b = b'abc'

In [29]: type(b)
Out[29]: bytes

In [30]: b
Out[30]: b'abc'

In [31]: b.decode()
Out[31]: 'abc'
```

bytes还可以使用bytes函数，通过以下方式获得：
```python 
 |  bytes(iterable_of_ints) -> bytes
 |  bytes(string, encoding[, errors]) -> bytes
 |  bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
 |  bytes(int) -> bytes object of size given by the parameter initialized with null bytes
 |  bytes() -> empty bytes object
```

### bytes的操作

    除了encode外，str操作，都有bytes的版本，但是传入的参数也必须是bytes类型；

```python 
In [39]: b'abc'.find('b')   # 参数必须是bytes，这里传入的参数是str；
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-39-e88c50f98451> in <module>()
----> 1 b'abc'.find('b')   # 参数必须是bytes，这里传入的参数是str；

TypeError: a bytes-like object is required, not 'str'

In [40]: b'abc'.find(b'b')  # 这里传入的是bytes类型，所以能正常返回；
Out[40]: 1
```


```python 
In [41]: '马哥教育'.encode().find(b'\xa9')  # bytes的操作是按字节来的；
Out[41]: 1

In [42]: '马哥教育'.encode()
Out[42]: b'\xe9\xa9\xac\xe5\x93\xa5\xe6\x95\x99\xe8\x82\xb2'

In [43]: len('马哥教育'.encode())  # 这里使用的是12个字节；
Out[43]: 12
```

```python 
In [47]: b.decode() # 转化为str
Out[47]: 'abc'

In [48]: b.hex() # 转化为16进制
Out[48]: '616263'

In [49]: 0xe9
Out[49]: 233
```

---
---

## bytearray

bytearray 是bytes的可变版本；

str和bytes是不可变的；

```python 
In [51]: b = b'abc'

In [52]: b[1]
Out[52]: 98

In [53]: b[1] = b'B'   # bytes是不可变的；
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-53-77f7c5b425ec> in <module>()
----> 1 b[1] = b'B'

TypeError: 'bytes' object does not support item assignment
```

定义：

```python 
 |  bytearray(iterable_of_ints) -> bytearray
 |  bytearray(string, encoding[, errors]) -> bytearray
 |  bytearray(bytes_or_buffer) -> mutable copy of bytes_or_buffer
 |  bytearray(int) -> bytes array of size given by the parameter initialized with null bytes
 |  bytearray() -> empty bytes array
```

```python 
In [55]: b
Out[55]: b'abc'

In [56]: type(b)
Out[56]: bytes

In [57]: b = bytearray(b)

In [58]: type(b)
Out[58]: bytearray

In [59]: b
Out[59]: bytearray(b'abc')

In [60]: b[1] = int(b'B'.hex(),16)  # bytearray 是可变的；

In [61]: b
Out[61]: bytearray(b'aBc')
```

* bytearray 是可变的，

* 可以用来做图片处理

* 相对bytes来说，多了insert,append,extend,pop,remove,clear,reverse等方法；

* 并且支持索引操作；

**bytearray的append方法：**
```python 
append(self, item, /)
    Append a single item to the end of the bytearray.
    
    item
      The item to be appended.
```

```python 
In [63]: type(b)
Out[63]: bytearray

In [64]: b
Out[64]: bytearray(b'aBc')

In [65]: b.append(b'b')  # insert,append,remove,count参数必须是int；
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-65-f076e736511c> in <module>()
----> 1 b.append(b'b')  # insert,append,remove,count参数必须是int；

TypeError: an integer is required
```

```python 
In [66]: b.append(1000000000) # 此处的int参数必须在0~256这个范围内，即8位无符号整数
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-66-1991a81c5b24> in <module>()
----> 1 b.append(1000000000) # 此处的int参数必须在0~256这个范围内，即8位无符号整数

ValueError: byte must be in range(0, 256)
```

```python 
In [85]: b = bytearray('kalaguiyin','utf-8')   # 将一个字符串使用bytearray函数转换为bytearray；

In [86]: b
Out[86]: bytearray(b'kalaguiyin')

In [87]: type(b)
Out[87]: bytearray

In [88]: b.extend(b' love')                   # 对bytearray对象扩展一个bytes对象；

In [89]: b
Out[89]: bytearray(b'kalaguiyin love')

In [90]: b.extend('python'.encode())          # 先对str编码成bytes，再做扩展；

In [91]: b
Out[91]: bytearray(b'kalaguiyin lovepython')
```


