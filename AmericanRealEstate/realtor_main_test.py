# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: realtor_main_test.py
@time: 2019/2/11
"""
from AmericanRealEstate.settings import realtor_search_criteria, realtor_user_agent_list

# 爬虫进程数
process_nums = 1
# 生成起始url字符串

# 将start_url 分成进程数
each_spider_criteria_number = int(len(realtor_search_criteria) / process_nums)
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

    if i == process_nums - 1:
        # # start_request_list
        # start_url_str = ','.join(
        #     realtor_search_criteria[each_spider_criteria_number * i:])
        # user_agent_list
        user_agent_str = '|'.join(
            realtor_user_agent_list[each_spider_user_agent_number * i:])

    # print(start_url_str)
    # spider_start_urls_list.append(start_url_str)

    spider_user_agent_list.append(user_agent_str)
    for i in spider_user_agent_list:
        # print('split',i.split('-'))
        for j in i.split('|'):
            print(j)

# print(spider_start_urls_list)
# print(spider_user_agent_list)

# print(len(realtor_user_agent_list))
# print(len(set(realtor_user_agent_list)))