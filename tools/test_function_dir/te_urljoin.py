# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: te_urljoin.py
@time: 2019/1/11
"""
from urllib.parse import urljoin

a ='https://www.realtor.com/realestateandhomes-search/Monroe-County_NY/pg-2'
b = '/realestateandhomes-search/Monroe-County_NY/pg-3'
c  = urljoin(a,b)
print(c)