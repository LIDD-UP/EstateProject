# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: generate_realtor&trulia_search_condition.py
@time: 2019/1/15
"""
import pandas as pd


data = pd.read_csv('county_stateabbrevation.csv')
print(data.head())

new_data = pd.DataFrame()

# for i in data.loc:
#     print(i)

new_data['countyStateJoin'] = ['-'.join(x.split(' '))+'-County_'+y for i,x in enumerate(data['countyName']) for j,y in enumerate(data['stateAbbreviation']) if i==j]


new_data = new_data.drop_duplicates()
new_data.to_csv('./realtor_search_criteria.csv',index=False)


# print(new_data)
# new_data_list = list(new_data['countyStateJoin'])
# # print(new_data_list)
# for k in new_data_list:
#     print(k)
# #

'Autauga-County_AL'




