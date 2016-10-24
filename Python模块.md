# python模块(导入、内置、自定义、开源)
## 一、模块：
### 1.模块简介：
 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用python标准库的方法。

类似于函数式编程和面向过程编程，函数式编程则完成一个功能，其他代码用来调用即可，提供了代码的重用性和代码间的耦合。而对于一个复杂的功能来，可能需要多个函数才能完成（函数又可以在不同的.py文件中），n个 .py 文件组成的代码集合就称为模块。

### 2.模块的导入：
在Python中用关键字import来引入某个模块，比如要引用模块math，就可以在文件最开始的地方用import math来引入。在调用math模块中的函数时，必须这样引用：

```python
# 模块名.函数名
例：
In [1]: import math

In [2]: import sys
```

有时候我们只需要用到模块中的某个函数，只需要引入该函数即可，此时可以通过语句
	from 模块名 import 函数名1，函数名2....

例：
```python
import module
#从某个模块导入某个功能；
from module.xx.xx import xx
# 从某个模块导入某个功能，并且给他个别名；
from module.xx.xx import xx as rename
# 从某个模块导入所有
from module.xx.xx import *
```

### 模块分为三种：
- 自定义模块；
- 内置模块；
- 开源模块；

### 模块的安装：
####(1) yum install 模块名
####(2) apt-get install 模块名
####(3) pip 安装；
####(4) 源码安装：
```python
# 需要编译环境：yum -y install python-devel gcc
# 下载源码包： wget http://xxxxxx.tar.gz
# 解压： tar xzvf xxx.tar.gz
# 进入解压目录： cd xxx
# 编译： python steup.py build
# 安装： python setup.py install
```

## 二、自定义模块：
### 1.在python中，每个Python文件都可以作为一个模块，模块的名字就是文件的名字；
例如：
	写一个模块(模块文件要和代码文件在同一目录下)
```python
# vim module_test.py
# 写入如下代码：
#!/usr/bin/env python3
print('自定义 module')

# 调用
# vim test.py
#!/usr/bin/env python3
# 导入自定义模块：
import module_test
执行test.py
```

### 2.模块文件为单独文件夹，文件夹和代码在同一目录下：
![Custom_Module](/images/Custom_Module.png)

导入模块其实就是告诉Python解释器去解释那个py文件
- 导入一个py文件，解释器解释该py文件；
- 导入一个包，解释器解释该包下的__init__.py文件；

### 3.sys.path添加目录：
如果sys.path路径列表没有你想要的路径，可以通过sys.path.append('路径')添加。
通过os模块可以获取各种目录。

## 三、内置模块：
### 1.os模块提供系统级别的操作
os.getcwd()  获取当前工作目录，即当前python脚本工作的目录路径；
```python
In [4]: import os

In [5]: os.getcwd()
Out[5]: '/media/sslinux/Disk-Study/magePython/PPT/MagePython'
```

os.chdir("目录名")  改变当前脚本工作目录；相当于Linux下cd命令；
```python
In [6]: os.chdir('/usr/local')

In [7]: os.getcwd()
Out[7]: '/usr/local'
```

os.pardir 获取当前目录的父目录字符串名：('..')
```python
In [8]: os.pardir
Out[8]: '..'
```

os.mkdir('目录')  生成单级目录；相当于shell中mkdir 目录；
```python
In [10]: os.chdir('/tmp')

In [11]: os.getcwd()
Out[11]: '/tmp'

In [12]: os.mkdir('test')
```

os.makedirs('目录1/目录2') 可生成多层递归目录(相当于Linux下 mkdir -p):
```python
In [14]: os.makedirs('test/python/module/')

In [15]: ll test/python/module/
total 0
```

rmdir('目录') 删除单级空目录，若目录不为空则无法删除,报错；相当于shell中rmdir；
```python
In [16]: os.rmdir('test')
---------------------------------------------------------------------------
OSError                                   Traceback (most recent call last)
<ipython-input-16-c50735c2422d> in <module>()
----> 1 os.rmdir('test')

OSError: [Errno 39] Directory not empty: 'test'

In [17]: os.rmdir('test/python/module')   # 删除空目录是OK的；

In [18]: ll test/python/
total 0

```

