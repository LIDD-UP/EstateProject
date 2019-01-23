# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: get_state.py
@time: 2019/1/9
"""
import requests
import json


cookie3 = 'PHPSESSID=4eavs7vnd1fgkd8ppgpe7p9m71; tlftmusr=190123plrupu1xed2xa7wdndmzq8w372; fvstts=20190122; csrft=Qfm8I4YnAAqQFPe4qo2zvu%2B7MtZbtKmVgAQFksCNj1M%3D; SERVERID=webfe337|XEgNs; _ga=GA1.2.1650952074.1548225867; _gid=GA1.2.2086241566.1548225867; G_ENABLED_IDPS=google; trul_visitTimer=1548225868039_1548225970431; s_fid=3C39829E9232E2D2-22EA23AB4DC0B4F4; s_cc=true; _pxvid=548ef6b0-1eda-11e9-9293-b3dd52f6f3dc; s_vi=[CS]v1|2E2406A6052A395C-6000010640000AB7[CE]; _px3=de8286f507bae5e3c347c623355654f921b7d1652c7504db4266539b16fed0e1:KLDMdvh449Y0WY9y/PLZvAbo0cHSx2hFq3HuxKeMc2/iyDVcSyRgucwehxx9Oo4WikljBGUH/IAmbkz1XSVAqw==:1000:PmYmdiO0chQlsP4pUk5SgoLlE8JHnxo5LiDBawgy0eXNwetH8seCW99ZO1bNs48xr8WQ/2XLK1BMNW5nq29TYZCXxETzimmCq7sdW+vwV18ClqKseXAkyBP3UOAVX+YcgITDsiEthMWRO3XGsh8yz8rxtl8zRLCR/EWKdJ6z+g8=; QSI_S_ZN_aVrRbuAaSuA7FBz=v:0:0'

trulia_headers ={
'authority': 'www.trulia.com',
# 'method': 'GET',
# 'path':'/sitemap/Alabama-real-estate/',
'scheme': 'https',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
'cache-control': 'max-age=0',
# 'cookie':'s_fid=433AA466E2E74246-15C3C4922E6D4B9F; tlftmusr=190111pl5oxe6dz6h9ql8f26dy4gw379; fvstts=20190110; _ga=GA1.2.1370343627.1547191941; s_vi=[CS]v1|2E1C236905033FEB-40001188A0008984[CE]; _pxvid=3becfc80-1573-11e9-8c5b-a9eccfd531c4; PHPSESSID=jeggrdnphgs8cccvlpbs45i1j0; csrft=jA0ya2SbWv3cOtEpj66HYO%2BeAi5DCp0GGeJWxahT8pk%3D; _gid=GA1.2.1042690951.1548056115; QSI_S_ZN_aVrRbuAaSuA7FBz=v:0:0; s_cc=true; fontsLoaded=1; __gads=ID=e54b8c8a9d0a3af6:T=1548144822:S=ALNI_MbTTP258XwNoU2W760CAOClFmDtSg; previousSearchOptions=optQuery0%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DNew%2BYork%2526state%253DNY%2526st%253Dh%3BoptQuery1%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DClayton%2526state%253DAL%2526zip_code%253D36016%2526st%253Dh%3BoptQuery2%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526state%253DNY%2526zip_code%253D10001%2526st%253Dh; previousSearches=locQuery0%3DNew%2BYork%2C%2BNY%3BlocQuery1%3DClayton%2C%2BAL%3BlocQuery2%3D%2C%2BNY; search_parameter_set=%7B%22searchType%22%3A%22for_sale%22%2C%22location%22%3A%7B%22zips%22%3A%5B%2210001%22%5D%7D%2C%22filters%22%3A%7B%22page%22%3A1%2C%22view%22%3A%22map%22%2C%22limit%22%3A30%2C%22sort%22%3A%7B%22type%22%3A%22best%22%2C%22ascending%22%3Atrue%7D%7D%7D; promptdata=%7B%22c%22%3A%7B%22pg-srp%22%3A21%2C%22pg-pdp%22%3A4%7D%2C%22pd%22%3A%5B%5D%2C%22pts%22%3Anull%7D; s_sq=%5B%5BB%5D%5D; tabc=%7B%221071%22%3A%22a%22%2C%221022%22%3A%22b%22%2C%221052%22%3A%22a%22%2C%221053%22%3A%22a%22%7D; _gat=1; trul_visitTimer=1548152351080_1548155547267; SERVERID=webfe377|XEb6n; _px3=ae2b223470f2211a06c251d79e6fc3fd4ab070213a5b4ddb3e8a4ff995a4dde6:hgJoObRC/kdjy8V3U8ctgEYsdUwVpwS0uyiym/KS27PvCsWwLZrKNseEZyaTOxfZcPXbrJpD4qo17dvhHgax7w==:1000:NkoBM/FQrYvhH9O4n5rJhH2ykeszilkUq/3cj/muGGNbOmFfExjY1L4+s8vrpW+1YCVUMTABKlrwBiaiIY0t1x5ztzchB9T8RwP59XVhvbAFrGBQLRjHxExR+/je78iAysaYxUmu392G5SOIF9+qUbsJbiWQn1yITdm8gJq51bg=',
'cookie': cookie3,
'referer': 'https://www.trulia.com',
'upgrade-insecure-requests': '1',
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',

}
# state = requests.get(url='https://www.trulia.com/County/AL/Autauga_Real_Estate/',
#                      headers=trulia_headers,
#                      verify=False)
# # print(type(state.cookies))
# print(state.text)
#
# with open('./test_html.html','w') as f:
#     f.write(state.text)

# session = requests.session()
# res = session.get(url='https://www.trulia.com/County/AL/Autauga_Real_Estate/',headers=trulia_headers,verify=False)
# print(res.text)
#
# print(session.cookies)
# cookies2 = requests.utils.dict_from_cookiejar(session.cookies)
#
# header2 = {
#     "cookie": {}
# }
#
# res2 = requests.get('https://www.trulia.com/County/AL/Autauga_Real_Estate/',)
# session










res = requests.get(url='https://www.trulia.com/p/al/gulf-shores/1421-w-lagoon-ave-b-gulf-shores-al-36542--2178117798',headers=trulia_headers,verify=False)
print(res.text)