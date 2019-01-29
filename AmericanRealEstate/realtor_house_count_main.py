# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: realtor_house_count_main.py
@time: 2019/1/28
"""
from scrapy.cmdline import execute

execute('scrapy crawl statistics_realtor_house_count'.split(' '))