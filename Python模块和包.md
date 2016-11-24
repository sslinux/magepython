# Python模块和包

[Python模块Blog](Python模块.md)


模块：

	顶层文件；
	模块文件；

## Python模块：

可以将代码量较大的程序分割成多个有组织的、彼此独立但又能互相交互的代码片段，这些自我包含的有组织的代码就是模块；

模块在物理形式上表现为以.py结尾的代码文件；

	一个文件被看作一个独立的模块，一个模块也可以被看作是一个文件；
	模块的文件名就是模块的名字加上扩展名.py
	每个模块都有自己的名称空间；

Python允许"导入"其他模块以实现代码重用，从而也实现了将独立的代码文件组织成更大的程序系统；

	python中，模块也是对象；
	在一个模块的顶层定义的所有变量都在被导入时成为了被导入模块的属性；

## Python程序架构：

一个Python程序通常包括一个顶层程序文件和其他的模块文件(0个、1个或多个)

	顶层文件：包含了程序的主要控制流程；
	模块文件：为顶层文件或其他模块提供各种功能性组件；

		模块首次导入(或重载)时，Python会立即执行模块文件的顶层程序代码
                (不在函数内的代码,函数声明语句也会执行并生成函数对象),
                而位于函数主体内的代码直到函数被调用后才会执行；

![python_strucure](/images/python_strucure.png)


## 模块的执行环境：

模块是被导入的，但模块也可以导入和使用其它模块，这些模块可以用Python或其他编程语言写成；

模块可内含变量、函数以及类来进行其工作，而函数和类可以包含变量和其它元素；

![python_module](/images/python_module.png)


### 导入模块：

在导入模块时只能使用模块名，而不能使用带.py后缀的模块文件名；

- import语句：

	导入指定的整个模块，包括生成一个以模块名命名的名称空间；

	import module[,module2[,... moduleN ]]

		建议一个import语句只导入一个模块；

	import modules as module_alias  # 使用了别名后仅能使用别名名称空间；

- from-import语句：

	常用于只**导入指定模块的部分属性**至**当前名称空间**；

	from module import name1[, name2[, ... nameN ]]

- import和from-import是赋值语句：

	import和from是可执行语句，类似于def，因此，他们可以嵌套在if测试中，出现于def中等等；

	python执行到这些语句时才会对其进行解析，这意味着，所有来自模块的属性仅在import语句执行后才能使用；

- import和from都是隐性赋值语句：

	import将整个模块对象赋值给一个变量名；

	from将一个或多个变量名赋值给导入此模块的模块中的同名对象；

- 模块就是名称空间：

	模块的名称空间可以通过属性__dict__或dir(M)获取

		模块属性可通过点号(.)运算符获取，格式为M.sttr

	模块是一个独立的作用域(本地变量就是全局变量)

---

### import的工作机制：

import语句导入指定的模块时会执行三个步骤：

- 找到模块文件：

	在指定的路径下搜索模块文件；

- 编译成字节码：

	文件导入时就会编译，因此，顶层文件的.pyc字节码文件在内部使用后会丢弃，只有被导入的文件才会留下.pyc文件；

- 执行模块的代码来创建其所定义的对象；

	模块文件中的所有语句会依次执行，从头至尾，而此步骤中任何对变量名赋值的运算，都会产生所得到的模块文件的属性；

**注意**：

    模块只在第一次导入时才会执行如上步骤；

    后续的导入操作只不过是提取内存中已加载的模块对象；

    reload()可用于重新加载模块；

### 模块搜索：

python解释器在import模块时必须先找到对应的模块文件：

- 程序的主目录；
- PYTHONPATH目录(如果设置了此目录)
- 标准链接库目录；
- 任何.pth文件的内容(如果存在.pth文件)

这四个组件组合起来即为sys.path所包含的路径，而Python会选择在搜索路径中的第一个符合导入文件名的文件；

```python
In [1]: import sys
In [1]: import sys

In [2]: sys.path
Out[2]: 
['',
 '/usr/local/bin',
 '/usr/lib/python35.zip',
 '/usr/lib/python3.5',
 '/usr/lib/python3.5/plat-x86_64-linux-gnu',
 '/usr/lib/python3.5/lib-dynload',
 '/usr/local/lib/python3.5/dist-packages',
 '/usr/lib/python3/dist-packages',
 '/usr/local/lib/python3.5/dist-packages/IPython/extensions',
 '/home/sslinux/.ipython']
```

```python 
import sys
sys.path.appen('/path/to/module')
```

```python
#!/usr/bin/env python3

x = 30
def printInfo():
    print(x + 30)

class MyClass():
    data = "hello myclass"
    def __init__(self,who):
        self.name = who
    def printName(self):
        print(self.data,self.name)

if __name__ == '__main__':
    printInfo()
    ins1 = MyClass('jerry')
    print(ins1.data)
    print(ins1.name)
```

### Python包：

包用于将一组模块归并到一个目录中，此目录即为包，目录名即为报名；

	包是一个有层次的文件目录结构，它定义类一个由模块和子包组成的python应用程序执行环境。

	基于包，Python在执行模块导入时可以指定模块的导入路径；
		import dir1.dir2.mod1

要使用如图所示的package1,则py_pkg_mod容器必须要在模块搜索路径中；

	import package1.mod1

包导入语句的路径内的每个目录都必须有\_\_init\_\_.py文件：

	__init__.py可包含python代码，但通常为空，仅用于扮演包初始化的挂钩、替目录产生模块命名空间以及使
        用目录导入时实现from * 行为的角色；

![Python_Package](/images/python_package.png)

