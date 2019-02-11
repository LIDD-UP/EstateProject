# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: te_fake_user_agent.py
@time: 2019/1/25
"""
import requests
from fake_useragent import UserAgent
import json

# ua = UserAgent()
# print(ua['browsers'])
# print(ua.)
# for x in ua.ie:
#     print(x)

# user_agent_json = requests.get(url='http://fake-useragent.herokuapp.com/browsers/0.1.11')
# print(type(user_agent_json.text))
# true_user_agent_json = json.loads(user_agent_json.text)
# print(type(true_user_agent_json))

# with open('./user-agent.json','r') as f:
#     with open('./user_agent_list.txt','w') as f2:
#         true_user_agent_json = json.loads(f.read())
#         print(type(true_user_agent_json))
#         print(true_user_agent_json.keys())
#         # dict_keys(['browsers', 'randomize'])
#         # dict_keys(['chrome', 'opera', 'firefox', 'internetexplorer', 'safari'])
#         print(true_user_agent_json['browsers'].keys())
#         for x in true_user_agent_json['browsers']:
#             for browser in true_user_agent_json['browsers'][x]:
#                 f2.write('\'')
#                 f2.write(browser)
#                 f2.write('\'')
#                 f2.write(',')
#                 f2.write('\n')
#
#
#         # 总共有200;
from fake_useragent import utils

# ua = UserAgent()
# print(ua)
# print(ua.ie)
# print(help(ua))

ret = utils.load()
print(utils.get_browsers())
print(len(utils.get_browser_versions('Chrome')))

print(ret)

