# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: tes_re.py
@time: 2019/1/10
"""
import re
source_str = 'https://www.trulia.com/sitemap/Louisiana-real-estate/Acadia-Parish-22001/'

x = re.findall(r'Parish',source_str)
if len(x)!=0:
    print(x)