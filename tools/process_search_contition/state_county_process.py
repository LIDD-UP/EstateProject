# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: state_county_process.py
@time: 2019/1/14
"""
import pandas as pd


data = pd.read_csv('./raw_search_data/state_county.csv')

print(data.drop(columns=['id']).head())
new_data = pd.DataFrame()
new_data['stateName'] = [' '.join([x for x in y.split(' ') if x != '']) for y in data['stateName']]
new_data['countyName'] = [' '.join([x for x in y.split(' ') if x != '']) for y in data['countyName']]
new_data['county'] = [' '.join([x for x in y.split(' ') if x != '']) for y in data['county']]
print(new_data.head())
new_data.to_csv('true_state_county.csv',index=False)