os.removedirs('目录')  若目录为空，则删除，并递归到上一层目录，如若也为空，则删除，依此类推；
```python
In [19]: os.removedirs('test/python/')

#a目录中除了有一个b目录外，再没有其它的目录和文件。
#b目录中必须是一个空目录。 如果想实现类似rm -rf的功能可以使用**shutil模块**
```

os.remove() 删除一个文件；
```python
In [21]: os.getcwd()
Out[21]: '/tmp'

In [22]: os.remove('config-err-lM44JA')
```

os.rename("原名","新名") 重命名文件/目录
```python
In [24]: os.makedirs('test/python/osModule')

In [25]: os.listdir('test')
Out[25]: ['python']

In [26]: os.rename('test/python','test/golang')

In [27]: os.listdir('test')
Out[27]: ['golang']
```

os.stat('path/filename')  获取文件/目录信息；
```python
In [28]: os.stat('test/golang')
Out[28]: os.stat_result(st_mode=16893, st_ino=457998, st_dev=23, st_nlink=1, st_uid=1000, st_gid=1000, st_size=16, st_atime=1476420101, st_mtime=1476420101, st_ctime=1476420167)
```

os.sep  输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
```python
# 属性：
In [29]: os.sep
Out[29]: '/'
```

os.linesep 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
```python
In [30]: os.linesep
Out[30]: '\n'
```

os.pathsep  输出用于分隔文件路径的字符串；
```python
In [31]: os.pathsep
Out[31]: ':'
```

os.name   # 输出字符串指示当前使用平台。win  --> 'nt';  Linux-> 'posix'
```python
In [32]: os.name
Out[32]: 'posix'
```

os.system('pwd')   运行shell命令，直接显示
```python
In [33]: os.system('pwd')
/tmp
Out[33]: 0

In [34]: os.system('id sslinux')
uid=1000(sslinux) gid=1000(sslinux) groups=1000(sslinux),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
Out[34]: 0
```

os.environ    显示系统上的环境变量；
```python
In [35]: os.environ
Out[35]: environ({'LOGNAME': 'sslinux', 'HOME': '/home/sslinux', 'QT_ACCESSIBILITY': '1',   # 此处省略N行；
```

os模块的其他语法：   其实就是os子模块： os.path
```python
os.path模块主要用于文件的属性获取，
os.path.abspath(path)  返回path规范化的
os.path.split(path)  将path分割成目录和文件名二元组返回
os.path.dirname(path)  返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  如果path是绝对路径，返回True
os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
```

### 2.sys模块 用于提供对解释器相关的操作；
```python

sys.argv   命令行参数List，第一个元素是程序本身路径
sys.modules 返回系统导入的模块字段，key是模块名，value是模块
sys.exit(n)        退出程序，正常退出时exit(0)
sys.version        获取Python解释程序的版本信息
sys.maxint         最大的Int值
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform       返回操作系统平台名称
sys.stdout.write('please:')
val = sys.stdin.readline()[:-1]
sys.modules.keys() 返回所有已经导入的模块名
sys.modules.values() 返回所有已经导入的模块
sys.exc_info()     获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
sys.exit(n)        退出程序，正常退出时exit(0)
sys.hexversion     获取Python解释程序的版本值，16进制格式如：0x020403F0
sys.version        获取Python解释程序的
sys.api_version    解释器的C的API版本
sys.version_info
‘final’表示最终,也有’candidate’表示候选，serial表示版本级别，是否有后继的发行
sys.displayhook(value)      如果value非空，这个函数会把他输出到sys.stdout，并且将他保存进__builtin__._.指在python的交互式解释器里，’_’ 代表上次你输入得到的结果，hook是钩子的意思，将上次的结果钩过来
sys.getdefaultencoding()    返回当前你所用的默认的字符编码格式
sys.getfilesystemencoding() 返回将Unicode文件名转换成系统文件名的编码的名字
sys.setdefaultencoding(name)用来设置当前默认的字符编码，如果name和任何一个可用的编码都不匹配，抛出 LookupError，这个函数只会被site模块的sitecustomize使用，一旦别site模块使用了，他会从sys模块移除
sys.builtin_module_names    Python解释器导入的模块列表
sys.executable              Python解释程序路径
sys.getwindowsversion()     获取Windows的版本
sys.copyright      记录python版权相关的东西
sys.byteorder      本地字节规则的指示器，big-endian平台的值是’big’,little-endian平台的值是’little’
sys.exc_clear()    用来清除当前线程所出现的当前的或最近的错误信息
sys.exec_prefix    返回平台独立的python文件安装的位置
sys.stderr         错误输出
sys.stdin          标准输入
sys.stdout         标准输出
sys.platform       返回操作系统平台名称
sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.maxunicode     最大的Unicode值
sys.maxint         最大的Int值
sys.version        获取Python解释程序的版本信息
sys.hexversion     获取Python解释程序的版本值，16进制格式如：0x020403F0
```

