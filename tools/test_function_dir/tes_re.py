# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: tes_re.py
@time: 2019/1/10
"""
import re
# source_str = 'https://www.trulia.com/sitemap/Louisiana-real-estate/Acadia-Parish-22001/'
source_str1 = ' / realestateandhomes - detail / 60 - Riverside - Blvd - Apt - 1112_New - York_NY_10069_M37676 - 31493'

x = re.findall(r'M\d{5} - \d{5}',source_str1)
if len(x)!=0:
    print(x)