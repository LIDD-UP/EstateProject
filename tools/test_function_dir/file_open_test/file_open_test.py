# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: file_open_test.py
@time: 2019/1/30
"""
import requests
with open('./test.txt','w') as f:
    for i in range(2):
        result = requests.get('http://www.baiduc.com')
        f.write('sssssssss')