# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: trulia_cookies_analysis.py
@time: 2019/1/22
"""
# cookie_list = [{'domain': 'www.trulia.com', 'httpOnly': False, 'name': 'SERVERID', 'path': '/', 'secure': False, 'value': 'webfe312|XEasr'}, {'domain': '.trulia.com', 'expiry': 1594791597, 'httpOnly': False, 'name': '_pxvid', 'path': '/', 'secure': False, 'value': '25e420b0-1e08-11e9-a729-f9a97b8dbe72'}, {'domain': '.trulia.com', 'expiry': 1548136200, 'httpOnly': False, 'name': '_px3', 'path': '/', 'secure': False, 'value': '966106efae2d29813b3edc82c974a91099c7ebbc6c3f2edd7a32a82eca29ddc7:4VxAZDWMyqyjwTFnM8mv46JqQCDP1Kpx3E+5WJ1twU2JMjmCQ0tZW5dE7l/KavkyKCUrJebqMhzneT2aMGmsiw==:1000:r54nFYHANdugPFdVzySKsNDY5Tivs2DLu9gunml/X1OuDIV0O84Q1C/IHbLLlKd0O8SHf4tEfmEf9reUZK15pXm/59HCLQFJ0lDvJm525sJM/vkh1NzpgJEk1amoo/Oo5LmW0L9BVEMw+OZS6plVfJ2Ug+5QpQI5o9IUh1G2ABY='}]

# for item in cookie_list: driver.add_cookie({
#     'domain': '.trulia.com',
#     'name': item['name'],
#     'value': item['value'],
#     'path': '/',
#     'expires': None
# })

# for item in cookie_list:
#     print(item)


trulia_merge_cookie = 's_fid=433AA466E2E74246-15C3C4922E6D4B9F; tlftmusr=190111pl5oxe6dz6h9ql8f26dy4gw379; fvstts=20190110; _ga=GA1.2.1370343627.1547191941; s_vi=[CS]v1|2E1C236905033FEB-40001188A0008984[CE]; _pxvid=3becfc80-1573-11e9-8c5b-a9eccfd531c4; PHPSESSID=jeggrdnphgs8cccvlpbs45i1j0; csrft=jA0ya2SbWv3cOtEpj66HYO%2BeAi5DCp0GGeJWxahT8pk%3D; _gid=GA1.2.1042690951.1548056115; QSI_S_ZN_aVrRbuAaSuA7FBz=v:0:0; s_cc=true; trul_visitTimer=1548129963418_1548130008013; tabc=%7B%221071%22%3A%22a%22%2C%221022%22%3A%22b%22%2C%221052%22%3A%22a%22%2C%221053%22%3A%22a%22%7D; _gat=1; search_parameter_set=%7B%22searchType%22%3A%22for_sale%22%2C%22location%22%3A%7B%22cities%22%3A%5B%7B%22city%22%3A%22New+York%22%2C%22state%22%3A%22NY%22%7D%5D%7D%2C%22filters%22%3A%7B%22page%22%3A1%2C%22view%22%3A%22map%22%2C%22limit%22%3A30%2C%22sort%22%3A%7B%22type%22%3A%22best%22%2C%22ascending%22%3Atrue%7D%7D%7D; _px3=f594a4d53bde57904647e1f4db4c92f5f68099a1821646759a602ba8d22758c8:uU3dER1KfV+oHwlRrE4BSJ+5gmvFS8yTqiMNpC4O+AmS5sjcwKSxVt79o3GBjZnMYsA1VCmdUCUfg37ip4ih9g==:1000:j3RWTPnbP/Ovb7wfVt/uAKrO+xQBqgfCbzEfcWq7sZxiOmDNnG8OhRdsFtctRyp99vPnCt8TN0pIg6vIKjmDuXzB1gEOoGr1M0fHUq/Zs4EBZ+9zAm3PNANNZWauDKz+mSUHLfDIdbKPWbtliNzxH0gcxQE1rASg49jYSxV+E+g=; promptdata=%7B%22c%22%3A%7B%22pg-srp%22%3A9%7D%2C%22pd%22%3A%5B%5D%2C%22pts%22%3Anull%7D; SERVERID=webfe335|XEaqW'
trulia_merge_cookie_list = trulia_merge_cookie.split(';')
print(len(trulia_merge_cookie_list))
for tru in trulia_merge_cookie_list:
    print(tru.split('=')[0]+":"+tru.split('=')[1])

