# Centos 7 打造 Python开发环境

安装Centos 7，配置网络，配置yum，安装desktop；

关闭firewalld和selinux；

## 1、安装IDEA

下载地址：[https://download.jetbrains.8686c.com/idea/ideaIU-2016-2.4.tar.gz](https://download.jetbrains.8686c.com/idea/ideaIU-2016-2.4.tar.gz)
```bash
tar xf ideaIU-2016.2.4.tar.gz 
 
ln -sv idea-IU-162.2032.8 idea

cd idea

./bin/idea.sh     
# 因为我下的版本是包含了JDK的，所以不需要单独安装JDK，否则需要安装并配置JDK；

ln -sv ./bin/idea.sh /usr/bin/idea   # 为了方便，创建一个软链接；
```
上述命令启动了安装界面，顺着界面就可以完成安装了，可以为所有用户创建一个快捷图标；

然后在初始界面点击configure --&gt; 并安装plugins --&gt; python  --&gt; Install

安装完成后就可以创建python项目了

## 2、安装git：

```bash
[sslinux@localhost ~]$ sudo yum -y install git
```

**安装pyenv**:

为了安装pyenv方便，作者开发了另一个项目：pyenv-installer来帮助广大劳苦大众安装pyenv；

pyenv：[https://github.com/yyuu/pyenv/](https://github.com/yyuu/pyenv/)

pyenv-installer：[https://github.com/yyuu/pyenv-installer](https://github.com/yyuu/pyenv-installer)

使用pyenv-installer安装pyenv：

```bash
$ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash  
```

修改环境变量：

```bash
[sslinux@localhost ~]$ vim ~/.bash_profile   # 仅对当前用户有效；
export PATH="/home/sslinux/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

所有用户有效：

```bash
[sslinux@localhost ~]$ cat /etc/profile.d/pyenv.sh
export PATH="/home/sslinux/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

更新pyenv：

```bash
pyenv update
```

**卸载pyenv**
pyenv 默认安装在环境变量$PYENV\_ROOT所指定的目录下\(默认为:~\/.pyenv\)

```bash
$ rm -rf ~/.pyenv
# 将配置文件中的相关配置删除掉；
export PATH="/home/sslinux/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

### 通过PyPi的方式安装pyenv：

```bash
$ pip install --egg pyenv
```

## 3、安装Python：

**安装编译工具:**

```bash
[sslinux@localhost ~]$ sudo yum -y install gcc make patch
```

**安装依赖包：**

```bash
[sslinux@localhost ~]$ sudo yum -y install gdbm-devel openssl-devel \
sqlite-devel readline-devel zlib-devel bzip2-devel
```

**安装python 3.5.2**

```bash
[sslinux@localhost ~]$ pyenv install 3.5.2
```

### 使用pyenv：

```bash
[sslinux@localhost .pyenv]$ pyenv
pyenv 1.0.2
Usage: pyenv <command> [<args>]

Some useful pyenv commands are:
   commands    List all available pyenv commands  # 列出所有可用的子命令，包括virtualenv
   local       Set or show the local application-specific Python version
   global      Set or show the global Python version
   shell       Set or show the shell-specific Python version
   install     Install a Python version using python-build
   uninstall   Uninstall a specific Python version
   rehash      Rehash pyenv shims (run this after installing executables)
   version     Show the current Python version and its origin
   versions    List all Python versions available to pyenv
   which       Display the full path to an executable
   whence      List all Python versions that contain the given executable

See `pyenv help <command>' for information on a specific command.
For full documentation, see: https://github.com/yyuu/pyenv#readme
```

**local命令:**  

local命令切换当前目录及子目录的Python版本，可以通过删除'.python-version'恢复默认Python版本；

**global命令:**

global切换全局默认Python版本，不建议这么使用；

#### virtualenv命令：

创建虚拟环境：

```bash
pyenv virtualenv $python_version $name
```

```bash
[sslinux@localhost .pyenv]$ pyenv help virtualenv
Usage: pyenv virtualenv [-f|--force] [VIRTUALENV_OPTIONS] [version] <virtualenv-name>
       pyenv virtualenv --version
       pyenv virtualenv --help

  -f/--force       Install even if the version appears to be installed already
```

**install命令:**

安装指定版本，后面直接跟版本号即可；

**Uninstall命令:**

卸载某个版本，包括虚拟环境；

**环境配置原理：**

    python的环境是基于site的，即整个机器的python环境是一样的；

    java是基于project的，每个项目可以使用不同的java环境；

### pyenv virtualenv 命令：

```bash
[sslinux@localhost ~]$ pyenv virtualenv 3.5.2 py2go    # 创建一个虚拟环境，名叫py2go
Ignoring indexes: https://pypi.python.org/simple
Requirement already satisfied (use --upgrade to upgrade): setuptools in /home/sslinux/.pyenv/versions/3.5.2/envs/py2go/lib/python3.5/site-packages
Requirement already satisfied (use --upgrade to upgrade): pip in /home/sslinux/.pyenv/versions/3.5.2/envs/py2go/lib/python3.5/site-packages
[sslinux@localhost ~]$ pyenv versions
* system (set by /home/sslinux/.pyenv/version)
  3.5.2
  3.5.2/envs/py2go
  3.5.2/envs/symbio
  py2go
  symbio
```

切换到虚拟环境：

```bash
[sslinux@localhost ~]$ pyenv local py2go  # 切换本地python环境为指定虚拟环境
(py2go) [sslinux@localhost ~]$ python -V
Python 3.5.2
(py2go) [sslinux@localhost ~]$ pyenv version
py2go (set by /home/sslinux/.python-version)
```

所有使用pyenv创建的python版本，都在~\/.pyenv\/versions\/目录下；

### python IDE
- Pycharm
- IDEA
- Atom
- vscode

## pip命令

```
[sslinux@localhost ~]$  pyenv versions
* system (set by /home/sslinux/.python-version)
  3.5.2
  3.5.2/envs/py2go
  py2go
[sslinux@localhost ~]$ pyenv local py2go
(py2go) [sslinux@localhost ~]$ mkdir ~/.pip
(py2go) [sslinux@localhost ~]$ vim ~/.pip/pip.conf
(py2go) [sslinux@localhost ~]$ cat ~/.pip/pip.conf   # 为提高下载速度设置；
```

```ini
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
trusted-host = mirrors.aliyun.com
```

在虚拟环境中，使用pip安装ipython，安装其他模块和包也是一样的；

```bash
(py2go) [sslinux@localhost ~]$ pip install ipython
```

**pip 安装jupyter:**

安装文档：[http:\/\/jupyter.org\/install.html](http://jupyter.org/install.html)

```bash
pip3 install --upgrade pip
pip3 install jupyter
```

```bash
(py2go) [sslinux@localhost ~]$ jupyter -h
usage: jupyter [-h] [--version] [--config-dir] [--data-dir] [--runtime-dir]
               [--paths] [--json]
               [subcommand]

Jupyter: Interactive Computing

positional arguments:
  subcommand     the subcommand to launch

optional arguments:
  -h, --help     show this help message and exit
  --version      show the jupyter command's version and exit
  --config-dir   show Jupyter config dir
  --data-dir     show Jupyter data dir
  --runtime-dir  show Jupyter runtime dir
  --paths        show all Jupyter paths. Add --json for machine-readable
                 format.
  --json         output paths as machine-readable json

Available subcommands: console kernelspec migrate nbconvert nbextension
notebook qtconsole serverextension troubleshoot trust
```

**启动jupyter：**

```bash
(py2go) [sslinux@localhost ~]$ jupyter notebook --no-browser --ip=0.0.0.0
```

此时便可以在本地的浏览器中使用ip加端口进行访问了；

