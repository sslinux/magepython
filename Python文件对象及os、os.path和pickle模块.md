# Python文件对象及os、os.path和pickle模块

### 文件系统和文件：
文件系统是OS用于明确磁盘或分区上的文件的方法和数据结构——即在磁盘上组织文件的方法；

计算机文件(或称文件、电脑档案、档案),是存储在某种长期储存设备或临时存储设备中的一段数据流，并且归属于计算机文件系统管理之下；

概括来讲：

	文件是计算机中由OS管理的具有名字的存储区域；

	在Linux系统上，文件被看作是字节序列；

套接字文件、命名管道，都可以通过文件访问接口来访问；

### Python打开文件：
Python内置函数open()用于打开文件和创建文件对象；

	open(name[,mode [,bufsize]])

open方法可以接收三个参数：文件名、模式和缓冲区参数；

	open函数返回的是一个文件对象；

	mode：指定文件的打开模式；

		文件存储的两种格式：文本和二进制；
		简单模式：
			r: 只读
				open('/var/log/message.log','r')
			r: 写入，从文件指针所在位置开始写入；
			a：附加，从文件尾部开始写入；
		在模式后使用"+"表示同时支持输入、输出操作；
			如：r+、w+和a+
		在模式后附加"b"表示以二进制方式打开；
			如：rb、wb+

	bufsize：定义输出缓存；
		0表示无输出缓存；
		1表示使用缓冲；
		负数表示使用系统默认设置；
		正数表示使用近似指定大小的缓冲；

```python 
var_name = open(filename[mode,[bufsize]])
	mode:
		r
		w
		a
		r+
		w+
		a+
	b表示以二进制模式打开文件：
		rb
		wb
		ab
		rb+
		wb+
		ab+
	缓冲：
		0：禁用；
		负数：使用系统默认缓冲；
		1：使用缓冲，只缓冲一行数据；
		2+： 指定缓冲空间大小；

f1 = open('passwd.txt','w+')
```

方法：
	f1.next()  # 迭代器的next()
	f1.close() # 关闭文件，有打开一定要有关闭；
	In [14]: f1.fileno()   # 文件描述符；
	Out[14]: 6			   # 0，1，2是标准输入、标准输出、标准错误输出
	f1.readline()   # 读取文件的一行；包括行结束符；移动文件指针；
	f1.readlines()  # 以列表形式返回文件的所有行；移动文件指针；
	f1.tell() 		# 打印当前指针在文件中的位置，显示字节数；
	# 以可写入的方式打开文件，并写入数据有风险；若文件指针不在文件尾部，写入数据时会覆盖原有内容；
	f1.seek(offset[,whence])  # 设定文件指针；
		whence:三个值；偏移量的起点；
			0：从文件头；
			1：从当前位置；
			2：从文件尾部；
		offset：偏移量；
		例如：f1.seek(0) # 将文件指针移动到文件首部；
	f1.read([size])   # 明确指定读取多少个字节；返回一个字串；
	f1.name    # 属性，调用当前文件的名称；
	f1.write()  # 写入
		f1.write('new line.\n')
	f1.flush()  # 刷写缓冲区，将缓冲区中的数据手动写入到磁盘上的文件中；

### 打开不存在的文件：
1、以读模式打开不存在的文件，会报IOError错误；
	r,r+,rb+
2、以w或a模式打开不存在文件，则会创建；

```python
In [8]: for line in ( i**2 for i in range(1,11)):
   ...:     f1.write(str(line) + '\n')
   ...:  
In [9]: f1.close()   
```

```bash
sslinux@sslinux-pygo:~$ cat /tmp/passwd 
new line.
1
4
9
16
25
36
49
64
81
100
```

