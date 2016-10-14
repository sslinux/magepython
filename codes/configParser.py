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