### 3.hashlib模块：
Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）用于加密相关的操作，代替了md5模块和sha模块，主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法

(1) MD5算法：
```python
In [36]: import hashlib

In [37]: hash = hashlib.md5()

In [38]: hash.update('kalaguiyin'.encode('utf-8'))

In [39]: hash.hexdigest()
Out[39]: '69ef6db4778d79bf5373788b96c9f1e3'
```
- 1.首先从python直接导入hashlib模块；
- 2.调用hashlib里的md5()生成一个md5 hash对象；
- 3.生成hash对象后，就可以用update方法对字符串进行md5加密的更新处理；
- 4.继续调用update方法会在前面加密的基础上更新加密；
- 5.在3.x的版本上update里面需要加.encode('utf-8'),而2.x的版本不需要；

(2) sha1算法：
```python
In [40]: import hashlib

In [41]: sha_1 = hashlib.sha1()

In [42]: sha_1.update('sslinux'.encode('utf-8'))

In [43]: sha_1.hexdigest()
Out[43]: '5f822022886a2ba661970d518afb8358851d09ac'
```

(3) sha256算法：
```python
In [44]: import hashlib

In [45]: sha_256 = hashlib.sha256()

In [46]: sha_256.update('sslinux'.encode('utf-8'))

In [47]: sha_256.hexdigest()
Out[47]: 'a10219f156a74bf5cebb1f638a7842626b550e8a753c8d6173dedf10c03fa8e0'
```

(4) sha384算法：
```python
In [48]: import hashlib

In [49]: sha_384 = hashlib.sha384()

In [50]: sha_384.update('sslinux'.encode('utf-8'))

In [51]: sha_384.hexdigest()
Out[51]: '085f0736665f9a7230d3fd1d48dd9340a4565b3e0b7694d6e78807da70a1b1b37edf8b363862385d29b1de952fc4b08b'
```

(5) sha512算法：
```python
In [52]: import hashlib

In [53]: sha_512 = hashlib.sha512()

In [54]: sha_512.update('sslinux'.encode('utf-8'))

In [55]: sha_512.hexdigest()
Out[55]: '2cf946532501afa3589ffabc02f24d5ee41461f9043382f319285e5f2c2cba808eaa571ace79d1789ad24f6a3515390d90462b96ddfaab7846a4cf6fb9b0fd65'
```

(6) 对加密算法中添加自定义key再来做加密，防止被撞库破解：
```python
In [56]: md5_key = hashlib.md5('jwljflsdjflsdjfl'.encode('utf-8'))

In [57]: md5_key.update('sslinux'.encode('utf-8'))

In [58]: md5_key.hexdigest()
Out[58]: '12d3410d81876eeffe219d72d0c57a60'
```

### 注：hmac模块，它内部对我们创建key和内容在进行处理然后再加密；
```python
In [59]: import hmac

In [60]: hm = hmac.new('sslinux'.encode('utf-8'))

In [61]: hm.update('hellowo'.encode('utf-8'))

In [62]: print(hm.hexdigest())
cba144260de2adf6e5a08e2d95c51e79
```

### 4.configparser模块 (在2.x版本为：ConfigParser)

用于对特定的配置文件进行操作；

配置文件的格式是： [] 包含的叫section，section下有option=value这样的键值；

用法：
读取配置方法：
```python
-read(filename)  # 直接读取ini文件内容；
-sections()      # 得到所有的section，并以列表的形式返回；
-options(section)  # 得到该section的所有option；
-iterms(section)   # 得到该section的所有键值对；
-get(section,option) # 得到section中option的值，返回为string类型；
-getint(section,option) #得到section中option的值，返回为int类型；
```

