import requests
import json



# realtor_web_headers = {
#         "Cache-Control": "public",
#         "Mapi-Bucket": "for_sale_v2:on,for_rent_ldp_v2:on,for_rent_srp_v2:on,recently_sold_ldp_v2:on,recently_sold_srp_v2:on,not_for_sale_ldp_v2:on,not_for_sale_srp_v2:on,search_reranking_srch_rerank1:variant1",        "Host": "mapi-ng.rdc.moveaws.com",
#         "Connection": "Keep-Alive",
#         "Accept-Encoding": "gzip",
#         "User-Agent": "okhttp/3.10.0",
# }


# res = requests.get(url='https://mapi-ng.rdc.moveaws.com/api/v1/properties?offset=9200&limit=150&county=New+York&state_code=NY&sort=relevance&schema=mapsearch&client_id=rdc_mobile_native%2C9.4.2%2Candroid',headers=realtor_web_headers,verify=False)
#
# json_res = json.loads(res.text)
# # print(json_res.keys)
# # dict_res = dict(json_res)
# # print(json_res['matching_rows'])
# # for k,v in json_res.items():
# #     print(k,v)
# print(len(json_res['listings']))
# a = range(3,6)
#
# for i in range(3,6):
#     print(i)
# print(a)
print([x for x  in range(4,10)])

