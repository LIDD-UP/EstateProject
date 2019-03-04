# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: main.py
@time: 2019/1/9
"""
import os
import sys
sys.path.append(os.path.abspath(__file__))

import time

import redis
import pandas as pd
from scrapy.cmdline import execute
from multiprocessing import Pool
import os, time, random, datetime





# 将url先插入到redis队列里面
# pool = redis.ConnectionPool(host='192.144.149.43',password='123456')   #实现一个连接池
#
# r = redis.Redis(connection_pool=pool)
# data = pd.read_csv('./crawl_tools/realtor_search_criteria.csv')
# city_list = list(data['countyStateJoin'])
# for city in city_list:
#     r.lpush('realtor:start_urls',city)
# print(r.get('foo').decode('utf8'))











def execute_spider(num,
                   # start_urls,
                   user_agent_list,scrapy_start_time,*args,**kwargs):
    # print('开启了第{}爬虫进程'.format(num))
    # print('realtor{}'.format(num))
    execute(['scrapy', 'crawl',
             'realtor_w',
             # "-a",
             # "start_urls={}".format(start_urls),
             "-a",
             "user_agent_list={}".format(user_agent_list),
             "-s",
             "scrapy_start_time={}".format(scrapy_start_time)
             ])

if __name__=='__main__':
    # from AmericanRealEstate.settings import realtor_search_criteria
    from AmericanRealEstate.settings import realtor_user_agent_list

    #爬虫进程数
    process_nums = 1
    # 生成起始url字符串

    # 将start_url 分成进程数
    # each_spider_criteria_number = int(len(realtor_search_criteria) / process_nums)
    # 将user_agent_list 分成进程数
    each_spider_user_agent_number = int(len(realtor_user_agent_list) / process_nums)

    # spider_start_urls_list = []
    spider_user_agent_list = []


    for i in range(process_nums):
        # start_request_list
        # start_url_str = ','.join(
        #     realtor_search_criteria[each_spider_criteria_number * i:(i + 1) * each_spider_criteria_number])

        # user_agent_list
        user_agent_str = '|'.join(
            realtor_user_agent_list[each_spider_user_agent_number * i:(i + 1) * each_spider_user_agent_number])

        if i == process_nums-1:
            # start_request_list
            # start_url_str = ','.join(
            #     realtor_search_criteria[each_spider_criteria_number * i:])
            # user_agent_list
            user_agent_str = '|'.join(
                realtor_user_agent_list[each_spider_user_agent_number * i:])

        # print(start_url_str)
        # spider_start_urls_list.append(start_url_str)

        spider_user_agent_list.append(user_agent_str)

    # print('一共几批start_url',len(spider_start_urls_list))
    print('Parent process %s.' % os.getpid())
    p = Pool(process_nums)
    for i in range(process_nums):
        # 首次执行
        p.apply_async(execute_spider, args=(i+1,
                                            # spider_start_urls_list[i],
                                            spider_user_agent_list[i], i),)

    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')