写入配置方法：
```python
-add_section(section)   # 添加一个新的section；
-set(section,option,value)  # 对section中的option进行设置；
# 需要调用write将内容写入配置文件中；
```

### 案例：

**测试配置文件：**
[sslinux]
passwd = 123456
card = 625813964
limi5 = 1500000
debt = 0
interest = 0.5

[mayun]
passwd = 234567
card = 623052909
limit = 150000
debt=0
interest = 0.5

[donghang]
passwd = 234567
card = 6230582403
limit = 150000
debt = 0
interest = 0.5

```python
#!/usr/bin/env python3
# _*_ encoding: utf-8 _*_

import configparser

#生成config对象：
config = config.ConfigParser()

# 用config对象读取配置文件；
config.read('test_con')

# 以列表形式返回所有的section：
sections = config.sections()
print('sections:',sections)

# 得到指定section的所有option
options = config.options("sslinux")
print('options:',options)

# 得到指定section的所有键值对：
kvs = config.items("sslinux")
print('kvs:',kvs)

# 指定section，option读取值：
str_val = config.get('sslinux','card')
int_val = config.getint('sslinux','limit')
print('sslinux的card:',str_val)
print('sslinux的limit:',int_val)

# 修改写入配置文件：
# 更新指定section，option的值：
config.set('mayun','limit','110000')
int_val = config.getint('mayun','limit')
print('mayun的limit:',int_val)

# 写入指定section增加新option和值；
config.set("sslinux","age","21")
int_val = config.getint("sslinux","age")
print("SSLinux的age",int_val)

# 增加新的section
config.add_section('duobian')
config.set('duobian','age','21')

# 写回配置文件：
config.write(open("test_con",'w')
```

#### configparser 实例所支持的方法：
```python
In [13]: config = configparser.ConfigParser()

In [14]: config.
          config.add_section     config.defaults        config.has_option      config.OPTCRE          config.popitem         config.readfp           
          config.BOOLEAN_STATES  config.get             config.has_section     config.OPTCRE_NV       config.read            config.remove_option    
          config.clear           config.getboolean      config.items           config.options         config.read_dict       config.remove_section  >
          config.converters      config.getfloat        config.keys            config.optionxform     config.read_file       config.SECTCRE          
          config.default_section config.getint          config.NONSPACECRE     config.pop             config.read_string     config.sections         
```

### 5.Subprocess模块
subprocess最早是在2.4版本中引入的。

subprocess模块用来生成子进程，并可以通过管道连接它们的输入/输出/错误，以及获得它们的返回值。

它用来代替多个旧模块和函数:
```
os.system
os.spawn*
os.popen*
popen2.*
commands.*
```
> 运行python的时候，我们都是在创建并运行一个进程。

> 像Linux进程那样，一个进程可以fork一个子进程，并让这个子进程exec另外一个程序。

> 在Python中，我们通过标准库中的subprocess包来fork一个子进程，并运行一个外部的程序。

> subprocess包中定义有数个创建子进程的函数，这些函数分别以不同的方式创建子进程，所以我们可以根据需要来从中选取一个使用。

> 另外subprocess还提供了一些管理标准流(standard stream)和管道(pipe)的工具，从而在进程间使用文本通信。

#### 使用：
(1) call
执行命令，返回状态码 shell=True,允许shell命令是字符串形式：
```python
In [14]: import subprocess

In [15]: ret = subprocess.call(['ls','-l'],shell=False)
total 10
-rwxrwxrwx 1 sslinux sslinux 1123 10月 14 14:29 configParser.py
-rwxrwxrwx 1 sslinux sslinux  765 10月 14 14:28 ConfigParser.py
-rwxrwxrwx 1 sslinux sslinux    0 10月 13 08:26 passwd.txt
-rwxrwxrwx 1 sslinux sslinux   64 10月 13 08:26 QuickStart.py
-rwxrwxrwx 1 sslinux sslinux  220 10月 13 08:26 send_mail.py
-rwxrwxrwx 1 sslinux sslinux  247 10月 14 14:13 test_con

In [16]: type(ret)   # 返回结果为int类型；
Out[16]: int

In [17]: print(ret)   # 依此判断，返回的是执行结果状态码；
0
```

