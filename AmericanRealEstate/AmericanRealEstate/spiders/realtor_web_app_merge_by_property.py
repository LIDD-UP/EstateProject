# -*- coding: utf-8 -*-
import re
import datetime

import scrapy
from urllib.parse import urljoin
from scrapy_redis.spiders import RedisSpider
import pandas as pd
import ast

from AmericanRealEstate.items import RealtorHouseInfoJsonItem, RealtorDetailDomItem,RealtorDetailPageJsonItem
# from AmericanRealEstate.settings import realtor_search_criteria, realtor_domain_url




class RealtorWebAppMergeByPropertySpider(scrapy.Spider):
    name = 'realtor_web_app_merge_by_property'
    allowed_domains = ['mapi-ng.rdc.moveaws.com']
    # start_urls = [x for x in realtor_search_criteria]

    def __init__(self,
                 start_urls=None,
                 # user_agent_list=None,
                 scrapy_start_time=None,
                 *args, **kwargs):
        super(RealtorWebAppMergeByPropertySpider, self).__init__(*args, **kwargs)
        # print(start_urls)
        # 传入start_request_list
        start_urls_list = None
        if start_urls is not None:
            start_urls_list = start_urls.split(',')
            print(len(start_urls_list))
        self.start_urls = start_urls_list
        #
        # # 传入user_agent_list
        #
        # true_user_agent_list = None
        # print('用户代理',user_agent_list)
        # if user_agent_list is not None:
        #     true_user_agent_list = user_agent_list.split('|')
        # # print(self.user_agent_list)
        # true_user_agent_list_middle = true_user_agent_list
        #
        # with open('./invalidation_user_agent_file.txt', 'r') as f:
        #     for user_agent in true_user_agent_list_middle:
        #         if user_agent in f.readlines():
        #             true_user_agent_list.remove(user_agent)
        # self.user_agent_list = true_user_agent_list

        true_scrapy_start_time = None
        if scrapy_start_time is not None:
            true_scrapy_start_time = datetime.datetime.strptime(scrapy_start_time,'%Y-%m-%d %H:%M:%S')
        self.scrapy_start_time = true_scrapy_start_time

    custom_settings = {
        "ITEM_PIPELINES": {
            'AmericanRealEstate.pipelines.RealtordetailPagePsqlPipeline': 301,
            # 'AmericanRealEstate.pipelines.RealtordetailPageMysqlPipeline':302
            # 'AmericanRealEstate.pipelines.RealtorDetailDomPipeline': 302,
            # 'AmericanRealEstate.pipelines.RealtorHouseInfoTestPipeline': 302,
            # 'scrapy_redis.pipelines.RedisPipeline': 300

        },
        "DOWNLOADER_MIDDLEWARES":{
        # 'AmericanRealEstate.middlewares.AmericanrealestateDownloaderMiddleware': 543,
        #  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
         # 'AmericanRealEstate.middlewares.RandomUserAgentMiddleware': 543,
         #    'AmericanRealEstate.middlewares.TestGetSpiderAttrMiddleware':1,
            # 'AmericanRealEstate.middlewares.Process302Middleware' :544,
            # 'AmericanRealEstate.middlewares.AlertUserAgentWhenEncounter302Middleware': 545,
            'AmericanRealEstate.middlewares.RealtorDetailPageAMiddleware': 545,

    },

        "DEFAULT_REQUEST_HEADERS": {
                "Cache-Control": "public",
                "Mapi-Bucket": "for_sale_v2:on,for_rent_ldp_v2:on,for_rent_srp_v2:on,recently_sold_ldp_v2:on,recently_sold_srp_v2:on,not_for_sale_ldp_v2:on,not_for_sale_srp_v2:on,search_reranking_srch_rerank1:variant1",
                "Host": "mapi-ng.rdc.moveaws.com",
                "Connection": "Keep-Alive",
                "Accept-Encoding": "gzip",
                "User-Agent": "okhttp/3.10.0",
                # 'authority': 'www.realtor.com',
                # 'method': 'GET',
                # # 'path':'/sitemap/Alabama-real-estate/',
                # 'scheme': 'https',
                # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,',
                # 'accept-encoding': 'gzip, deflate, br',
                # 'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
                # # 'accept-language': 'en-US,en;q=0.5',
                # 'cache-control': 'no-cache',
                # 'upgrade-insecure-requests': '1',
                # 'cookie': '_ss=1366x768; threshold_value=89; clstr=v; clstr_tcv=54; split_tcv=60; __vst=fd0f0f5d-d57b-48c8-84f7-ee9332f86618; __gads=ID=c9c6bc68343b1c38:T=1547191429:S=ALNI_MbEoOR211jKBxjj3c6AxORc9rNejw; _gcl_au=1.1.462908694.1547191500; ajs_user_id=null; ajs_group_id=null; _ga=GA1.2.1809646443.1547191147; __qca=P0-1856484682-1547191544959; ajs_anonymous_id=%22db0f4b00-cb6b-4f3b-b074-13c91af6e735%22; _ncg_g_id_=4911c6ac-7925-4d04-8b99-bce40fcc0b74; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-179204249%7CMCIDTS%7C17919%7CMCMID%7C78470061863700216203027265384897932330%7CMCAAMLH-1548725294%7C11%7CMCAAMB-1548725295%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-549291961%7CMCOPTOUT-1548127694s%7CNONE%7CMCAID%7CNONE; _gid=GA1.2.1644294370.1548120496; _ncg_id_=1682b97e315-51c4ce99-0b7f-4994-8781-14746f45fe7f; __ssn=dae48bd1-8575-48ac-9d51-27bd07bacfca; __ssnstarttime=1548221607; userStatus=return_user; automation=false; split=n; bcc=false; bcvariation=SRPBCRR%3Av1%3Adesktop; header_slugs=gs%3DAdair-County_MO%26lo%3DAdair%26st%3Dcounty; ab_srp_viewtype=ab-list-view; criteria=loc%3DAdair+County%2C+MO%26locSlug%3DAdair-County_MO%26lat%3D40.190562%26long%3D-92.600719%26status%3D1%26pg%3D1%26pgsz%3D48%26sprefix%3D%2Frealestateandhomes-search%26city%3DAdair+County%26state_id%3DMO; srchID=be158ecc1301418f8a3b881bc47a8bc5; _ncg_sp_ses.cc72=*; _fbp=fb.1.1548229728818.1374132530; AWSALB=/bTmyIu5nlvbnACPmfjR1nAT2QtPGZjWun45It7FAVGsHuftFBvIWLc+38t9pAsLy2yUqUXMNpha1iMQGBv+ATeWIch7JhWPNybKy8LzVYGMFSQiF6Z8kJfP3hHV3m40228anyBezHl3NwQiHhK4s/nNH5zibgotk1hn86s0opoCavwjXQTIiP5doylcUQ==; _rdc-next_session=dDNod0Nvd1ZDdEZDV0xQV242U2lYdTI0aVZKR1J3dkN2MTkzL055RzVmMGFxS0xML2xFeXhZNHpOMnZadkVUNU5lUDlTU0xuU0d3VTh6ajlJTEN2MGozcHNDc1VUOGhEQUZMb2VSN2dkUHV1UVI1SDhFTm1QR0M2SHRQek1udHVwZjV2cmpvdW5TVkNlcXBxNTVLUTVLcmQxbUJzL0dqcXF3ZzBwZWF5SmVtUXZHL0E5dW4wUDM0V1hWSThHSGd2SmN3TFpPNXY5NkJkNno0OGNPWEFyQnVqUXJaUWRjcE5SUXNyaWMvb2NwTG0rbklXZ0hKeFEyWUJzRnFNclY0WS0tRHMzZDFtcjNEKzBWTDhTWUtwVVRjQT09--7f95f7bded29d4ea1340c765bec95c793a17ace9; _ncg_sp_id.cc72=c8b8f168-bbc0-4797-b97c-384bcd5da00d.1548122553.5.1548231603.1548143865.7e020ece-e650-47b8-a75b-5cc6c9b51159; _4c_=fVLbctowEP2VjJ5j0P3CGyGdJm0JhCSlfWKEJYOLgz2ygZDAv3cF5DJtp36Qd1dnd492zwvazP0SdYjgmjJilJSanaOF39ao84LSKp7reKxCgTpo3jRV3Wm3N5tNK3hbNGVopeVjO9q%2Bbmzj7dLNy0dfJ7W3IZ23u87mIemVq2WznfQH6BylpfNQipiWalHwm2fwuMZgVqF0q7SZNNsqQjZ%2Bela7BVx8LstZ4a8vIZg5nOFMuMQJNU24TnWieaYS7w1jNNNSEg0Z3%2FM6B3aHlIQoQzGn3Oz6vevL%2B7sdBEh0%2BteXO6W5whiyJIM%2FJZJihqmiUjDNtVGGUcYwgLvd%2FrerJI5KUUEN3xFyjF68B8Vu9HVejZ71Isxo820gq9nqx7gSZbHopg%2FL%2FPbn8Mr2x%2BOZ%2B8Kenofj20f3C2%2BhDPC62iWCGwrMZCw8GN4PHu4PpQlV0vB6dzO4%2BRRbAutoxuHNg6%2FnZeEma1us4tC0gXA9Wedgv89hchgE%2BBe29ql9hMWiG3Cn6dqG3DZ5CSpAd6PhRW806qxJx%2Fl60ZRV3FdRNwEu1xEeyk3to9ebB1jzmSIQLUEsaJwvHVyCG3zmQzigIpW8ibQ%2BqOUUBJG9x%2BPy11EVDKyiTEFO4IE0YffdycOBPdHYSC45Zy0YiiKGEK7Q%2Fhw9HQXMAICZpBTG0oBateQ4foAIuTspGWWWWDwVTmdcS0UJMZ5IlWEq0sx64tCpnhAauhktpNgfyR3yCfuzH%2FlHv%2BOc%2FpNE%2Bd9JVfEKf0NTJjEDGuKEJvwNHRd8fBHmYioFyaS2GuvUeuG1YsSxjOM0Swn6UI5xzIR5bR65xGr7%2FW8%3D',
                # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                # 'user-agent':'Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50',
                # 'user-agent': 'Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50',
                # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0',
                # 'User-Agent': start_user_agent,
                # 'referer': 'www.realtor.com',
        },
        "COOKIES_ENABLED": False,
        "REDIRECT_ENABLED": False,
        "CONCURRENT_REQUESTS" :16,
        "REFERER_ENABLED": False,
        "RETRY_ENABLED": False,
        "REACTOR_THREADPOOL_MAXSIZE":100,
        "CONCURRENT_REQUESTS_PER_DOMAIN" : 10,
        # "CONCURRENT_REQUESTS_PER_IP" : 100,

        # "RETRY_HTTP_CODES": [500, 502, 503, 504, 400, 408]

        # "LOG_FILE": "realtor_log.txt",
        # "LOG_LEVEL": 'INFO',
        # 'REDIS_HOST': '192.144.149.43',
        # 'REDIS_PORT': 6379,
        #
        # # 指定 redis链接密码，和使用哪一个数据库
        # 'REDIS_PARAMS': {
        #     'password': '123456',
        # },
        # redis 设置：
        # Enables scheduling storing requests queue in redis.
        # "SCHEDULER": "scrapy_redis.scheduler.Scheduler",
        #
        # # Ensure all spiders share same duplicates filter through redis.
        # "DUPEFILTER_CLASS": "scrapy_redis.dupefilter.RFPDupeFilter",

    }

    def parse(self,response):
        # 接口的parse
        realtor_detail_pageJson_item = RealtorDetailPageJsonItem()
        realtor_detail_pageJson_item['detailJson'] = response.text
        realtor_detail_pageJson_item['propertyId'] = re.findall(r'api/v1/properties/(\d.*)\?client_id=',response.url)[0]
        yield realtor_detail_pageJson_item