```python
In [10]: f4 = open('/tmp/test2.txt','w+')

In [11]: l1 = [ i**2 for i in range(1,11) ]

In [12]: print l1
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

In [13]: f4.writelines(l1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-13-fe8341a43fb7> in <module>()
----> 1 f4.writelines(l1)

TypeError: writelines() argument must be a sequence of strings

In [14]: import os

In [15]: l2 = os.listdir('/etc')

In [16]: print l2
['X11', 'subuid', 'hostname', 'ucf.conf', 'rmt', 'pki', '.pwd.lock', 'pam.conf', 'ca-certificates.conf', 'gnome', 'fwupd.conf', 'acpi', 'rsyslog.conf', 'apparmor', 'network', 'sgml', 'ppp', 'localtime', 'bash.bashrc', 'resolv.conf', 'signond.conf', 'pnm2ppa.conf', 'fstab', 'rcS.d', 'update-notifier', 'group', 'os-release', 'shells', 'upstart-xsessions', 'gai.conf', 'locale.gen', 'aptdaemon', 'zsh_command_not_found', 'ufw', 'modules-load.d', 'libao.conf', 'init', 'protocols', 'init.d', 'hdparm.conf', 'gshadow', 'logcheck', 'cron.hourly', 'sudoers', 'apm', 'apt', 'kbd', 'libpaper.d', 'grub.d', 'cron.daily', 'subgid', 'xdg', 'udev', 'mailcap.order', 'ltrace.conf', 'polkit-1', 'securetty', 'rc0.d', 'doc-base', 'magic.mime', 'usb_modeswitch.conf', 'rc.local', 'libnl-3', 'thermald', 'rc5.d', 'magic', 'profile', 'lightdm', 'pulse', 'selinux', 'gss', 'adduser.conf', 'hosts.allow', 'mke2fs.conf', 'sensors.d', 'avahi', 'rpc', 'python2.7', 'python3.5', 'sensors3.conf', 'rc2.d', 'kernel-img.conf', 'papersize', 'rc1.d', 'inputrc', 'rc3.d', 'ld.so.conf', 'ghostscript', 'NetworkManager', 'shadow-', 'bluetooth', 'initramfs-tools', 'update-manager', 'speech-dispatcher', 'modprobe.d', 'hosts', 'groff', 'pcmcia', 'deluser.conf', 'ld.so.cache', 'gshadow-', 'pam.d', 'insserv.conf.d', 'apparmor.d', 'login.defs', 'manpath.config', 'machine-id', 'ssl', 'pm', 'timidity', 'binfmt.d', 'group-', 'cupshelpers', 'udisks2', 'ssh', 'issue', 'console-setup', 'kernel', 'bash_completion', 'resolvconf', 'usb_modeswitch.d', 'legal', 'wpa_supplicant', 'vdpau_wrapper.cfg', 'host.conf', 'passwd', 'openal', 'UPower', 'brltty.conf', 'tmpfiles.d', 'anacrontab', 'dconf', 'sysctl.d', 'insserv.conf', 'apport', 'appstream.conf', 'brlapi.key', 'fuse.conf', 'gdb', 'cron.monthly', 'calendar', 'sysctl.conf', 'gnome-app-install', 'kerneloops.conf', 'python', 'modules', 'gtk-3.0', 'hp', 'updatedb.conf', 'subuid-', 'depmod.d', 'alternatives', 'ld.so.conf.d', 'guest-session', 'profile.d', 'sane.d', 'mime.types', 'compizconfig', 'networks', 'ImageMagick-6', 'cups', 'mtab', 'rc6.d', 'newt', 'libaudit.conf', 'opt', 'at-spi2', 'shadow', 'rc4.d', 'dbus-1', 'terminfo', 'lvm', 'default', 'bash_completion.d', 'dpkg', 'subgid-', 'brltty', 'mtools.conf', 'rsyslog.d', 'lsb-release', 'crontab', 'skel', 'mailcap', 'python3', 'iproute2', 'cron.weekly', 'nanorc', 'locale.alias', 'debconf.conf', 'popularity-contest.conf', 'drirc', 'nsswitch.conf', 'passwd-', 'thunderbird', 'gtk-2.0', 'xml', 'dnsmasq.d', 'ldap', 'bindresvport.blacklist', 'chatscripts', 'wgetrc', 'timezone', 'issue.net', 'environment', 'cracklib', 'lintianrc', 'ifplugd', 'firefox', 'apg.conf', 'services', 'perl', 'systemd', 'dhcp', 'update-motd.d', 'ca-certificates', 'cron.d', 'logrotate.d', 'emacs', 'iftab', 'vim', 'vtrgb', 'signon-ui', 'libreoffice', 'insserv', 'hosts.deny', 'wildmidi', 'security', 'debian_version', 'gconf', 'dictionaries-common', 'fonts', 'logrotate.conf', 'sudoers.d']

In [18]: f4.writelines(l2)
In [19]: f4.flush()
```

