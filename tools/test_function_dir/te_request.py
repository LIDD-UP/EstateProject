import requests

# cookies = {
#     "jinxinfu.session.id":"d16ee9c6d3d84c119e1d9d1453cc8da2",
#     "Path" : "/"
# }
# req = requests.session()
# res = req.get()



def GetCookie():
    s=requests.session()
    print(s.cookies.get_dict())

    loginUrl='https://prod.51jt.com/app/wyjt/api'
    postData={'actionName':'login','methodName':'submit','param':'{"ak": "Android", "appVersion": "3.46", "channeId": "10003","deviceModel": "SM-G925F", "deviceToken": "355980021180108","osType": "android", "osVersion": "5.1.1","password": "8f96af18b0f195bbae783f18bcd9d840","phoneNo": "17611378735"}'
    }
    rs=s.post(loginUrl,postData)
    print(rs.text)
    # c=requests.cookies.RequestsCookieJar()#利用RequestsCookieJar获取
    # c.set('jinxinfu.session.id','77cbb1372a784fb6b8fc892ad5170abe for prod.51jt.com/')
    # # print(s.cookies)
    # requ2 = requests.session()
    # requ2.cookies.update(c)
    postData2 = {'actionName': 'friend', 'methodName': 'applyAddFriend',
                'param': '{"friendId":"2756258","note":"hi"}'
                }
    rs2 = s.post(loginUrl, postData2)
    print(rs2.text)
    # s.cookies.update(c)
    # print(s.cookies.get_dict())







def DirLogin():
    s=requests.session()
    url='https://prod.51jt.com/app/wyjt/api'
    headers={
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Cache-Control': 'max-age=0',
    # 'Connection': 'keep-alive',
    # 'Host': '***',
    # 'Referer': 'http://***/***/admin_index.php'
    }
    postData = {'actionName': 'login', 'methodName': 'submit',
                'param': '{"ak": "Android", "appVersion": "3.46", "channeId": "10003","deviceModel": "SM-G925F", "deviceToken": "355980021180108","osType": "android", "osVersion": "5.1.1","password": "8f96af18b0f195bbae783f18bcd9d840","phoneNo": "17611378735"}'
                }
    rs = s.post(url, postData)
    cookies={'cookie-name': 'cookie-value', 'jinxinfu.session.id': '81323fe8db6d45d797387991b19d6b35'}#这里就是利用上面的函数获得的Cookies
    rs=s.get(url,headers=headers,cookies=cookies,verify=False)
    rs.encoding='utf-8'
    print(rs.text)


# GetCookie()


'''

16:53:28
17611378735，wc199422
'''


def GetCookie1():
    s=requests.session()
    print(s.cookies.get_dict())
    apiUrl='https://prod.51jt.com/app/wyjt/api'
    loginPostData={'actionName':'login','methodName':'submit','param':'{"ak": "Android", "appVersion": "3.46", "channeId": "10003","deviceModel": "SM-G925F", "deviceToken": "355980021180108","osType": "android", "osVersion": "5.1.1","password": "8f96af18b0f195bbae783f18bcd9d840","phoneNo": "17611378735"}'
    }
    rs=s.post(apiUrl,loginPostData)
    print(rs.text)
    postData2 = {'actionName': 'friend', 'methodName': 'applyAddFriend',
                'param': '{"friendId":"2756258","note":"hi"}'
                }
    rs2 = s.post(apiUrl, postData2)
    print(rs2.text)


GetCookie1()