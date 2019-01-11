# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: get_state.py
@time: 2019/1/9
"""
import requests
import json

trulia_headers ={
'authority': 'www.trulia.com',
'method': 'GET',
# 'path':'/sitemap/Alabama-real-estate/',
'scheme': 'https',
# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
'cache-control': 'max-age=0',
# 'cookie':'_pxvid=05b33ba0-1304-11e9-be80-9143a92e94bf; s_fid=091772EA4252BCF3-30BDFCA435C410CC; PHPSESSID=vj6b7af38oqrrr0aehfqmqkho4; tlftmusr=190108pl07q98uuuefvs6nqxgg00w200; fvstts=20190108; csrft=60gaQOvgw%2Fp7eh0FCcWF5LVfL3UBaHguiFbnBzfL56E%3D; _ga=GA1.2.1739258178.1546936361; _gid=GA1.2.233419384.1546936361; s_cc=true; G_ENABLED_IDPS=google; s_vi=[CS]v1|2E1A303E05316460-40000114000000CC[CE]; QSI_S_ZN_aVrRbuAaSuA7FBz=v:0:0; fontsLoaded=1; __gads=ID=8c7c897faf592e2c:T=1546936722:S=ALNI_MY0hzlDQvXNNDEo2j_KzgUapqeVkQ; previousSearchOptions=optQuery0%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DNassau%2526state%253DNY%2526st%253Dh%3BoptQuery1%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DMontgomery%2526state%253DAL%2526st%253Dh%3BoptQuery2%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DJuneau%2526state%253DAK%2526st%253Dh%3BoptQuery3%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DNew%2BYork%2526state%253DNY%2526st%253Dh%3BoptQuery4%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DAmerican%2BCanyon%2526state%253DCA%2526st%253Dh; previousSearches=locQuery0%3DNassau%2C%2BNY%3BlocQuery1%3DMontgomery%2C%2BAL%3BlocQuery2%3DJuneau%2C%2BAK%3BlocQuery3%3DNew%2BYork%2C%2BNY%3BlocQuery4%3DAmerican%2BCanyon%2C%2BCA; search_parameter_set=%7B%22searchType%22%3A%22for_sale%22%2C%22location%22%3A%7B%22cities%22%3A%5B%7B%22city%22%3A%22New+York%22%2C%22state%22%3A%22NY%22%7D%5D%7D%2C%22filters%22%3A%7B%22page%22%3A1%2C%22view%22%3A%22map%22%2C%22limit%22%3A30%2C%22sort%22%3A%7B%22type%22%3A%22best%22%2C%22ascending%22%3Atrue%7D%7D%7D; promptdata=%7B%22c%22%3A%7B%22pg-srp%22%3A23%2C%22pg-pdp%22%3A12%7D%2C%22pd%22%3A%5B%5D%2C%22pts%22%3Anull%7D; s_sq=%5B%5BB%5D%5D; trul_visitTimer=1547022942454_1547023923594; SERVERID=webfe902|XDW2N; _px3=16c280b25b22146133e6300c3849888074cac604fad9832b741ecc7c16eedcb0:/h9aVy8h1snaWH6FxYxD3dM7Nve9PDofXUU5AL0/0mv1tiVblPOdQRkMXZr1NHTUyWG/apF2DNESBJGj6eohFA==:1000:4fE9ljEmSuHOK8RfsW+J8LWPUSGfsqHjZS0cMk3dv06YLvRyp8KhLDc5s6nszaq0X1PiF1XTrI2Ov75ChnX2RMfuq+zAj9RMIwQ55CWHW+34YqPjoA2FDcHnRbE5uSeM/vx2mAa0zsr9Ca+UpuUu5DN2dQBnCLAsRZiVFw69mxE=',
# 'referer': 'https://www.trulia.com/sitemap/,',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'

}
state = requests.get(url='https://www.realtor.com/property-overview/M4319803655')
print(json.loads(state.text))
with open('./test_html.json','w') as f:
    f.write(str(json.loads(state.text)))