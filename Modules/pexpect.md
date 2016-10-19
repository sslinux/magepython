# 系统批量运维管理器pexpext详解

pexpect可以理解成Linux下的expect的python封装，通过pexpect我们可以实现对ssh,ftp,passwd,telnet等命令进行自动交互。



[pexpect官方文档](http://pexpect.readthedocs.io/en/stable/)

## 安装：
pexpect作为python的一个普通模块，支持pip、easy_install或源码安装方式：
```bash
pip install pexpect
```
Or:  

``bash
easy_install pexpect
```
This version of Pexpect requires Python 3.3 or above, or Python 2.7.


## 源码安装：
采用GitHub平台的项目托管源，安装步骤如下：
```bash 
git clone https://github.com/pexpect/pexpect.git
cd pexpect
(py2go) [sslinux@pythonenv pexpect]$ python setup.py install
```

测试是否安装成功：
```python
In [1]: import pexpect   # 导入模块成功，无报错，说明安装成功；
```

安装需要root权限，如果没有root权限在，还能使用吗？

　　答案是肯定的，你只需要把lib的路径放入sys.path。这样便可以使用pexpect
```python
#!/usr/bin/env python
import sys
sys.path.append('pexpect-4.0.1/build/lib')
```

### 使用方法：
run函数，run函数和os.system()差不多，所不同的是os.system()返回的是整数，而run返回的是字符串；
```python
>>> import pexpect
>>> print(pexpect.run('ping localhost -c 3'))
b'PING localhost (127.0.0.1) 56(84) bytes of data.\r\n64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.078 ms\r\n64 bytes from localhost (127.0.0.1): icmp_seq=2 ttl=64 time=0.065 ms\r\n64 bytes from localhost (127.0.0.1): icmp_seq=3 ttl=64 time=0.066 ms\r\n\r\n--- localhost ping statistics ---\r\n3 packets transmitted, 3 received, 0% packet loss, time 1999ms\r\nrtt min/avg/max/mdev = 0.065/0.069/0.078/0.011 ms\r\n'
```

**spawn 类是通过生成子程序sendline发送命令与expect拿回返回进行交互**
```python
In [1]: import pexpect

In [2]: child = pexpect.spawn('python',timeout=3)

In [3]: child.expect(">>>")
Out[3]: 0

In [4]: child.sendline("exit()")
Out[4]: 5

In [5]: print(child.before)
b'Python 3.5.2 (default, Oct 17 2016, 14:41:46) \r\n[GCC 4.8.5 20150623 (Red Hat 4.8.5-4)] on linux\r\nType "help", "copyright", "credits" or "license" for more information.\r\n\x1b[?1034h'
```
timeout是等待时间，如果超过就会抛出exception，可以 使用except关键字捕获

**设置log:**
```python
In [8]: fout = open('log_file','a')

In [9]: child = pexpect.spawn('su root')

In [11]: import sys

In [12]: child.logfile = sys.stdout

In [13]: child.logfile_send=fout

In [14]: fout.close()
```

```python
(py2go) [sslinux@pythonenv ~]$ cat pexpect_module.py 
#!/usr/bin/env python

from pexpect import pxssh
import getpass

try:
    s = pxssh.pxssh()    # 创建pxssh对象；

    hostname = input('Hostname:')
    username = input('Username:')
    password = getpass.getpass('Password:')

    s.login(server=hostname,username=username,password=password)  # 建立ssh连接

    s.sendline('uptime')  #运行uptime命令；
    s.prompt()            # 匹配系统提示符
    print(s.before)

    s.sendline('df -lh')
    s.prompt()
    print(s.before)

    s.sendline('free -lh')
    s.prompt()
    print(s.before)

    s.logout()    # 断开ssh连接

except pxssh.ExceptionPxssh as e:
    print('pxssh failed on login')
    print(str(e))
```