(2) check_all
执行命令，如果执行状态码是0，则返回0，否则抛出异常；
```python
In [18]: subprocess.check_call(["ls","-l"])
total 10
-rwxrwxrwx 1 sslinux sslinux 1123 10月 14 14:29 configParser.py
-rwxrwxrwx 1 sslinux sslinux  765 10月 14 14:28 ConfigParser.py
-rwxrwxrwx 1 sslinux sslinux    0 10月 13 08:26 passwd.txt
-rwxrwxrwx 1 sslinux sslinux   64 10月 13 08:26 QuickStart.py
-rwxrwxrwx 1 sslinux sslinux  220 10月 13 08:26 send_mail.py
-rwxrwxrwx 1 sslinux sslinux  247 10月 14 14:13 test_con
Out[18]: 0

In [19]: subprocess.check_call("exit 1",shell=True)
---------------------------------------------------------------------------
CalledProcessError                        Traceback (most recent call last)
<ipython-input-19-d48cff9735f3> in <module>()
----> 1 subprocess.check_call("exit 1",shell=True)

/usr/lib/python3.5/subprocess.py in check_call(*popenargs, **kwargs)
    579         if cmd is None:
    580             cmd = popenargs[0]
--> 581         raise CalledProcessError(retcode, cmd)
    582     return 0
    583 

CalledProcessError: Command 'exit 1' returned non-zero exit status 1
```

(3) check_output
执行命令，如果状态码是0，则返回执行结果，否则抛出异常；
```python
In [20]: subprocess.check_output(["echo","Hello World!"])
Out[20]: b'Hello World!\n'

In [21]: subprocess.check_output("exit 1",shell=True)
---------------------------------------------------------------------------
CalledProcessError                        Traceback (most recent call last)
<ipython-input-21-257ed6e3f355> in <module>()
----> 1 subprocess.check_output("exit 1",shell=True)

/usr/lib/python3.5/subprocess.py in check_output(timeout, *popenargs, **kwargs)
    624 
    625     return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
--> 626                **kwargs).stdout
    627 
    628 

/usr/lib/python3.5/subprocess.py in run(input, timeout, check, *popenargs, **kwargs)
    706         if check and retcode:
    707             raise CalledProcessError(retcode, process.args,
--> 708                                      output=stdout, stderr=stderr)
    709     return CompletedProcess(process.args, retcode, stdout, stderr)
    710 

CalledProcessError: Command 'exit 1' returned non-zero exit status 1
```

(4) subprocess.Popen(...)
用于执行复杂的系统命令：
参数：
- args: shell命令，可以是字符串或者序列类型 (如：list,元组)
- bufsize: 指定缓冲。0无缓冲，1行缓冲，其他 缓冲区大小，负值，系统缓冲；
- stdin,stdout,stderr: 分别表示程序的标准输入、输出、错误句柄；
- preexec_fn: 只在Unix平台下有效，用于指定一个可执行对象(callable object),它将在子进程运行之前被调用；
- close_sfs: 在windows平台下，如果close——fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道；
	所以不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin,stdout,stderr)
- shell：同上；
- cwd：用于设置子进程的当前目录；
- env：用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承；
- universal_newlines: 不同系统的换行符不同，True -> 统一使用\n
- startupinfo 与 createionflags只在windows下有效
	将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等；

例：
```python
In [22]: import subprocess

In [23]: res = subprocess.Popen(["mkdir","sub"])

In [24]: res2 = subprocess.Popen("mkdir sub_1",shell=True)

In [25]: ls
configParser.py*  ConfigParser.py*  passwd.txt*  QuickStart.py*  send_mail.py*  sub/  sub_1/  test_con*
```

#### 终端输入的命令分为两种：
- 输入即可得到输出，如：ifconfig
- 输入进行某环境，依赖再输入，如：python

```python
In [27]: obj = subprocess.Popen("sudo mkdir cwd",shell=True,cwd='/home/',)
```

```python

import subprocess
 
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write('print 1 \n ')
obj.stdin.write('print 2 \n ')
obj.stdin.write('print 3 \n ')
obj.stdin.write('print 4 \n ')
obj.stdin.close()
 
cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()
 
print cmd_out
print cmd_error
```

