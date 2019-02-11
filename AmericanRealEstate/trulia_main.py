# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: trulia_main.py
@time: 2019/2/11
"""
from scrapy import cmdline


cmdline.execute('scrapy crawl trulia'.split(' '))
