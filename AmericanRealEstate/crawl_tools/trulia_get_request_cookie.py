# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: trulia_get_request_cookie.py
@time: 2019/1/22
"""

import requests
# import json
#
# trulia_headers ={
# 'authority': 'www.trulia.com',
# # 'method': 'GET',
# # 'path':'/sitemap/Alabama-real-estate/',
# 'scheme': 'https',
# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'accept-encoding': 'gzip, deflate, br',
# 'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
# 'cache-control': 'max-age=0',
# 'cookie':'s_fid=433AA466E2E74246-15C3C4922E6D4B9F; tlftmusr=190111pl5oxe6dz6h9ql8f26dy4gw379; fvstts=20190110; _ga=GA1.2.1370343627.1547191941; s_vi=[CS]v1|2E1C236905033FEB-40001188A0008984[CE]; _pxvid=3becfc80-1573-11e9-8c5b-a9eccfd531c4; SERVERID=webfe335|XEV18',
# 'referer': 'https://www.trulia.com',
# 'upgrade-insecure-requests': '1',
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
#
# }
# state = requests.get(url='https://www.trulia.com/County/AL/Autauga_Real_Estate/',headers=trulia_headers)
# print(type(state.cookies))
#
# with open('./test_html.html','w') as f:
#     f.write(state.text)


res = requests.session()
res = res.get('https://www.trulia.com/County/AL/Autauga_Real_Estate')
cookie = res.cookies
print(res.text)
print(res.headers)
print(cookie)
