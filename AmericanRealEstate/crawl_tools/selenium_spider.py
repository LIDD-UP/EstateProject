# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: selenium_spider.py
@time: 2019/1/22
"""
from selenium import webdriver


# browser = webdriver.Chrome(executable_path=r'F:\PycharmProject\EstateProject\AmericanRealEstate\crawl_tools\chromedriver.exe')
# browser.get('https://www.trulia.com/NY/New_York/')
# # print(browser.page_source)
# print(browser.get_cookies())



# selenium
# xml
# lxml c语言写的库，速度快

# chromdirver 不加载图片

# 设置chromedriver不加载图片
# chrome_opt = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":2}
# chrome_opt.add_experimental_option("prefs",prefs)
# browser = webdriver.Chrome(executable_path=r'F:\PycharmProject\EstateProject\AmericanRealEstate\crawl_tools\chromedriver.exe',chrome_options=chrome_opt)
# browser.get('https://www.trulia.com/NY/New_York/')
# print(browser.get_cookies())
# 虽然说selenium+chrome是一个不错的选择，但是每次要打开浏览器，所以不是最优的选择；

# phtomjs 多进程的情况下性能下降

# 剩下最后的选择就是selenium + chromeheadless
# from selenium import  webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.binary_location = '/usr/bin/google-chrome-stable'
# capabilities = {}
# capabilities['platform'] = 'Linum'
# capabilities['version'] = '16.04'

from selenium import webdriver
from scrapy.http import HtmlResponse # 当scrapy 遇到htmlresponse的时候scrapy就不会将这个url交到下载器里里面进行下载
from selenium.webdriver.chrome.options import Options


# class SeleniumMiddleware(object):
# 需要再这里加上一个init方法然后继承之后实现初始化，不用每次都需要启动了
# from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals




# 使用selenium

# def __init__(self):
#     self.browser = webdriver.Chrome(executable_path="D:/Temp/chromedriver.exe")
#     super(JobboleSpider, self).__init__()
#     dispatcher.connect(self.spider_closed, signals.spider_closed)
#
#
# def spider_closed(self, spider):
#     # 当爬虫退出的时候关闭chrome
#     print("spider closed")
#     self.browser.quit()
#   def process_request(self,request,spider):
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--disable-gpu')
#     options.binary_locaion = '/usr/bin/google-chrome-stable'
#     capabilities = {}
#     capabilities['platform'] = 'Linux'
#     capabilities['version'] = '16.04'
#     if spider.name == "music163": # 这里需要注意
#       print 'start parse {0}'.format(request.url)
#       #driver = webdriver.PhantomJS()
#       driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver',chrome_options=options,desired_capabilities=capabilities)
#       try:
#         driver.get(request.url)
#         driver.switch_to.frame('g_iframe')
#         body = driver.page_source
#         print 'finished parse {0}'.format(request.url)
#         return HtmlResponse(driver.current_url,body=body,encoding='utf-8',request=request)
            # 注意这里的参数要够
#       except:
#         driver.quit()



# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.binary_locaion = '/usr/bin/google-chrome-stable'

# capabilities = {}
# capabilities['platform'] = 'Linux'
# capabilities['version'] = '16.04'

# print 'start parse {0}'.format(request.url)
#driver = webdriver.PhantomJS()
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r'F:\PycharmProject\EstateProject\AmericanRealEstate\crawl_tools\chromedriver.exe',chrome_options=options)

driver.get('https://www.trulia.com/NY/New_York/')
print(driver.get_cookies())
cookie_list = driver.get_cookies()

for item in cookie_list: driver.add_cookie({
    'domain': '.trulia.com',
    'name': item['name'],
    'value': item['value'],
    'path': '/',
    'expires': None
})
# cookie_list = driver.get_cookies()

cookies = ";".join([item["name"] + "=" + item["value"] + "" for item in cookie_list])
print(cookies)



import requests
import json


trulia_headers ={
'authority': 'www.trulia.com',
# 'method': 'GET',
# 'path':'/sitemap/Alabama-real-estate/',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
'cache-control': 'max-age=0',
# 'cookie':'s_fid=433AA466E2E74246-15C3C4922E6D4B9F; tlftmusr=190111pl5oxe6dz6h9ql8f26dy4gw379; fvstts=20190110; _ga=GA1.2.1370343627.1547191941; s_vi=[CS]v1|2E1C236905033FEB-40001188A0008984[CE]; _pxvid=3becfc80-1573-11e9-8c5b-a9eccfd531c4; SERVERID=webfe335|XEV18',
'cookie':cookies,
# 'cookie': '98504c2c72c25c2260c0d4d58f76999e36e9c1bddd6727180fa4d88c82e9368f:NDveLiFoDkPA+jfpBD6OkzYW825UMvd4dAtPYqwDGdAJPYXJAvddOTiayRTaxzXF+54MMI1e5fA5iBJtNw6nYw==:1000:RDPcIWDvxN2d8xrXVdr2hhqw+vF+zC01l0tgGqwihxESM8qIPgFV1KzgCjh56tCfPfyAGOpU/Y0b5uij7iMOF8FuOi91jR1yoJMOppSJPoXFkhoEjVXwOF3MYcpFndXiCRQnJ+n7zMIRIBC+4vUirsmhaoSfv4JIdAzNRL273gc=',
'referer': 'https://www.trulia.com',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',

}
session =requests.session()

state = session.get(url='https://www.trulia.com/County/AL/Autauga_Real_Estate/',headers=trulia_headers)
# print(type(state.cookies))
print(state.text)
#
#
# with open('./test_html.html','w') as f:
#     f.write(state.text)