```python
In [20]: l3 = [ i + '\n' for i in os.listdir('/etc') ]

In [21]: print l3
['X11\n', 'subuid\n', 'hostname\n', 'ucf.conf\n', 'rmt\n', 'pki\n', '.pwd.lock\n', 'pam.conf\n', 'ca-certificates.conf\n', 'gnome\n', 'fwupd.conf\n', 'acpi\n', 'rsyslog.conf\n', 'apparmor\n', 'network\n', 'sgml\n', 'ppp\n', 'localtime\n', 'bash.bashrc\n', 'resolv.conf\n', 'signond.conf\n', 'pnm2ppa.conf\n', 'fstab\n', 'rcS.d\n', 'update-notifier\n', 'group\n', 'os-release\n', 'shells\n', 'upstart-xsessions\n', 'gai.conf\n', 'locale.gen\n', 'aptdaemon\n', 'zsh_command_not_found\n', 'ufw\n', 'modules-load.d\n', 'libao.conf\n', 'init\n', 'protocols\n', 'init.d\n', 'hdparm.conf\n', 'gshadow\n', 'logcheck\n', 'cron.hourly\n', 'sudoers\n', 'apm\n', 'apt\n', 'kbd\n', 'libpaper.d\n', 'grub.d\n', 'cron.daily\n', 'subgid\n', 'xdg\n', 'udev\n', 'mailcap.order\n', 'ltrace.conf\n', 'polkit-1\n', 'securetty\n', 'rc0.d\n', 'doc-base\n', 'magic.mime\n', 'usb_modeswitch.conf\n', 'rc.local\n', 'libnl-3\n', 'thermald\n', 'rc5.d\n', 'magic\n', 'profile\n', 'lightdm\n', 'pulse\n', 'selinux\n', 'gss\n', 'adduser.conf\n', 'hosts.allow\n', 'mke2fs.conf\n', 'sensors.d\n', 'avahi\n', 'rpc\n', 'python2.7\n', 'python3.5\n', 'sensors3.conf\n', 'rc2.d\n', 'kernel-img.conf\n', 'papersize\n', 'rc1.d\n', 'inputrc\n', 'rc3.d\n', 'ld.so.conf\n', 'ghostscript\n', 'NetworkManager\n', 'shadow-\n', 'bluetooth\n', 'initramfs-tools\n', 'update-manager\n', 'speech-dispatcher\n', 'modprobe.d\n', 'hosts\n', 'groff\n', 'pcmcia\n', 'deluser.conf\n', 'ld.so.cache\n', 'gshadow-\n', 'pam.d\n', 'insserv.conf.d\n', 'apparmor.d\n', 'login.defs\n', 'manpath.config\n', 'machine-id\n', 'ssl\n', 'pm\n', 'timidity\n', 'binfmt.d\n', 'group-\n', 'cupshelpers\n', 'udisks2\n', 'ssh\n', 'issue\n', 'console-setup\n', 'kernel\n', 'bash_completion\n', 'resolvconf\n', 'usb_modeswitch.d\n', 'legal\n', 'wpa_supplicant\n', 'vdpau_wrapper.cfg\n', 'host.conf\n', 'passwd\n', 'openal\n', 'UPower\n', 'brltty.conf\n', 'tmpfiles.d\n', 'anacrontab\n', 'dconf\n', 'sysctl.d\n', 'insserv.conf\n', 'apport\n', 'appstream.conf\n', 'brlapi.key\n', 'fuse.conf\n', 'gdb\n', 'cron.monthly\n', 'calendar\n', 'sysctl.conf\n', 'gnome-app-install\n', 'kerneloops.conf\n', 'python\n', 'modules\n', 'gtk-3.0\n', 'hp\n', 'updatedb.conf\n', 'subuid-\n', 'depmod.d\n', 'alternatives\n', 'ld.so.conf.d\n', 'guest-session\n', 'profile.d\n', 'sane.d\n', 'mime.types\n', 'compizconfig\n', 'networks\n', 'ImageMagick-6\n', 'cups\n', 'mtab\n', 'rc6.d\n', 'newt\n', 'libaudit.conf\n', 'opt\n', 'at-spi2\n', 'shadow\n', 'rc4.d\n', 'dbus-1\n', 'terminfo\n', 'lvm\n', 'default\n', 'bash_completion.d\n', 'dpkg\n', 'subgid-\n', 'brltty\n', 'mtools.conf\n', 'rsyslog.d\n', 'lsb-release\n', 'crontab\n', 'skel\n', 'mailcap\n', 'python3\n', 'iproute2\n', 'cron.weekly\n', 'nanorc\n', 'locale.alias\n', 'debconf.conf\n', 'popularity-contest.conf\n', 'drirc\n', 'nsswitch.conf\n', 'passwd-\n', 'thunderbird\n', 'gtk-2.0\n', 'xml\n', 'dnsmasq.d\n', 'ldap\n', 'bindresvport.blacklist\n', 'chatscripts\n', 'wgetrc\n', 'timezone\n', 'issue.net\n', 'environment\n', 'cracklib\n', 'lintianrc\n', 'ifplugd\n', 'firefox\n', 'apg.conf\n', 'services\n', 'perl\n', 'systemd\n', 'dhcp\n', 'update-motd.d\n', 'ca-certificates\n', 'cron.d\n', 'logrotate.d\n', 'emacs\n', 'iftab\n', 'vim\n', 'vtrgb\n', 'signon-ui\n', 'libreoffice\n', 'insserv\n', 'hosts.deny\n', 'wildmidi\n', 'security\n', 'debian_version\n', 'gconf\n', 'dictionaries-common\n', 'fonts\n', 'logrotate.conf\n', 'sudoers.d\n']

In [22]: f4.seek(0)

In [23]: f4.writelines(l3)

In [24]: f4.flush()
```