```python
mport subprocess
 
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write('print 1 \n ')
obj.stdin.write('print 2 \n ')
obj.stdin.write('print 3 \n ')
obj.stdin.write('print 4 \n ')
 
out_error_list = obj.communicate()
print out_error_list
```

```python

import subprocess
 
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out_error_list = obj.communicate('print "hello"')
print out_error_list
```

### 6.时间模块：
(1) time模块
time.time()函数返回从1970年1月1日以来的秒数，这是一个浮点数；

```python
In [29]: import time

In [30]: time.time()
Out[30]: 1476429527.3847122
```

```python
print(time.clock()) #返回处理器时间,3.3开始已废弃
print(time.process_time()) #返回处理器时间,3.3开始已废弃
print(time.time()) #返回当前系统时间戳
print(time.ctime()) #输出Tue Jan 26 18:23:48 2016 ,当前系统时间
In [32]: time.ctime()
Out[32]: 'Fri Oct 14 15:20:30 2016'

print(time.ctime(time.time()-86640)) #将时间戳转为字符串格式
print(time.gmtime(time.time()-86640)) #将时间戳转换成struct_time格式
print(time.localtime(time.time()-86640)) #将时间戳转换成struct_time格式,但返回 的本地时间
In [34]: time.localtime(time.time()-86640)
Out[34]: time.struct_time(tm_year=2016, tm_mon=10, tm_mday=13, tm_hour=15, tm_min=17, tm_sec=58, tm_wday=3, tm_yday=287, tm_isdst=0)

print(time.mktime(time.localtime())) #与time.localtime()功能相反,将struct_time格式转回成时间戳格式
#time.sleep(4) #sleep
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) ) #将struct_time格式转成指定的字符串格式

print(time.strptime("2016-01-28","%Y-%m-%d") ) #将字符串格式转换成struct_time格式
```

(2) datetime模块
```python
print(datetime.date.today()) #输出格式 2016-01-26
print(datetime.date.fromtimestamp(time.time()-864400) ) #2016-01-16 将时间戳转成日期格式
current_time = datetime.datetime.now() #
print(current_time) #输出2016-01-26 19:04:30.335935
print(current_time.timetuple()) #返回struct_time格式
In [44]: print(current_time.timetuple())
time.struct_time(tm_year=2016, tm_mon=10, tm_mday=14, tm_hour=15, tm_min=52, tm_sec=55, tm_wday=4, tm_yday=288, tm_isdst=-1)

print(current_time.replace(2014,9,12)) #输出2014-09-12 19:06:24.074900,返回当前时间,但指定的值将被替换
In [46]: print(current_time.replace(2010,9,3))
2010-09-03 15:52:55.600350

str_to_date = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M") #将字符串转换成日期格式
new_date = datetime.datetime.now() + datetime.timedelta(days=10) #比现在加10天
new_date = datetime.datetime.now() + datetime.timedelta(days=-10) #比现在减10天
new_date = datetime.datetime.now() + datetime.timedelta(hours=-10) #比现在减10小时
new_date = datetime.datetime.now() + datetime.timedelta(seconds=120) #比现在+120s
print(new_date)
```


![time_arrtribute](/images/time_arrtribute.jpg)
![time_arrtribute2](/images/time_arrtribute2.png)


