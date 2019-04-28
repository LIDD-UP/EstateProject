import pandas as pd
import re

data = list(pd.read_csv('./realtor_search_criteria.csv')['countyStateJoin'])

new_data = pd.DataFrame()

new_data['search_text'] = [re.findall(r'search/(.*)',x)[0].split('_')[0].replace('-',' ')+','+ re.findall(r'search/(.*)',x)[0].split('_')[1] for x in data]
# new_data['state'] = [re.findall(r'search/(.*)',x)[0].split('_')[1] for x in data]

new_data.to_csv('./trulia_search_text.csv',index=False)

