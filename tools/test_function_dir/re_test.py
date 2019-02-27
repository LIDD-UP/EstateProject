# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: re_test.py
@time: 2019/2/27
"""

import re

source_str = 'http://1234556'
a= re.search('\d+',source_str).group()
print(a)