### 7、Logging日志模块
[logging模块详解](http://www.cnblogs.com/darkpig/p/5924820.html)

1、简单日志打印：
```python

#导入日志模块
import logging
#简单级别日志输出
logging.debug('[debug 日志]')
logging.info('[info 日志]')
logging.warning('[warning 日志]')
logging.error('[error 日志]')
logging.critical('[critical 日志]')
```

输出：
```python
WARNING:root:[warning 日志]
ERROR:root:[error 日志]
CRITICAL:root:[critical 日志]
```

可见，默认情况下python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，  
这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET）  

默认的日志格式为:  
     日志级别：Logger名称：用户输出消息。  


2、灵活配置日志级别，日志格式，输出位置
```python
(py2go) [sslinux@pythonenv python]$ cat log_test.py 
#!/usr/bin/env python3

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log.log',
                    filemode='w')
 
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
```

```bash
(py2go) [sslinux@pythonenv python]$ cat log.log 
Mon, 17 Oct 2016 18:34:46 log_test.py[line:11] DEBUG debug message
Mon, 17 Oct 2016 18:34:46 log_test.py[line:12] INFO info message
Mon, 17 Oct 2016 18:34:46 log_test.py[line:13] WARNING warning message
Mon, 17 Oct 2016 18:34:46 log_test.py[line:14] ERROR error message
Mon, 17 Oct 2016 18:34:46 log_test.py[line:15] CRITICAL critical message
```

### 在logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有

- filename：   用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。

- filemode：   文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。

- format：     指定handler使用的日志显示格式。

- datefmt：    指定日期时间格式。（datefmt='%a, %d %b %Y %H:%M:%S',%p）

- level：      设置rootlogger（后边会讲解具体概念）的日志级别

- stream：     用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件，默认为sys.stderr。

若同时列出了filename和stream两个参数，则stream参数会被忽略。

### format参数中可能用到的格式化串：
- %(name)s             Logger的名字
- %(levelno)s          数字形式的日志级别
- %(levelname)s     文本形式的日志级别
- %(pathname)s     调用日志输出函数的模块的完整路径名，可能没有
- %(filename)s        调用日志输出函数的模块的文件名
- %(module)s          调用日志输出函数的模块名
- %(funcName)s     调用日志输出函数的函数名
- %(lineno)d           调用日志输出函数的语句所在的代码行
- %(created)f          当前时间，用UNIX标准的表示时间的浮 点数表示
- %(relativeCreated)d    输出日志信息时的，自Logger创建以 来的毫秒数
- %(asctime)s                 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
- %(thread)d                  线程ID。可能没有
- %(threadName)s         线程名。可能没有
- %(process)d               进程ID。可能没有
- %(message)s             用户输出的消息

3、Logger，Handler，Formatter，Filter的概念

logging.basicConfig()（用默认日志格式（Formatter）为日志系统建立一个默认的流处理器（StreamHandler），
设置基础配置（如日志级别等）并加到root logger（根Logger）中）这几个logging模块级别的函数，
另外还有一个模块级别的函数是logging.getLogger([name])（返回一个logger对象，如果没有指定名字将返回root logger）

1).logging库提供了多个组件：Logger、Handler、Filter、Formatter。

Logger       对象提供应用程序可直接使用的接口，
Handler      发送日志到适当的目的地，
Filter          提供了过滤日志信息的方法，
Formatter   指定日志显示格式。

```python
# 创建一个logger
logger = logging.getLogger()
#创建一个带用户名的logger
logger1 = logging.getLogger('liuyao')
#设置一个日志级别
logger.setLevel(logging.INFO)
logger1.setLevel(logging.INFO)
#创建一个handler，用于写入日志文件
fh = logging.FileHandler('log.log')
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
# 定义handler的输出格式formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
#logger.addFilter(filter)
logger.addHandler(fh)
logger.addHandler(ch)
# 给logger1添加handler
#logger1.addFilter(filter)
logger1.addHandler(fh)
logger1.addHandler(ch)
#给logger添加日志
logger.info('logger info message')
logger1.info('logger1 info message')
```
输出：
```
2016-02-03 21:11:38,739 - root - INFO - logger info message
2016-02-03 21:11:38,740 - liuyao - INFO - logger1 info message
2016-02-03 21:11:38,740 - liuyao - INFO - logger1 info message
```

对于等级：
```
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
```

## 8.json和pickle模块
用于序列化的两个模块
-    json，用于字符串 和 python数据类型间进行转换

-    pickle，用于python特有的类型 和 python的数据类型间进行转换


Json模块提供了四个功能：dumps、dump、loads、load

pickle模块提供了四个功能：dumps、dump、loads、load

```python
#!/usr/bin/env python3

import pickle

data = {'k1':123,'k2':'Hello'}

# pickle.dumps 将数据通过特殊的形式转换为只有python语言识别的字符串；
p_str = pickle.dumps(data)
print(p_str)

# pickle.dump 将数据通过特殊的形式转换为只有python语言认识的字符串，并写入文件
with open('result.pk','w') as fp:
    pickle.dump(data,fp)

import json

# json.dumps 将数据通过特殊的形式转换为所有程序语言都认识的字符串
j_str = json.dumps(data)
print(j_str)

# json.dump 将数据通过特殊的形式转换为所有程序语言都认识的字符串，并写入文件；
with open('result.json','w') as fp:
    json.dump(data,fp)
```

