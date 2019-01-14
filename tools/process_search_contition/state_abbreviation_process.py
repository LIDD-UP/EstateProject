# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: state_abbreviation_process.py
@time: 2019/1/14
"""
import pandas as pd

data = pd.read_csv('./raw_search_data/state_abbraviation.csv')

print(data.head())
new_data = pd.DataFrame()
new_data['stateName'] = [' '.join([x for x in y.split(' ') if x != '']) for y in data['stateName']]
new_data['stateAbbreviation'] = [str(x).replace(' ','') for x in data['stateAbbreviation']]
print(new_data.head())
print(data.head())
new_data.to_csv('true_state_abbreviation.csv',index=False)


# for i in range(len(data)):
#     print(i)