In [26]: f4.isatty()		# 判断是不是一个终端文件；
Out[26]: False

```python
In [27]: f4.truncate(100)   # 截取文件内容，只保留100个字节；

In [28]: f4.flush()

In [29]: f4.seek(0)

In [30]: f4.readlines()
Out[30]: 
['X11\n',
 'subuid\n',
 'hostname\n',
 'ucf.conf\n',
 'rmt\n',
 'pki\n',
 '.pwd.lock\n',
 'pam.conf\n',
 'ca-certificates.conf\n',
 'gnome\n',
 'fwupd.conf\n',
 'acpi\n',
 'r']
```
```python
In [31]: f4.seek(0)

In [32]: f4.readline()
Out[32]: 'X11\n'

In [33]: f4.readline()
Out[33]: 'subuid\n'

In [34]: f4.truncate(f4.tell())   # 截取到当前指针；

In [35]: f4.seek(0)

In [36]: f4.readlines()
Out[36]: ['X11\n', 'subuid\n']
```

In [37]: f4.closed   # 属性，查看文件是否已经关闭；
Out[37]: False

In [38]: f4.encoding  # 属性，文件的编码；

In [39]: f4.mode    # 属性，获取该文件打开时使用的模式；
Out[39]: 'w+'

In [40]: f4.newlines  # 属性，返回换行符；

In [41]: f4.softspace   # 属性，写入行时是否使用软空格；
Out[41]: 0


### 文件系统功能：os模块；

```python
In [42]: import os

In [43]: os.abort 
        os.abort            os.EX_CANTCREAT     os.execv            os.getegid           
        os.access           os.EX_CONFIG        os.execve           os.getenv            
        os.altsep           os.EX_DATAERR       os.execvp           os.geteuid           
        os.chdir            os.EX_IOERR         os.execvpe          os.getgid            
        os.chmod            os.EX_NOHOST        os.extsep           os.getgroups         
        os.chown            os.EX_NOINPUT       os.F_OK             os.getloadavg        
        os.chroot           os.EX_NOPERM        os.fchdir           os.getlogin          
        os.close            os.EX_NOUSER        os.fchmod           os.getpgid           
        os.closerange       os.EX_OK            os.fchown           os.getpgrp           
        os.confstr          os.EX_OSERR         os.fdatasync        os.getpid            
        os.confstr_names    os.EX_OSFILE        os.fdopen           os.getppid          
        os.ctermid          os.EX_PROTOCOL      os.fork             os.getresgid         
        os.curdir           os.EX_SOFTWARE      os.forkpty          os.getresuid         
        os.defpath          os.EX_TEMPFAIL      os.fpathconf        os.getsid            
        os.devnull          os.EX_UNAVAILABLE   os.fstat            os.getuid            
        os.dup              os.EX_USAGE         os.fstatvfs         os.initgroups        
        os.dup2             os.execl            os.fsync            os.isatty            
        os.environ          os.execle           os.ftruncate        os.kill              
        os.errno            os.execlp           os.getcwd           os.killpg            
        os.error            os.execlpe          os.getcwdu          os.lchown   
```

os.mkdir('/tmp/testdir1')    # 创建目录；
os.getcwd()		# 获取当前工作目录；
os.chdir('/tmp')		# 切换工作目录；
os.stat('test2.txt')    # 查看当前目录test2.txt文件的元数据信息；

