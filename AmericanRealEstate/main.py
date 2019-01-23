# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: main.py
@time: 2019/1/9
"""
import os
import sys
sys.path.append(os.path.abspath(__file__))

import redis
import pandas as pd
from scrapy.cmdline import execute





# 将url先插入到redis队列里面
# pool = redis.ConnectionPool(host='192.144.149.43',password='123456')   #实现一个连接池
#
# r = redis.Redis(connection_pool=pool)
# data = pd.read_csv('./crawl_tools/realtor_search_criteria.csv')
# city_list = list(data['countyStateJoin'])
# for city in city_list:
#     r.lpush('realtor:start_urls',city)
# print(r.get('foo').decode('utf8'))


execute('scrapy crawl trulia_state_county_zip -s JOBDIR=crawls/trulia_state_county_zip-1'.split(' '))
# execute('scrapy crawl trulia_state_county_zip'.split(' '))

# execute('scrapy crawl realtor -s JOBDIR=crawls/trulia_state_county_zip-1'.split(' '))
# execute('scrapy crawl realtor'.split(' '))

# execute('scrapy crawl trulia'.split(' '))


