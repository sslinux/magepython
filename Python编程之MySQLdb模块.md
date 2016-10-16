# Python编程之MySQLdb模块


## python执行环境：
解释器环境与选项；
python解释器启动：
python [options] [-c cmd | filename | - ] [args]

![python_options](/images/python_options.png)

## python解释器环境变量
![python_variables](/images/python_variables.png)

## python代码的测试、调试与探查

如果函数、类或模块的第一行是一个字符串，这个字符串就称为文档字符串(docstrings)

内置函数help()或对象的默认方法__doc__可以显示这些文档字符串；

Example：

In [22]: def Sum(num1,num2):
    ...:     """the sumary of num1 and num2.
    ...:     >>> Sum(2,5)
    ...:     7
    ...:     >>> Sum(12,77)
    ...:     89
    ...:     """
    ...:     return num1 + num2
    ...: 

In [23]: help(Sum)

Help on function Sum in module __main__:

Sum(num1, num2)
    the sumary of num1 and num2.
    >>> Sum(2,5)
    7
    >>> Sum(12,77)
    89
In [24]: Sum.__doc__
Out[24]: 'the sumary of num1 and num2.\n    >>> Sum(2,5)\n    7\n    >>> Sum(12,77)\n    89\n    '
```

## doctest模块：
doctest模块允许在文档字符串内潜入注释以显示各种语句的期望行为，尤其是函数和方法的结果。
- 此处的文档字符串看起来如同一个交互式shell会话；
- 可用于测试文档是否与程序主体保持同步，或基于文档对程序本身做测试；

Example：
使用doctest模块进行测试：
```python
sslinux@sslinux-pygo:~$ cat test.py 
#!/usr/bin/python
#
def add(num1,num2):
    '''
    >>> add(12,43)
    55
    '''
    return num1 + num2
```
```python
In [1]: import test   # 导入自定义test模块；

In [2]: import doctest

In [3]: doctest.testmod(test)
Out[3]: TestResults(failed=0, attempted=1)

In [4]: doctest.testmod(test,verbose=True) #查看测试的详细过程；
Trying:
    add(12,43)
Expecting:
    55
ok
1 items had no tests:
    test
1 items passed all tests:
   1 tests in test.add
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
Out[4]: TestResults(failed=0, attempted=1)
```

如果文档字符串中的结果与预期结果不一致，测试会显示出错的结果信息；

例如，将前述例子文档中的结果修改为错误的结果，其测试结果如下所示：
```python
In [1]: import test

In [2]: import doctest

In [3]: doctest.testmod(test)
**********************************************************************
File "/home/sslinux/test.py", line 7, in test.add
Failed example:
    add(20,5)
Expected:
    26
Got:
    25
**********************************************************************
1 items had failures:
   1 of   2 in test.add
***Test Failed*** 1 failures.
Out[3]: TestResults(failed=1, attempted=2)
```

创建可自测试的模块：
	在模块的尾部添加如下代码即可：
	if __name__ == '__main__':
	    import doctest
	    doctest.testmod()

此类模块在python解释器中直接运行时即能进行自我测试；
```python
sslinux@sslinux-pygo:~$ python test.py 
**********************************************************************
File "test.py", line 7, in __main__.add
Failed example:
    add(20,5)
Expected:
    26
Got:
    25
**********************************************************************
1 items had failures:
   1 of   2 in __main__.add
***Test Failed*** 1 failures.
```

python：
	unitest 统一测试框架


## Python访问MariaDB

依赖于模块：MySQLdb  --依赖于--> easy_install
编译、安装；

setuptools.1.1.1.tar.gz
tar xf setuptools.1.1.1.tar.gz
cd setuptools
python setup.py build
python setup.py install

tar xf MySQLdb.*.tar.gz
cd MySQLdb
python setup.py build
python setup.py install


vim /etc/ld.so.conf.d/mysql.conf
	# 添加MySQL或MariaDB的库文件目录；
ldconfig  # 使其生效；

```python
import MySQLdb as mysql
```
### 创建MySQL连接：
![MySQL_Connections](/images/mysql_connections.png)


conn = mysql.connect(host='10.60.4.167',user='sslinux',passwd='sslinux',db='mydb')
conn.stat()   # 获取服务器状态；
conn.ping()   # 测试连通性；
conn.commit()   # 提交事务；
conn.rollback() # 回滚；
conn.autocommit(1)   # 开启自动提交功能；

# 创建游标
cur = conn.cursor()

cur.close()
cur.execute()    # 向服务器端发送sql语句；
cur.execute('SHOW DATABASES')
cur.fetchall()   # 获取所有的返回结果；
# 返回结果为元组；
cur.fetchone()   # 获取一行；
cur.fetchmany(5) # 获取多行；
cur.scroll(0,mode='absolute')    # 偏移游标到起始位置；

sqlsm = 'create table mydb.t1 (id int auto_increment primary key not null, name char(30))'

cure.execute(sqlsm)

sqlins = 'insert into t1 (name) value ("tom")'
cur.execute(sqlins)

cur.execute('select * form t1')
cur.fetchall()

# 批量插入：
sqlins = 'insert into t1 (name) value ("tom"),("stu1"),("stu2")'

sqlins = 'insert into t1 (name) value (%s)'   # 无论数据类型为何，都用%s;
cur.excute(sqlins,(value1,value2,...valueN))


cur.execute('create table t2 (id int,name varchar(30),gender char(6),age tinyint)')

sqlins = 'insert into t2 (id,name,gerder,age) values (%s,%s,%s,%s)'
cur.execute(sqlins,(0,'tom','male',30))
cur.execute('select * from t2')
cur.fetchall()


# 一次插入多行数据；
datains = ((2,'str2','female',17),(3,'stu3','male',27))
cur.executemany(sqlins,datains)

execute()
executemany()

a = cur.fetchall()  # 返回列表；
a[0]
a[1]
a[2][2]

cur.close() #关闭游标；
conn.close() # 关闭连接；


使用流程：
import MySQLdb as mysql

建立连接:
conn = mysql.connect(host='',user='',passwd='',db='')

创建游标对象：
cur = conn.curson()

发送查询：
	sqlstatement = 'sql statement'
	cur.execute(sqlstatement)
	cur.executemany(sqlstatements)

获取数据：
	cur.execute('select statement')
	cur.fetchone()
	cur.fetchmant(N)
	cur.fetchall()

对fetchall而言：
	result = cur.testchall()
	此时result就是一个列表了，我们可以对其执行所有对列表支持的操作；

关闭：
	cur.close()
	conn.close()


## 练习：
把/etc/passwd文件中的内容的每一行存储在MariaDB的表中；

