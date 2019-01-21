# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: use_selenium.py
@time: 2019/1/21
"""
from selenium import webdriver
from scrapy.http import HtmlResponse
class JSPageMiddleware(object):

    #通过chrome请求动态网页
    def process_request(self, request, spider):
        if spider.name == "jobbole":
            browser = webdriver.Chrome(executable_path="C:/chromedriver.exe")
            spider.browser.get(request.url)
            import time
            time.sleep(3)
            print ("访问:{0}".format(request.url))


