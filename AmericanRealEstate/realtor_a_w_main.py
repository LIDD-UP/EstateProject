# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: realtor_a_w_main.py
@time: 2019/2/27
"""
import datetime
from scrapy.cmdline import execute
from multiprocessing import Pool


def execute_realtor_a():
    execute(['scrapy', 'crawl',
             'realtor_a',
             ])


def execute_realtor_w(user_agent_list,*args,**kwargs):
    execute(['scrapy', 'crawl',
             'realtor_w',
             "-a",
             "user_agent_list={}".format(user_agent_list),
             ])


def splite_user_agent(nums):
    from AmericanRealEstate.settings import realtor_user_agent_list
    # 爬虫进程数
    nums = nums
    each_spider_user_agent_number = int(len(realtor_user_agent_list) / nums)

    spider_user_agent_list = []

    for i in range(nums):

        # user_agent_list
        user_agent_str = '|'.join(
            realtor_user_agent_list[each_spider_user_agent_number * i:(i + 1) * each_spider_user_agent_number])

        if i == process_nums-1:
            user_agent_str = '|'.join(
                realtor_user_agent_list[each_spider_user_agent_number * i:])
        spider_user_agent_list.append(user_agent_str)
    print('finish user-agent splite')
    return spider_user_agent_list


if __name__ == '__main__':
    process_nums = 1
    spider_user_agent_list_out = splite_user_agent(process_nums)

    p = Pool(process_nums+1)
    for w_spider in range(process_nums):
        p.apply_async(execute_realtor_w, args=(spider_user_agent_list_out[w_spider],), )
    p.apply_async(execute_realtor_a)
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()








