#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import datetime
import traceback
import logging
import os

# 测试用例执行函数：
def work(browser):
    url = "http://10.60.4.210:3000/login/"
    browser.get(url)
    try:
        browser.find_element_by_name("username").clear()
        browser.find_element_by_name("username").send_keys("admin")
        browser.find_element_by_id("inputPassword").clear()
        browser.find_element_by_id("inputPassword").send_keys("admin")
        browser.find_element_by_xpath("//button[@type='submit']").click()
        browser.find_element_by_css_selector("span.dashlist-title").click()

        # 验证登陆成功的url
        currUrl = browser.current_url
        if currUrl == 'http://10.60.4.210:3000/':
            # browser.find_element_by_css_selector("span.navbar-brand-btn-background").click()
            # browser.find_element_by_link_text("Home").click()
            # browser.find_element_by_css_selector("span.dashlist-title").click()

            print(u"success")

        else:
            print(u"failure")
            writeLog()
    except:
        print(u"failure")
        writeLog()

# 写错误日志并截图
def writeLog():
    # 组合日志文件名(当前文件名+当前时间). 比如： case_login_success_20150817192533
    basename = os.path.splitext(os.path.basename(__file__))[0]
    logFile = basename+"-"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+".log"
    logging.basicConfig(filename=logFile)
    s = traceback.format_exc()
    logging.error(s)
    browser.get_screenshot_as_file("./"+logFile+"-screenshot_error.png")

if __name__ == "__main__":
    browser = webdriver.Firefox()
    work(browser)
    browser.quit()