```python
mkdir pkg1   # 在sys.path的搜索路径的目录下；
cd pkg1
vim __init__.py
	:wq
cp mymod.py pkg1/

import pkg1.mymod   # 在程序文件中；
```

### 模块的顶层执行及被导入：

一个模块文件可以同时支持顶层执行(作为顶层文件)或被导入(作为模块文件)

	每个模块都有个名为__name__的内置属性，Python会自动设置该属性；
		如果文件是以顶层程序文件执行，在启动时，__name__的值为"__main__"
		如果是被导入，则__name__的值为模块名；

可以在模块文件中检测自己的__name__属性，以之实现在执行时运行指定的代码；

常用于模块的自我测试：

```python
#!/usr/bin/env python3
#
# 利用__name__属性的值判断该模块是主动执行，还是被调用执行；

def testFunc():
    print("Hello,there...")

if __name__ == "__main__":
    testFunc()
```

### 发布Python模块或程序：
Python模块、扩展和应用程序可以按以下几种形式进行打包和发布：
- 压缩文件(使用distutils模块)
	Windows的zip文件和类Unix平台的.tar.gz文件；
- 自动解包或自动安装可执行文件；
	Windows中的exe文件；
- 自包含的，不要求安装的预备运行可执行程序；
	Windows的.exe文件、Unix上带有一个小的脚本前缀的ZIP压缩文件、Mac上的.app文件等；
- 平台相关的安装程序：
	Windows上的.msi文件、Linux上常见的.rpm、src.rpm和.deb文件等；
- python eggs：(蟒蛇蛋)
	较流行的第三方扩展；

#### 使用disutils发布模块：
distutils模块能够帮助完成模块或程序发布：

	"发布"是指一个文件集合，这些文件联合在一起可使用distutils构建、打包和发布模块；

	创建好的发布可以用于安装，也可上传到PyPI与他人分享；

创建发布：

	将各代码文件组织到模块容器中；
	准备一个README或README.txt文件；
	而后在容器中创建setup.py文件：

```python
from distutils.core import setup

setup(
	name = 'testmod',
	version = '0.0.1',
	author = 'SSLinux',
	author_email = 'guiyin.xiong@gmail.com',
	py_modules = ['testmod'],
	url = 'http://www.sslinux.com',
	description = 'A simple module',
	)

```

#### setup.py的常用参数：

将各代码文件组织到模块容器中，而后在容器中创建setup.py文件；

![package_setup](/images/package_setup.png)

参数还有:

```python
py_modules = ['testmod',]   # 各模块名称组成的列表，此些模块可能位于包的根目录下(modename)，也可能位于某子包目录中(subpkg1.modename)；
platforms: 平台列表；
license：许可证；
packages: 各子包名称的列表；

大体分为两类：
	元数据信息
	包中的内容列表；

#### 完成打包：
在要发布的容器目录中执行"python setup.py sdist"命令；

#### 可以为sdist指定格式： --formats=
zip: zip file
gztar: tar.gz file
b1tar: tar.bz2 file
ztar: tar.Z file
tar: tar file


python setup.py bdist  # 二进制发行版；
可以为bdist指定的格式；--formats=
	gztar: tar.gz file
	ztar: tar.Z file
	tar: tar file
	zip: zip file
	rpm: RPM Package
	pkgtool: Solaris pkgtool
	wininst: Windows上能自解压的zip格式的包；
	msi: Microsot Installer

也可以使用以下命令：
	bdist_dump: 
	bdist_rpm:
	bdist_wininst
	bdist_msi



touch README
vim setup.py
```python
#!/usr/bin/env python3
#
from distutils.core import setup

setup(
	name = 'pkg1'
	version = '0.0.1'
	author = 'SSLinux'
	author = 'guiyin.xiong@gmail.com'
	py_modules = ['yanmod',],
	url = 'http://www.sslinux.com',
	download_url = 'http://www.sslinux.com/pymodules/download/',
	description = 'test module'
	)
```

```bash
python3 setup.py sdist
ls dist

python3 setup.py bdist
python3 setup.py bdist --formats=gztar
python3 setup.py bdist --formats=rpm
python3 setup.py bdist --formats=msi

python3 setup.py sdist
python3 setup.py sdist --formats=gztar
python3 setup.py sdist --formats=rpm
python3 setup.py sdist --formats=msi   # 只能在windows平台下能执行成功；
```

获取帮助的方式：
```bash
	python setup.py --help
	python setup.py --help-commands: #所有可以使用的命令，如build，install；
	python setup.py COMMAND --help ：#获取特定命令的帮助；
	python setup.py COMMAND --help-formats: #获取特定命令支持使用的格式；
```

上传到PyPI后就可以使用pip和easy_install方式来安装了；


安装包：

	python setup.py build   # 默认被install包含；
	python setup.py install

	python setup.py build:
		--build-base=/path/to/build_dir   # build目录放到其他目录；
			lib,   # 保存python库文件；
			lib.platform  # 保存其他语言编写的跟平台密切相关的文件；

	第三方模块的默认安装路径通常为：site-packages目录下；
		'/usr/lib/python3/dist-packages'

	自定义安装路径：
		--user=    # 安装到用户的家目录下；
		--prefix=  # 安装到其他指定目录；
		--exec-prefix= # 指定跟python无关，由其他语言编写的与平台相关的文件的路径；

	深度定制：
		--install-purelib=/path/to/python-lib   # 纯python库文件；
		--install-platlib=/path/to/plat_lit  # 其他语言的平台相关的库；
		--install-lib=/path/to/lib   # 不区分上述两者；

		--install-scripts=/path/to/bin  # 可执行文件的安装路径；

		--install-data=    # 数据文件的安装位置；
		--install-headers= # C的头文件安装路径；

		还可以编辑distutils文件的install段；































