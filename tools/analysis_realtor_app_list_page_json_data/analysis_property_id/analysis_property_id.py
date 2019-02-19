import pandas as pd


data = pd.read_csv('./property_id1.csv')
property_id_list = list(set(data['propertyId']))
property_id_list = [x.replace('"','') for x in property_id_list]

# print(len(property_id_list))
# https://mapi-ng.rdc.moveaws.com/api/v1/properties/1564789514?client_id=rdc_mobile_native%2C9.3.7%2Candroid
new_data = pd.DataFrame()
url_sample = 'https://mapi-ng.rdc.moveaws.com/api/v1/properties?offset=0&limit=200&county=New+York&state_code=NY&sort=relevance&schema=mapsearch&client_id=rdc_mobile_native%2C9.4.2%2Candroid'
new_data['detail_api'] = ['https://mapi-ng.rdc.moveaws.com/api/v1/properties/'+str(int(x))+'?client_id=rdc_mobile_native%2C9.3.7%2Candroid' for x in property_id_list]
new_data = new_data.drop_duplicates()
print(new_data)
new_data.to_csv('./realtor_app_detail_page_search_criteria.csv', index=False)