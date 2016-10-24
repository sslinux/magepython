# paramiko模块

github添加密钥后，配置如下：
```python
sslinux@sslinux-py2go:/media/sslinux/Disk-Study/magePython/PPT/MagePython$ cat .git/config 
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = git@github.com:sslinux/MagePython.git   #主要是这里；
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
```

即可不必输入用户名和密码进行push了；