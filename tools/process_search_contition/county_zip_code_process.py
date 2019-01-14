# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: county_zip_code_process.py
@time: 2019/1/14
"""
import pandas as pd


data = pd.read_csv('./raw_search_data/county_zip_code.csv')

print(data.head())
new_data = pd.DataFrame()
new_data['countyName'] = [' '.join([x for x in y.split(' ') if x != '']) for y in data['countyName']]
new_data['zipCode'] = [str(x).replace(' ','') for x in data['zipCode']]
print(new_data.head())
print(data[['countyName','zipCode']].head())
# for i in range(len(data)):
#     ' '.join([x for x in data.iloc[i]['countyName'].split(' ') if x != ''])

new_data.to_csv('true_zip_code.csv',index=False)
