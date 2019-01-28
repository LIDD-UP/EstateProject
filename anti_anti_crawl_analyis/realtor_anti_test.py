# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: realtor_anti_test.py
@time: 2019/1/23
"""
import requests


realtor_cookies = {
    # google 通用浏览器标识
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,ja;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.realtor.com',
    'Upgrade-Insecure-Requests': '1',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3452.0 Safari/537.36'
    # 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; ; x64; rv:0.0) Gecko/1 Fiox/5.0',
    # 'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',

    # 'user-agent' : 'Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50',

    # firefox 通用浏览器标识
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Connection': 'keep-alive',
    # 'Host':'www.realtor.com',
    # 'Upgrade-Insecure-Requests':'1',
    # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',

    # 'user-agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
      # 1111111111有问题的cookie
      # 'cookie':'_ss=1366x768; threshold_value=89; clstr=v; clstr_tcv=54; split_tcv=60; __vst=fd0f0f5d-d57b-48c8-84f7-ee9332f86618; __gads=ID=c9c6bc68343b1c38:T=1547191429:S=ALNI_MbEoOR211jKBxjj3c6AxORc9rNejw; _gcl_au=1.1.462908694.1547191500; ajs_user_id=null; ajs_group_id=null; _ga=GA1.2.1809646443.1547191147; __qca=P0-1856484682-1547191544959; ajs_anonymous_id=%22db0f4b00-cb6b-4f3b-b074-13c91af6e735%22; _ncg_g_id_=4911c6ac-7925-4d04-8b99-bce40fcc0b74; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-179204249%7CMCIDTS%7C17919%7CMCMID%7C78470061863700216203027265384897932330%7CMCAAMLH-1548725294%7C11%7CMCAAMB-1548725295%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-549291961%7CMCOPTOUT-1548127694s%7CNONE%7CMCAID%7CNONE; _gid=GA1.2.1644294370.1548120496; _ncg_id_=1682b97e315-51c4ce99-0b7f-4994-8781-14746f45fe7f; __ssn=dae48bd1-8575-48ac-9d51-27bd07bacfca; __ssnstarttime=1548221607; userStatus=return_user; automation=false; split=n; bcc=false; bcvariation=SRPBCRR%3Av1%3Adesktop; header_slugs=gs%3DAdair-County_MO%26lo%3DAdair%26st%3Dcounty; ab_srp_viewtype=ab-list-view; criteria=loc%3DAdair+County%2C+MO%26locSlug%3DAdair-County_MO%26lat%3D40.190562%26long%3D-92.600719%26status%3D1%26pg%3D1%26pgsz%3D48%26sprefix%3D%2Frealestateandhomes-search%26city%3DAdair+County%26state_id%3DMO; srchID=be158ecc1301418f8a3b881bc47a8bc5; _ncg_sp_ses.cc72=*; _ncg_sp_id.cc72=c8b8f168-bbc0-4797-b97c-384bcd5da00d.1548122553.5.1548229700.1548143865.7e020ece-e650-47b8-a75b-5cc6c9b51159; _gat=1; _fbp=fb.1.1548229728818.1374132530; AWSALB=Y4tUvKWq9vW+cJWf/hchEBV5UXFCpmqTrIq0V6z21KR1sMDFiVJFk2Lp2y/NGujzo/LwPWO82780fYzkV75aqmghJQ16mq18TCfpd//BbNBhgODeSGsrst1L35FPJ60t/iVcZRGHIWWeLLcrppKSZ4Xn5rKX+QIFJLL792yewHCnO1vmvqJIo1hf8gvPmQ==; _rdc-next_session=YTZ4OFpBWmFacWdlSDU0bHNobWpNaTdvVElDaVZmUkF6Qm1wS0d6eml4TXBMRlNTeEMvd1gwZnpyWi9iR095Ti96OXRjWWtMZ2g0STRwc3VVbEJKalQxNitrYk00bTllUnRVbkZ3RENhcHJYZUlrU2lJM3k2T05aSDZaeDBPajIyenNraEJoTEMwMy81Q21sVk80U24vcERkeTNTQXpoc2xiV1hLcFFaNDBpNXhkRm5mNk1nMTVDbmtSODZFemg5eWJQU3NjYzE1RzUzYVF2K3IwZjluN1Jwc3Q0ZTVPMFpCNFVQVUdaWXZmRGNCQmxxNGJWOHdlWFJOOHpzOWtIZy0tQVJ6S3dhVEdzVEhjK2ZraXVJbFJOUT09--5bbc8ab8edad53da2494199db14e5fa6a799e42a; _4c_=fVPbctowEP2VjJ5j0P3CGyGdJm0JhCSlfWKEJYOLwR7ZQEjg37uC3KaZqR%2Fk3dVejs8eP6Pt3K9QhwiuKTWKKybxOVr4XY06zyit4rmJxzoUqIPmTVPVnXZ7u922grdFU4ZWWi7b0fZ1YxtvV25eLn2d1N6GdN7uOpuHpFeuV81u0h%2Bgc5SWzkMrYlqqRcFvnsDjGoNZhdKt02bS7KqYsvXTs9ot4OJrWc4Kf30JwczhDGfCJU6oacJ1qhPNM5V4bxijmZaSaKj4mdc5oDuWJEQZijnlZt%2FvXV%2Fe3%2B0hQKLTv77cK80VxlAlGbwpkRQzTBWVgmmujTKMMoYhudvt%2F7hKIlWKCmr4npBT9OI9KPaj7%2FNq9KQXYUabHwNZzda%2FxpUoi0U3fVjlt7%2BHV7Y%2FHs%2FcN%2Fb4NBzfLt0fvIM2gOtqnwhuKCCTsfFgeD94uD%2B2JlRJw%2Bv9zeDmSxwJqKMZyZsHX8%2FLwk02tlhH0rSBcD3Z5GC%2F8zA5EgH%2Bha19apewWHQD7jTd2JDbJi9BBehuNLzojUadDek4Xy%2Basor7KuomwOUmpodyW%2Fvo9eYB1nymCERLEAsa5ysHl%2BAGn%2FkQjlkRSt5EWB%2FU8hIEkb3H4%2FI3URVRBkWZgpzAA2nC7ruThyN6orGRXHLOWkCKIoYQrtDhHD2eBMyIJAwbQYGWBtSqJcfxgYyQuxclo8wSi6fC6YxrqSghxhOpMkxFmllPHHrpJ4SGaUYLKQ4ncMd6gv%2Bdx8XneSee%2FlMk%2BOeiqnhNf8um8DsygPE6gvC37Ljg0xdhLqZSkExqq7FOrRdeK0YcyzhOs5SgD%2B2IgOH0lSFg9NjtcPgL',
    # 2222222222goole
    #   'cookie':'_ss=1366x768; threshold_value=89; clstr=v; clstr_tcv=54; split_tcv=60; __vst=fd0f0f5d-d57b-48c8-84f7-ee9332f86618; __gads=ID=c9c6bc68343b1c38:T=1547191429:S=ALNI_MbEoOR211jKBxjj3c6AxORc9rNejw; _gcl_au=1.1.462908694.1547191500; ajs_user_id=null; ajs_group_id=null; _ga=GA1.2.1809646443.1547191147; __qca=P0-1856484682-1547191544959; ajs_anonymous_id=%22db0f4b00-cb6b-4f3b-b074-13c91af6e735%22; _ncg_g_id_=4911c6ac-7925-4d04-8b99-bce40fcc0b74; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-179204249%7CMCIDTS%7C17919%7CMCMID%7C78470061863700216203027265384897932330%7CMCAAMLH-1548725294%7C11%7CMCAAMB-1548725295%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-549291961%7CMCOPTOUT-1548127694s%7CNONE%7CMCAID%7CNONE; _gid=GA1.2.1644294370.1548120496; _ncg_id_=1682b97e315-51c4ce99-0b7f-4994-8781-14746f45fe7f; __ssn=dae48bd1-8575-48ac-9d51-27bd07bacfca; __ssnstarttime=1548221607; userStatus=return_user; automation=false; split=n; bcc=false; bcvariation=SRPBCRR%3Av1%3Adesktop; header_slugs=gs%3DAdair-County_MO%26lo%3DAdair%26st%3Dcounty; ab_srp_viewtype=ab-list-view; criteria=loc%3DAdair+County%2C+MO%26locSlug%3DAdair-County_MO%26lat%3D40.190562%26long%3D-92.600719%26status%3D1%26pg%3D1%26pgsz%3D48%26sprefix%3D%2Frealestateandhomes-search%26city%3DAdair+County%26state_id%3DMO; srchID=be158ecc1301418f8a3b881bc47a8bc5; _ncg_sp_ses.cc72=*; _fbp=fb.1.1548229728818.1374132530; AWSALB=/bTmyIu5nlvbnACPmfjR1nAT2QtPGZjWun45It7FAVGsHuftFBvIWLc+38t9pAsLy2yUqUXMNpha1iMQGBv+ATeWIch7JhWPNybKy8LzVYGMFSQiF6Z8kJfP3hHV3m40228anyBezHl3NwQiHhK4s/nNH5zibgotk1hn86s0opoCavwjXQTIiP5doylcUQ==; _rdc-next_session=dDNod0Nvd1ZDdEZDV0xQV242U2lYdTI0aVZKR1J3dkN2MTkzL055RzVmMGFxS0xML2xFeXhZNHpOMnZadkVUNU5lUDlTU0xuU0d3VTh6ajlJTEN2MGozcHNDc1VUOGhEQUZMb2VSN2dkUHV1UVI1SDhFTm1QR0M2SHRQek1udHVwZjV2cmpvdW5TVkNlcXBxNTVLUTVLcmQxbUJzL0dqcXF3ZzBwZWF5SmVtUXZHL0E5dW4wUDM0V1hWSThHSGd2SmN3TFpPNXY5NkJkNno0OGNPWEFyQnVqUXJaUWRjcE5SUXNyaWMvb2NwTG0rbklXZ0hKeFEyWUJzRnFNclY0WS0tRHMzZDFtcjNEKzBWTDhTWUtwVVRjQT09--7f95f7bded29d4ea1340c765bec95c793a17ace9; _ncg_sp_id.cc72=c8b8f168-bbc0-4797-b97c-384bcd5da00d.1548122553.5.1548231603.1548143865.7e020ece-e650-47b8-a75b-5cc6c9b51159; _4c_=fVLbctowEP2VjJ5j0P3CGyGdJm0JhCSlfWKEJYOLgz2ygZDAv3cF5DJtp36Qd1dnd492zwvazP0SdYjgmjJilJSanaOF39ao84LSKp7reKxCgTpo3jRV3Wm3N5tNK3hbNGVopeVjO9q%2Bbmzj7dLNy0dfJ7W3IZ23u87mIemVq2WznfQH6BylpfNQipiWalHwm2fwuMZgVqF0q7SZNNsqQjZ%2Bela7BVx8LstZ4a8vIZg5nOFMuMQJNU24TnWieaYS7w1jNNNSEg0Z3%2FM6B3aHlIQoQzGn3Oz6vevL%2B7sdBEh0%2BteXO6W5whiyJIM%2FJZJihqmiUjDNtVGGUcYwgLvd%2FrerJI5KUUEN3xFyjF68B8Vu9HVejZ71Isxo820gq9nqx7gSZbHopg%2FL%2FPbn8Mr2x%2BOZ%2B8Kenofj20f3C2%2BhDPC62iWCGwrMZCw8GN4PHu4PpQlV0vB6dzO4%2BRRbAutoxuHNg6%2FnZeEma1us4tC0gXA9Wedgv89hchgE%2BBe29ql9hMWiG3Cn6dqG3DZ5CSpAd6PhRW806qxJx%2Fl60ZRV3FdRNwEu1xEeyk3to9ebB1jzmSIQLUEsaJwvHVyCG3zmQzigIpW8ibQ%2BqOUUBJG9x%2BPy11EVDKyiTEFO4IE0YffdycOBPdHYSC45Zy0YiiKGEK7Q%2Fhw9HQXMAICZpBTG0oBateQ4foAIuTspGWWWWDwVTmdcS0UJMZ5IlWEq0sx64tCpnhAauhktpNgfyR3yCfuzH%2FlHv%2BOc%2FpNE%2Bd9JVfEKf0NTJjEDGuKEJvwNHRd8fBHmYioFyaS2GuvUeuG1YsSxjOM0Swn6UI5xzIR5bR65xGr7%2FW8%3D',
    # 333333333333333google refresh cookie(ctrl +f5)
    #   'cookie':'_ss=1366x768; threshold_value=89; clstr=v; clstr_tcv=54; split_tcv=60; __vst=fd0f0f5d-d57b-48c8-84f7-ee9332f86618; __gads=ID=c9c6bc68343b1c38:T=1547191429:S=ALNI_MbEoOR211jKBxjj3c6AxORc9rNejw; _gcl_au=1.1.462908694.1547191500; ajs_user_id=null; ajs_group_id=null; _ga=GA1.2.1809646443.1547191147; __qca=P0-1856484682-1547191544959; ajs_anonymous_id=%22db0f4b00-cb6b-4f3b-b074-13c91af6e735%22; _ncg_g_id_=4911c6ac-7925-4d04-8b99-bce40fcc0b74; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-179204249%7CMCIDTS%7C17919%7CMCMID%7C78470061863700216203027265384897932330%7CMCAAMLH-1548725294%7C11%7CMCAAMB-1548725295%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-549291961%7CMCOPTOUT-1548127694s%7CNONE%7CMCAID%7CNONE; _gid=GA1.2.1644294370.1548120496; _ncg_id_=1682b97e315-51c4ce99-0b7f-4994-8781-14746f45fe7f; __ssn=dae48bd1-8575-48ac-9d51-27bd07bacfca; __ssnstarttime=1548221607; userStatus=return_user; automation=false; split=n; bcc=false; bcvariation=SRPBCRR%3Av1%3Adesktop; header_slugs=gs%3DAdair-County_MO%26lo%3DAdair%26st%3Dcounty; ab_srp_viewtype=ab-list-view; criteria=loc%3DAdair+County%2C+MO%26locSlug%3DAdair-County_MO%26lat%3D40.190562%26long%3D-92.600719%26status%3D1%26pg%3D1%26pgsz%3D48%26sprefix%3D%2Frealestateandhomes-search%26city%3DAdair+County%26state_id%3DMO; srchID=be158ecc1301418f8a3b881bc47a8bc5; _ncg_sp_ses.cc72=*; _fbp=fb.1.1548229728818.1374132530; _ncg_sp_id.cc72=c8b8f168-bbc0-4797-b97c-384bcd5da00d.1548122553.5.1548232094.1548143865.7e020ece-e650-47b8-a75b-5cc6c9b51159; _4c_=fVLbctowEP2VjJ5j0P3CGyGdJm0IhCSlfWKEJYOLgz2ygZDAv3cF5DKTmfpB3l2d3T3aPa9oM%2FdL1CGCa8qo0pQqfI4WflujzitKq3iu47EKBeqgedNUdafd3mw2reBt0ZShlZZP7Wj7urGNt0s3L598ndTehnTe7jqbh6RXrpbNdtIfoHOUls5DKWJaqkXBb17A4xqDWYXSrdJm0myrCNn46VntFnDxvSxnhb%2B%2BhGDmcIYz4RIn1DThOtWJ5plKvDeM0UxLSTRk%2FMrrHNgdUhKiDMWccrPr964vH%2B53ECDR6V9f7pTmCmPIkgz%2BlEiKGaaKSsE010YZRhnDAO52%2BzdXSRyVooIaviPkGL34CIrd6Oe8Gr3oRZjR5mYgq9nq97gSZbHopo%2FL%2FO7P8Mr2x%2BOZ%2B8GeX4bjuyf3F2%2BhDPC62iWCGwrMZCw8GD4MHh8OpQlV0vB6dzu4%2FRZbAutoxuHNg6%2FnZeEma1us4tC0gXA9Wedgf8xhchgE%2BBe29ql9gsWiW3Cn6dqG3DZ5CSpA96PhRW806qxJx%2Fl60ZRV3FdRNwEu1xEeyk3to9ebB1jzmSIQLUEsaJwvHVyCG3zmQzigIpW8ibQ%2BqeUUBJF9xOPy11EVHKyiTEFO4IE0YffdyeOBPdHYSC45Zy0YiiKGEK7Q%2Fhw9HwXMiDaUUKNgLA2oVUuO4weIkLuTklFmicVT4XTGtVSUEOOJVBmmIs2sJw6d6gmhoZvRQor9kdwhn%2FAv%2FejXfsc5%2FS%2FJfE2qijf4O5oyiRnQECc04e%2FouODjizAXUylIJrXVWKfWC68VI45lHKdZStCncpxBc8Xfyuljtf3%2BHw%3D%3D; AWSALB=8zapR3ElTuM02bIyh6I5SMhghPZ+vTjgHsvOTbt6ZsYjHyulqv0r35NtC2WtWyIG4HFQU1PCP/iRI/9e9GYpf87hkUQ8IMwi1+idY23HYaWc6YnLubCTaUsSAfFBSgcHWZ4XfytuWocFpBHcAQixb/7yxNX99jfgo0bv0bTx5Q7N7qSNzdvSNrUNLNWvAQ==; _rdc-next_session=RCtTSVdUT21EcWZlK2pYLytyQUtKNnFrb0tMVmcvL05weE9YYnc5N1dmTlhwZGZHSGtCaTJzNFMvUHlobWxkQmo3QUJJOXZ5K0FtOURaQ0F4L212Ry8vN25mNlZBOExLWUlicEViVzYySEVuNit5aGx5MWlYMks3Zlc3OWZGZ3d1UzhjblZOOFlsOSsxQkx6bGxxbUtkUTZHbGdRRHlZd0hNUkE4RmQrVEJBR3lWb1NJeGtjd0ordmJxTzR1WkVYZWM3UDNTR245dlFUUlF6ZU5DQkVMa0J5MllidmEzR0RNTitNOXhQekUvVWtzT2U4NExIdWlvVlROa2tJL2x4ZC0tamlFNmRWeVdlU2hwb0YwM1dJMmp4QT09--280cee761b336b56f481763976fce262bdf32744',
    # 44444444444google refresh cookie
    #   'cookie':'_ss=1366x768; threshold_value=89; clstr=v; clstr_tcv=54; split_tcv=60; __vst=fd0f0f5d-d57b-48c8-84f7-ee9332f86618; __gads=ID=c9c6bc68343b1c38:T=1547191429:S=ALNI_MbEoOR211jKBxjj3c6AxORc9rNejw; _gcl_au=1.1.462908694.1547191500; ajs_user_id=null; ajs_group_id=null; _ga=GA1.2.1809646443.1547191147; __qca=P0-1856484682-1547191544959; ajs_anonymous_id=%22db0f4b00-cb6b-4f3b-b074-13c91af6e735%22; _ncg_g_id_=4911c6ac-7925-4d04-8b99-bce40fcc0b74; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-179204249%7CMCIDTS%7C17919%7CMCMID%7C78470061863700216203027265384897932330%7CMCAAMLH-1548725294%7C11%7CMCAAMB-1548725295%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-549291961%7CMCOPTOUT-1548127694s%7CNONE%7CMCAID%7CNONE; _gid=GA1.2.1644294370.1548120496; _ncg_id_=1682b97e315-51c4ce99-0b7f-4994-8781-14746f45fe7f; __ssn=dae48bd1-8575-48ac-9d51-27bd07bacfca; __ssnstarttime=1548221607; userStatus=return_user; automation=false; split=n; bcc=false; bcvariation=SRPBCRR%3Av1%3Adesktop; header_slugs=gs%3DAdair-County_MO%26lo%3DAdair%26st%3Dcounty; ab_srp_viewtype=ab-list-view; criteria=loc%3DAdair+County%2C+MO%26locSlug%3DAdair-County_MO%26lat%3D40.190562%26long%3D-92.600719%26status%3D1%26pg%3D1%26pgsz%3D48%26sprefix%3D%2Frealestateandhomes-search%26city%3DAdair+County%26state_id%3DMO; srchID=be158ecc1301418f8a3b881bc47a8bc5; _ncg_sp_ses.cc72=*; _fbp=fb.1.1548229728818.1374132530; AWSALB=cAlld6MMiqavjoY9yzNS15OPr7JDhwiQAvTDH3/XA2BPTWEWzy3qA5zZQcw6bRN0YSiyyEBPtfsFym4X/iEpc5HFygyBDOydB9EuUiaZG4ogXYaui8dOHUiiRtI43/nlOWsnXcWbqlPAbHIiq+MITA/Xb5PGHeQyF8HPTl4dD6Sjz5HlC85bj+ZfwGTItw==; _rdc-next_session=MVVlNDVUWkxVZ1FwNnRCUkJtUWd2bkkyYm9veGNJbk9QYWlMbUpoNjhuclA2dHFFTDhqcEdWNjNGYTduVjNmNE1sM1o5L3FrZEVkd0RaZmdsNEh4SzY1OFdLQnJJTnU3ZVB3TEVlY2RWcThrOXpqa2NlbEJUNGZVZXVZckdyMWx3S1BSOFQ5dDZnY0tGU1FYcnRXRUFPNzRVd2wxZVhaM21iSTA1ckNIUWRmc0U3UGYxaVFwbmhmKzVYbnh5R2hlczZDZ1FNbXNoZWR1S2wzL01ueGttU25WU1crd3praVZ4SzluMWpzck1TRndQME1NanAzN2xJTHl3UnpyYlo2dC0tMmtCUVZGeDU0QmxYYVVsRUVuV3NoUT09--a4a9aae3daee11ee62310b6937c334affc0fead1; _ncg_sp_id.cc72=c8b8f168-bbc0-4797-b97c-384bcd5da00d.1548122553.5.1548232805.1548143865.7e020ece-e650-47b8-a75b-5cc6c9b51159; _4c_=fVLbctowEP2VjJ5j0P3CGyGdJm0JhCSlfWKEJYOLgz22gJDAv3cF5DLNTP0g767O7h7tnhe0mfsl6hDBNWVUay4pPUcLv21Q5wWlVTzX8VjVBeqgeQhV02m3N5tNq%2Fa2CGXdSsvHdrR9E2zwdunm5aNvksbbOp23u87mddIrV8uwnfQH6BylpfNQipiWalHwwzN4XGMwq7p0qzRMwraKkI2fnjVuARdfy3JW%2BOtLCGYOZzgTLnFCTROuU51onqnEe8MYzbSUREPGz7zJgd0hJSHKUMwpN7t%2B7%2Fry%2Fm4HARKd%2FvXlTmmuMIYsyeBPiaSYYaqoFExzbZRhlDEM4G63%2F%2BMqiaNSVFDDd4QcoxfvQbEbfZ9Xo2e9qGc0%2FBjIarb6Na5EWSy66cMyv%2F09vLL98XjmvrGn5%2BH49tH9wVsoA7yudonghgIzGQsPhveDh%2FtDaUKVNLzZ3QxuvsSWwDqacXjz2jfzsnCTtS1WcWjaQLiZrHOw3%2BcwOQwC%2FAvb%2BNQ%2BwmLRDbjTdG3r3Ia8BBWgu9Hwojcaddak43yzCGUV91U0oYbLdYTX5abx0evNa1jzmSIQLUEsaJwvHVyCW%2FvM1%2FUBFankIdL6oJZTEET2Ho%2FLX0dVCLCKMgU5gQfShN13Jw8H9kRjI7nknLVgKIoYQrhC%2B3P0dBQwI7BlwQwIOARQq5Ycxw8Qde5OSkaZJRZPhdMZ11JRQownUmWYijSznjh0qieEhm5GCyn2R3KHfCL%2B7afl537HOf0nybDPSVXxCn9DUyYxAxrihCb8DR0XfHwR5mIqBcmkthrr1HrhtWLEsYzjNEsJ%2BlCOS2guXhnDRA%2FV9vu%2F',
    # 555555555从浏览器中最新获取的cookie(firefox)
    #   'cookie':'AWSALB=6c/bCHICjll9XRsfQba5BusNCTi+3LWg9ww+SEprVXCuYTLvFMbpFEHxe6Og4HS7n0AWeI8uW6oH/DcO3jspazymOXuc9KgoHDObWMgr2/dfXenXz9Qg0FJPevSfoEGn5hw8CwGKHS0dmSvy99Zq2aLLn93a49hTKmGTBd9iqUG0PDZv8bQnTDtHzjqW2Q==; split=n; split_tcv=43; __vst=ddb03ec7-0d5e-41d8-ba0c-717d6048eff4; __ssn=27ee51e2-3eec-4d59-a88b-7071382a4423; __ssnstarttime=1548230827; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-179204249%7CMCIDTS%7C17920%7CMCMID%7C36629776097100914963441128513761121993%7CMCAAMLH-1548835642%7C3%7CMCAAMB-1548835644%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-549291961%7CMCOPTOUT-1548238042s%7CNONE%7CMCAID%7CNONE; AMCVS_8853394255142B6A0A4C98A4%40AdobeOrg=1; __gads=ID=73daf541abb16fb7:T=1548230837:S=ALNI_MaD_q6jlVRwOwWYIpx0mPpcLda2Jw; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%2269e86961-976f-4540-9c0c-c8cfaa34ac4f%22; cto_lwid=2db5e9b4-f01d-45a6-a8fa-3887acdebb3a; threshold_value=8; automation=false; clstr=v; clstr_tcv=41; bcc=false; bcvariation=SRPBCRR%3Av1%3Adesktop; _rdc-next_session=RHBIbEgvR3grZkFZVnM4NGlLQ1F1aXgzQUFVNVJiWjBiY3ZpWWpjby80TkNMUW15SG9wZ2tKWjRMT0d6T1puYzdML09ZQ3hwYlRzM1lPMG5IWFJLZVdlaDkwY08zVjl5KytrTU0rZ21hQXBuVnkwWEZxU3lNWjlKMUZhM3I1NW9PZzNwOVl3N2VhRWpxR3I5Z2U4bGdBPT0tLTVuamVERjExQnJjY2pSbnAzRSthQ0E9PQ%3D%3D--36fd91fbac1c61afdd317b78b5863e85c7f2c662; _gcl_au=1.1.1253675130.1548230846; _fbp=fb.1.1548230846151.759104185; _ga=GA1.2.856881187.1548230839; _gid=GA1.2.71977508.1548230846; nativeAiInstallationId=fcd32f61-9fca-4e04-8a73-74a202dfe50e; _4c_=fVJNU9swFPwrjM44SLI%2BcwvQFlpCQoCmPWVsSUncGOSxHSeA%2Be88JYZ0ykx98Oit9kmrffuCNkv3iPqEM0VjQqgknB%2BjlXuqUP8FmSL8m%2FBblznqo2VdF1X%2F5GSz2fRKl%2BS1L3vGP5ygY2S8dcAguid7FOr6GSqmMCyL0tu1qWf1UxEoG5ceVXYFG9%2B8X%2BTu8hxAa1McOyMjbLmLGLEqShNsIkmkFZgpN58z6PiZVRlcumuJiNQUM8p0Ozy7PL%2B7bXcAFMPL8zYWgmopBdaSYKwJ0yJmDJ6oOImlgAXROgbyYDC8uoiCAyrmgtG2A08PGGsnP5bF5FmtygWtr0aiWKx%2FTQvu89XA3D9mN7%2FHF8lwOl3Y7%2FH2eTy9ebB%2F8BMcA7Iu2ogzTTXRggAyGt%2BN7u%2BiveEK1Fft9ej6S7gSRIdl8G5ZumrpcztrknwdPFOAVrMmg%2BXBhdnOBqhPk8qZ5AGmha6hTE2TlFlSZx5Gi24n49OzyaTfkL511ar2RZhWXtUlbDaBXvpN5UL1NSvd3G%2BPRAywhwigafZoYRdK2HFluaMFLVkdZP2VgQ6E6BzwMHtIDwp5yL1J8tADeYPJD2b3O%2FWKC6UIUbK3twSrWKPXY7TdhzImklOGiQRTakigEgyHDxhlZrt0IpqkDsY751Q5myaMC6LBXMmdSxh1GnXncYGxUIzHisIBwc19v9RSG2KNMFYagS2FqKTJHM%2BN4kpziT700JhCxDTGnR6i3uUUeXcaOZAZpxwTQd7J7EN80XRs%2Bump9PNT9xP6T4%2F6t%2Bf19Q0%3D; _parsely_visitor={%22id%22:%22c996cc59-19ae-40b2-83c0-88076164ef49%22%2C%22session_count%22:1%2C%22last_session_ts%22:1548230857514}; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.realtor.com/news/celebrity-real-estate/malibu-mansion-125m/%22%2C%22sref%22:%22%22%2C%22sts%22:1548230857514%2C%22slts%22:0}; _ncg_sp_ses.cc72=*; _ncg_sp_id.cc72=7e167b4f-67ed-4ac8-acdf-53a2a092e94b.1548230859.1.1548230863.1548230859.3acb9a34-6521-42df-b227-3c97471b3f6b; _ncg_id_=7e167b4f-67ed-4ac8-acdf-53a2a092e94b; userStatus=new_user; nativeAiSession=1548232364428|MWVmYjRiNjAtZjk2Ny00NzdkLTkzNTItMTM4ZjEyMjY0NDE1fA==; vidoraUserId=92dceusuihvvm34ao7c9mu0m4l1222'
    # google
}

signal = 1
while(signal):
    res = requests.get(url='https://www.realtor.com/realestateandhomes-search/Adair-County_MO',headers=realtor_cookies,verify=False,allow_redirects=False)
    print('status_code',res.status_code)
    print('signal',signal)
    if res.status_code==302:
        signal +=1
        if signal==10:
            break

    # else:
    #     print(res.status_code)
    #     print(signal)
    #     break



# res = requests.get(
#                     # url='https://www.realtor.com/realestateandhomes-search/Adair-County_MO',
#                    url = 'https://www.realtor.com/realestateandhomes-detail/807-W-Hamilton-St_Kirksville_MO_63501_M86027-79545?view=qv',
#                    headers=realtor_cookies,
#                    verify=False)
# print(res.text)
#
# with open('./realtor_test.html','w',encoding='utf-8') as f:
#     f.write(res.text)


