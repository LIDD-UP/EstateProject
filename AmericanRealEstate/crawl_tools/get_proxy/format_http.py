# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: format_http.py
@time: 2019/1/29
"""
proxy_ip_list = [
'119.101.124.223:9999',
    '119.101.125.75:9999',
    '58.240.7.195:32558',
    '222.217.68.51:39682',
    '119.101.125.180:9999',
    '119.101.126.9:9999',
]

full_proxy_list = '\n'.join(['http://{}'.format(x) for x in proxy_ip_list])
print(full_proxy_list)