# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: realtor_crawl_script.py
@time: 2019/1/24
"""
for search_criteria in search_criterias:
    # 向爬虫传递start_url
        # 爬虫内部出现302 超过10次之后激发停止爬虫
    #这里可能出现爬虫停止之后整个程序一起停止;或者是无限等待的情况;