### json模块：
    四个功能： dumps、dump、loads，load
1). dumps
```python

name = {'liuyao':'["age",12]',
        'yaoyai':'["age",21]'}
print(name)
print(type(name))
a = json.dumps(name)
print(a)
print(type(a))
```

```python
{'yaoyai': '["age",21]', 'liuyao': '["age",12]'}
<class 'dict'>
{"yaoyai": "[\"age\",21]", "liuyao": "[\"age\",12]"}
<class 'str'>
```

## shelve 模块 

shelve模块是一个简单的k,v将内存数据通过文件持久化的模块，可以持久任何pickle可支持的python数据格式；
```python
#!/usr/bin/env python3

# shelve模块简介：

import shelve

d = shelve.open('shelve_test')   # 打开一个文件；

class Test(object):
    def __init__(self,n):
        self.n = n

t = Test(123)
t2 = Test(123334)

name = ['alex','rain','test']

d["test"] = name   #持久化列表
d["t1"] = t        #持久化类
d["t2"] = 52

d.close()
```

## random模块

random模块是专门用来生成随机数的。

1）random.random 
random.random() 用于生成一个0到1的随机浮点数：0 <= n < 1.0

例： 
```python
>>> import random
>>> print(random.random)
<built-in method random of Random object at 0x17f4388>
>>> print(random.random())
0.5438051254769491
```

2) random.uniform
random.uniform的函数原型为：random.uniform(a,b),用于生成一个指定范围内的随机浮点数，两个参数其中一个是上限，一个是下限。

如果a>b,则生成的随机数n: a <= n <= b
如果a<b,则b <= n <= b
```python 
>>> random.uniform(5,10)
5.930611332627718
>>> random.uniform(10,10)
10.0
>>> random.uniform(10,5)
5.772749826995059
```

3) random.randint
random.randint()的函数原型为：random.randint(a,b),用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b,下限必须小于上限；
```python
>>> random.randint(10,20)
14
>>> random.randint(10,20)
19
```

4) random.randrange
random.randrange的函数原型为： random.randrange([start],stop[,step]),从指定的范围内，按指定的基数递增的集合中获取一个随机数；
如：random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。random.randrange(10, 100, 2)在结果上与 random.choice(range(10, 100, 2) 等效。

例：
```python
>>> random.randrange(1,37,2)
1
>>> random.randrange(1,37,2)
17
>>> random.randrange(1,37,2)
35
>>> random.randrange(1,37,2)
33
```

5) random.choice
random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。

sequence在python中不是一种特定的数据类型，而是泛指一系列的类型。

list、tuple、字符串都属于sequence。

例：
```python
>>> random.choice('SsLinux')
'L'
>>> random.choice('SsLinux')
'u'
>>> random.choice('SsLinux')
'i'
>>> random.choice('SsLinux')
's'
```

6) random.shuffle
random.shuffle的函数原型为：random.shuffle(x[,random]),用于就爱你个一个列表中的元素打乱，

例如：
```python
>>> l = ["Python","is","simple","and so on..."]
>>> random.shuffle(l)
>>> print(l)
['and so on...', 'Python', 'simple', 'is']
```

7）random.sample
random.sample的函数原型为： random.sample(sequence,k),从指定序列中随机获取指定长度的片段；sample函数不会修改原有序列；
```python
>>> li = [1,2,3,4,5,6,7,8,9,10]
>>> slice = random.sample(li,5)
>>> print(slice)
[5, 4, 9, 8, 6]
>>> print(li)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**随机码验证实例：**
```python
#!/usr/bin/env python3

import random
checkcode = ''
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))   #chr(i, /)  Return a Unicode string of one character with ordinal i;
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)

print(checkcode)
```

# 开源模块：
## 1、pexpect
[系统批量运维管理器pexpect详解](Modules/pexpect.md)
## 2、paramiko
[系统批量运维管理器paramiko详解](Modules/paramiko.md)
## 3、Fabric
[系统批量运维管理器fabric详解](Modules/fabric.md)

