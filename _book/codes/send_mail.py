#!/usr/bin/env python3
#

import smtplib

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com,25')
smtp.login('xiongqikai@163.com','6525876As>?')
smtp.sendmail('xiongqikai@163.com','guiyin.xiong@symbio.com',msg.as_string())