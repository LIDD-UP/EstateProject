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


# execute('scrapy crawl trulia_state_county_zip -s JOBDIR=crawls/trulia_state_county_zip-1'.split(' '))
# execute('scrapy crawl trulia_state_county_zip'.split(' '))

# execute('scrapy crawl realtor -s JOBDIR=crawls/trulia_state_county_zip-1'.split(' '))
# execute('scrapy crawl realtor'.split(' '))

# execute(['scrapy', 'crawl', 'realtor',"-a","start_urls='https://www.realtor.com/realestateandhomes-search/New-York-County_NY'"])
# execute("scrapy crawl realtor -a start_urls=['https://www.realtor.com/realestateandhomes-search/New-York-County_NY']".split(' '))

# execute('scrapy crawl trulia'.split(' '))




#
# print(each_spider_criteria_number)
#
# for process_num in range(process_nums):
#     pass


from multiprocessing import Pool
import os, time, random
import ast




custom_settings_str = '{"ITEM_PIPELINES": {"AmericanRealEstate.pipelines.RealtorHouseInfoPipeline": 301,},"DOWNLOADER_MIDDLEWARES": {"AmericanRealEstate.middlewares.AlertUserAgentWhenEncounter302Middleware": 545,},"DEFAULT_REQUEST_HEADERS": {"authority": "www.realtor.com","method": "GET","scheme": "https","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,","accept-encoding": "gzip, deflate, br","accept-language": "zh-CN,zh;q=0.9,ja;q=0.8","cache-control": "no-cache","upgrade - insecure - requests": "1","user-agent": "Opera/9.80 (X11; Linux i686; U; hu) Preso/2.9.168 Verssion",},"COOKIES_ENABLED": False,"REDIRECT_ENABLED": False,"LOG_FILE": "realtor_log.txt","LOG_LEVEL": "INFO",}'
custom_settings_str2 = '{"ITEM_PIPELINES": {"AmericanRealEstate.pipelines.RealtorHouseInfoPipeline": 301,},"DOWNLOADER_MIDDLEWARES": {"AmericanRealEstate.middlewares.AlertUserAgentWhenEncounter302Middleware": 545,},"DEFAULT_REQUEST_HEADERS": {"authority": "www.realtor.com","method": "GET","scheme": "https","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,","accept-encoding": "gzip, deflate, br","accept-language": "zh-CN,zh;q=0.9,ja;q=0.8","cache-control": "no-cache","upgrade - insecure - requests": "1","user-agent": "Opera/9.80 (X11; Linux i686; U; hu) Preto/2.9.168 Vversion",},"COOKIES_ENABLED": False,"REDIRECT_ENABLED": False,"LOG_FILE": "realtor_log.txt","LOG_LEVEL": "INFO",}'
custom_settings_str3 = '{"ITEM_PIPELINES": {"AmericanRealEstate.pipelines.RealtorHouseInfoPipeline": 301,},"DOWNLOADER_MIDDLEWARES": {"AmericanRealEstate.middlewares.AlertUserAgentWhenEncounter302Middleware": 545,},"DEFAULT_REQUEST_HEADERS": {"authority": "www.realtor.com","method": "GET","scheme": "https","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,","accept-encoding": "gzip, deflate, br","accept-language": "zh-CN,zh;q=0.9,ja;q=0.8","cache-control": "no-cache","upgrade - insecure - requests": "1","user-agent": "Opera/9.80 (X11; Linux i686; U; hu) Psto/2.9.168 Vern",},"COOKIES_ENABLED": False,"REDIRECT_ENABLED": False,"LOG_FILE": "realtor_log.txt","LOG_LEVEL": "INFO",}'
custom_settings_str4 = '{"ITEM_PIPELINES": {"AmericanRealEstate.pipelines.RealtorHouseInfoPipeline": 301,},"DOWNLOADER_MIDDLEWARES": {"AmericanRealEstate.middlewares.AlertUserAgentWhenEncounter302Middleware": 545,},"DEFAULT_REQUEST_HEADERS": {"authority": "www.realtor.com","method": "GET","scheme": "https","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,","accept-encoding": "gzip, deflate, br","accept-language": "zh-CN,zh;q=0.9,ja;q=0.8","cache-control": "no-cache","upgrade - insecure - requests": "1","user-agent": "Opera/9.80 (X11; Linux i686; U; hu) Prto/2.9.168 Versve9rsion",},"COOKIES_ENABLED": False,"REDIRECT_ENABLED": False,"LOG_FILE": "realtor_log.txt","LOG_LEVEL": "INFO",}'




# custom_settings_str_transform = ast.literal_eval(custom_settings_str4)
# print(custom_settings_str_transform)

custom_settings_str_list = [custom_settings_str,custom_settings_str2,custom_settings_str3,custom_settings_str4]



def execute_spider(num,start_urls,custom_settings,*args,**kwargs):
    print('开启了第{}爬虫进程'.format(num))
    execute(['scrapy', 'crawl', 'realtor'.format(num),
             "-a",
             "start_urls={}".format(start_urls),
             "-a",
             "custom_settings={}".format(custom_settings),
             ])



if __name__=='__main__':
    from AmericanRealEstate.settings import realtor_search_criteria

    #爬虫进程数
    process_nums = 4
    # 生成起始url字符串
    each_spider_criteria_number = int(len(realtor_search_criteria) / process_nums)
    spider_start_urls_list = []
    for i in range(process_nums):
        if i == process_nums-1:
            start_url_str = ','.join(
                realtor_search_criteria[each_spider_criteria_number * i:])
        start_url_str = ','.join(
            realtor_search_criteria[each_spider_criteria_number * i:(i + 1) * each_spider_criteria_number])

        print(start_url_str)
        spider_start_urls_list.append(start_url_str)

    print(len(spider_start_urls_list))
    print('Parent process %s.' % os.getpid())
    p = Pool(process_nums)
    for i in range(process_nums):
        p.apply_async(execute_spider, args=(i, spider_start_urls_list[i], custom_settings_str_list[i], i),)
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')




