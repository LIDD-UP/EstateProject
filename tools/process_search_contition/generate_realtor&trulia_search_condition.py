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

# generate realtor search criteria
# new_data['countyStateJoin'] = ['https://www.realtor.com/realestateandhomes-search/'+'-'.join(x.split(' '))+'-County_'+y for i,x in enumerate(data['countyName']) for j,y in enumerate(data['stateAbbreviation']) if i==j]
# new_data = new_data.drop_duplicates()
# new_data.to_csv('./realtor_search_criteria.csv',index=False)
# 'County / KY / Webster_Real_Estat'

# generate trulia search critertia
# County/NY/New_York_Real_Estate/
# new_data['countyStateJoin'] = ['https://www.trulia.com/County'+'/'+y+'/'+'_'.join(x.split(' '))+'_Real_Estate' for i,x in enumerate(data['countyName']) for j,y in enumerate(data['stateAbbreviation']) if i==j]
# new_data = new_data.drop_duplicates()
# print(new_data)
# new_data.to_csv('./trulia_search_criteria.csv',index=False)



# generate realtor app list page url interface
url_sample = 'https://mapi-ng.rdc.moveaws.com/api/v1/properties?offset=0&limit=200&county=New+York&state_code=NY&sort=relevance&schema=mapsearch&client_id=rdc_mobile_native%2C9.4.2%2Candroid'
new_data['countyStateJoin'] = ['https://mapi-ng.rdc.moveaws.com/api/v1/properties?offset=0&limit=200&county='+'+'.join(x.split(' '))+'&state_code='+y+'&sort=relevance&schema=mapsearch&client_id=rdc_mobile_native%2C9.4.2%2Candroid' for i,x in enumerate(data['countyName']) for j,y in enumerate(data['stateAbbreviation']) if i==j]
new_data = new_data.drop_duplicates()
print(new_data)
new_data.to_csv('./realtor_app_list_page_search_criteria.csv',index=False)


# print(new_data)
# new_data_list = list(new_data['countyStateJoin'])
# # print(new_data_list)
# for k in new_data_list:
#     print(k)
# #

'Autauga-County_AL'

# County/NY/New_York_Real_Estate/




