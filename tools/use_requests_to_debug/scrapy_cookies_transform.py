# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: scrapy_cookies_transform.py
@time: 2019/1/22
"""
class transCookie:
  def __init__(self, cookie):
     self.cookie = cookie

  def stringToDict(self):

     itemDict = {}
     items = self.cookie.split(';')
     for item in items:
        key = item.split('=')[0].replace(' ', '')
        value = item.split('=')[1]
        itemDict[key] = value
     return itemDict

if __name__ == "__main__":
  cookie = "s_fid=433AA466E2E74246-15C3C4922E6D4B9F; tlftmusr=190111pl5oxe6dz6h9ql8f26dy4gw379; fvstts=20190110; _ga=GA1.2.1370343627.1547191941; s_vi=[CS]v1|2E1C236905033FEB-40001188A0008984[CE]; _pxvid=3becfc80-1573-11e9-8c5b-a9eccfd531c4; PHPSESSID=jeggrdnphgs8cccvlpbs45i1j0; csrft=jA0ya2SbWv3cOtEpj66HYO%2BeAi5DCp0GGeJWxahT8pk%3D; _gid=GA1.2.1042690951.1548056115; QSI_S_ZN_aVrRbuAaSuA7FBz=v:0:0; s_cc=true; fontsLoaded=1; __gads=ID=e54b8c8a9d0a3af6:T=1548144822:S=ALNI_MbTTP258XwNoU2W760CAOClFmDtSg; previousSearchOptions=optQuery0%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DNew%2BYork%2526state%253DNY%2526st%253Dh%3BoptQuery1%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526city%253DClayton%2526state%253DAL%2526zip_code%253D36016%2526st%253Dh%3BoptQuery2%3Dprice_reductions%253D0%2526type%253Daddress%2526open_homes%253D0%2526subtype%253Dcity%2526state%253DNY%2526zip_code%253D10001%2526st%253Dh; previousSearches=locQuery0%3DNew%2BYork%2C%2BNY%3BlocQuery1%3DClayton%2C%2BAL%3BlocQuery2%3D%2C%2BNY; search_parameter_set=%7B%22searchType%22%3A%22for_sale%22%2C%22location%22%3A%7B%22zips%22%3A%5B%2210001%22%5D%7D%2C%22filters%22%3A%7B%22page%22%3A1%2C%22view%22%3A%22map%22%2C%22limit%22%3A30%2C%22sort%22%3A%7B%22type%22%3A%22best%22%2C%22ascending%22%3Atrue%7D%7D%7D; promptdata=%7B%22c%22%3A%7B%22pg-srp%22%3A21%2C%22pg-pdp%22%3A4%7D%2C%22pd%22%3A%5B%5D%2C%22pts%22%3Anull%7D; s_sq=%5B%5BB%5D%5D; tabc=%7B%221071%22%3A%22a%22%2C%221022%22%3A%22b%22%2C%221052%22%3A%22a%22%2C%221053%22%3A%22a%22%7D; _gat=1; trul_visitTimer=1548152351080_1548155547267; SERVERID=webfe377|XEb6n; _px3=ae2b223470f2211a06c251d79e6fc3fd4ab070213a5b4ddb3e8a4ff995a4dde6:hgJoObRC/kdjy8V3U8ctgEYsdUwVpwS0uyiym/KS27PvCsWwLZrKNseEZyaTOxfZcPXbrJpD4qo17dvhHgax7w==:1000:NkoBM/FQrYvhH9O4n5rJhH2ykeszilkUq/3cj/muGGNbOmFfExjY1L4+s8vrpW+1YCVUMTABKlrwBiaiIY0t1x5ztzchB9T8RwP59XVhvbAFrGBQLRjHxExR+/je78iAysaYxUmu392G5SOIF9+qUbsJbiWQn1yITdm8gJq51bg="
  trans = transCookie(cookie)
  print (trans.stringToDict())