### 目录：
chdir() # 改变当前工作目录；
fchdir() # 通过文件描述符，改变工作目录；不常用；
chroot()  # 设定当前进程的根目录；
listdir() # 列出指定目录下的所有文件名，返回为一个列表；
mkdir()   # 创建指定目录，如果给定的路径不存在，可能会报错；
makedirs()  # 创建多级目录，若父目录不存在，则先创建父目录；类似于mkdir -pv
getcwd()    # 获取工作目录；
rmdir()     # 删除空目录；
removedirs() # 删除多级目录；

### 文件:
mkfifo()   # 创建先进先出管道；
mknode()   # 创建设备文件；
remove()   # 删除文件；
unlink()   # 删除链接文件；
rename()   # 重命名；
stat()     # 返回文件状态信息；
sylink()   # 创建一个符号链接；
utime()    # 更新文件的时间戳；
tmpfile()  # 创建并打开(w+b)一个新的临时文件
walk()     # 目录树生成器；
	g1 = os.walk('tmp')
	g1.next()

### 访问权限：
access()   # 检验权限模式；
	os.access('test2.txt',500)   # 数字是uid或gid
chmod()    # 修改权限；
	os.chmod(path,mode)
	os.chmod('test2.txt',0640)  
chown()    # 改变属主属组；
	os.chown(path,uid,gid)
umask()    # 设置默认权限遮罩码(模式)；

### 文件描述符：
open()     # 底层操作系统的open，for low level IO；不建议使用；
read()     
write()    

### 设备文件：
makedev()    # 创建设备；
major()		 # 获取主设备号
minor()      # 获取次设备号


### 子模块: os.path
import os.path    # 跟文件路径相关；

basename()    # 文件基名
dirname()     # 路径目录名；
join()   	  # 拼接路径名和文件名；
```python
In [44]: import os.path

In [45]: dir1 = os.path.dirname('/etc/sysconfig/network-scripts')

In [46]: file1 = os.path.basename('/etc/sysconfig/network-scripts')

In [47]: print dir1,file1
/etc/sysconfig network-scripts

In [48]: os.path.join(dir1,file1)
Out[48]: '/etc/sysconfig/network-scripts'
```

aplit()   # 返回dirname(),basename()结果的元组；
splitext()  # 返回(filename,extension)元组；

#### 信息：
getatime()    # 返回atime
getctime()
getmtime()
getsize()     # 返回文件大小；

#### 查询：
exists()      # 判断指定文件是否存在；
isabs() 	  # 判断指定的路径是否为绝对路径；
isdir()       # 判断指定路径是否为目录；
isfile()      # 判断是否存在且为文件；
islink()      # 是否为符号链接；
ismount()     # 是否为挂载点；
samefile()    # 两个路径是否指向了同一个文件；

练习：判断文件是否存在，存在则打开；
	让用户通过键盘反复输入多行数据；
	追加保存至此文件中；
```python
#!/usr/bin/python2.7
#

import os
import os.path

filename = raw_input("Which file you want to edit?")

if os.path.isfile(filename):
    f1 = open(filename,'a+')
else:
    print "File is not exists."
    exit

while True:
    line = raw_input('Enter something> ')
    if line == 'q' or line == 'quit':
        break

    f1.write(line+'\n')

f1.close()
```	


# 对象持久存储：
	存到文件中:
		pickle模块
		marshal模块
	DBM接口 ；
		第三方接口；
	shelve模块：

import pickle
pickle.dump()  # 将对象流式化存储到文件中；

```python
In [52]: d1 = {'Mon':1,'Tus':2,'Thu':3}

In [54]: f5 = open('/tmp/dfile.txt','a+')

In [55]: import pickle

In [57]: pickle.dump(d1,f5)

In [59]: f5.flush()
```

```bash
sslinux@sslinux-pygo:~$ cat /tmp/dfile.txt 
(dp0
S'Thu'
p1
I3
sS'Tus'
p2
I2
sS'Mon'
p3
I1
s.sslinux@sslinux-pygo:~$ 
```

pickle.load(FILE)   # 读取流式化存储的文件，还原为原本的数据对象；

```python
In [9]: f5.close()

In [10]: f6 = open('/tmp/dfile.txt','r+')

In [11]: d2 = pickle.load(f6)  # 将流式化存储的文件重新装载回来，依然是一个字典；

In [12]: print d2
{'Thu': 3, 'Tus': 2, 'Mon': 1}
```
