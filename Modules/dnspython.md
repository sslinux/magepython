### DNS处理模块dnspython；

#### 安装：
[dnspython](http://www.dnspython.org)是python实现的一个DNS工具包，它支持几乎所有的记录类型，可以用于查询、传输并动态更新ZONE信息，同时支持TSIG(事务签名)验证消息和EDNS0(扩展DNS).

利用dnspython的查询功能来实现DNS服务监控以及解析结果的校验，可以替代nslookup及dig等工具。

```bash
wget http://www.dnspython.org/kits/1.15.0/dnspython-1.15.0.tar.gz
tar -zxvf dnspython-1.15.0.tar.gz 
cd dnspython-1.15.0/
sudo python3 setup.py install
```
```python 
In [1]: import dns.resolver    # 导入无报错，说明安装成功；
```

#### 模块域名解析方法详解：
dnspython模块提供了大量的DNS处理方法，最常用的方法是域名查询。

dnspython提供了一个DNS解析器类——resolver，使用它的query方法来实现域名的查询功能。query方法的定义如下：

```python
query(self,qname,rdtype=1,rdclass=1,tcp=False,source=None,raise_on_no_answer=True,source_port=0)
```
其中，qname参数为查询的域名。rdtype参数用来指定RR资源的类型，常用的有以下几种：
- A记录，将主机名转换成IP地址；
- MX记录，邮件交换记录，定义邮件服务器的域名；
- CNAME记录，指别名记录，实现域名间的映射；
- NS记录，标记区域的域名服务器及授权子域；
- PTR记录，反向解析，与A记录相反，将IP转换成主机名；
- SOA记录，SOA标记，一个起始授权区的定义。

rdclass参数用于指定网络类型，可选的值有IN、CH与HS，其中IN为默认，使用最广泛。tcp参数用于指定查询是否启用TCP协议，默认为False(不启用)。

source与source_port参数作为指定查询源地址与端口，默认值为查询设备IP地址和0.

raise_on_no_answer参数用于指定当查询无应答时是否触发异常，默认为True。

(1) A记录：
```python
#!/usr/bin/env python3 
import dns.resolver

domain = input("Please input an domain: ")   # 输入域名地址；

A = dns.resolver.query(domain,'A')    # 指定查询类型为A记录；
for i in A.response.answer:           # 通过response.answer方法获取查询回应信息；
    for j in i.items:        # 遍历回应信息；
        print(j.address)
```

(2) MX记录：
```python
import dns.resolver

domain = input("Please input an domain:")
MX = dns.resolver.query(domain,'MX')      # 指定查询类型为MX记录；
for i in MX:                # 遍历回应结果，输出MX记录的preference及exchanger信息
    print('MX preference = ',i.preference,'mail exchanger = ',i.exchange)
```
输出：
```python
Please input an domain:163.com
MX preference =  10 mail exchanger =  163mx03.mxmail.netease.com.
MX preference =  50 mail exchanger =  163mx00.mxmail.netease.com.
MX preference =  10 mail exchanger =  163mx01.mxmail.netease.com.
MX preference =  10 mail exchanger =  163mx02.mxmail.netease.com.
```

(3)NS记录：
```python
import dns.resolver

domain = input('Please input an domain: ')

ns = dns.resolver.query(domain,'NS')     # 指定查询类型为NS记录；
for i in ns.response.answer:
    for j in i.items:
        print(j.to_text())
```
只限输入一级域名，如baidu.com。如果输入二级或多级域名，如www.baidu.com,则是错误的；
输出：
```python
Please input an domain: baidu.com
ns2.baidu.com.
ns3.baidu.com.
ns4.baidu.com.
ns7.baidu.com.
dns.baidu.com.
```

(4) CNAME记录：
```python
import dns.resolver

domain = input("Please input an domain: ")
cname = dns.resolver.query(domain,'CNAME')     # 指定查询类型为CNAME记录；
for i in cname.response.answer:                # 结果将回应cname后的目标域名；
    for j in i.items:
        print(j.to_text())
```
输出：
```python
Please input an domain: www.baidu.com
www.a.shifen.com.
```
结果将返回cname后的目标域名；

#### 实践：DNS域名轮循业务监控：

DNS轮循可以做到一个域名对应多个IP，从而实现简单且高效的负载均衡，不过此方案最大的弊端是目标主机不可用时无法被自动剔除，因此做好业务主机的服务可用监控至关重要；

