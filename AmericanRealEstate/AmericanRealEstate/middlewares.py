# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import time
import datetime
import re
from scrapy import signals
from fake_useragent import UserAgent
from scrapy import Request
from AmericanRealEstate.settings import realtor_user_agent_list, trulia_cookies_list
from crawl_tools import get_psql_con
from crawl_tools.get_sql_con import get_sql_con




class AmericanrealestateSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)

        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s', spider.name)






class AmericanrealestateDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


# 设置自动切换user-gent
class RandomUserAgentMiddleware(object):
    # 随机替换usergent
    def __init__(self,crawler):
        super(RandomUserAgentMiddleware,self).__init__()
        # self.user_agent_list = crawler.settings.get("user_agent_list")
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE","random")

    @classmethod
    def from_crawler(cls,crawler):
        # 将它传递给self
        return cls(crawler)

    def process_request(self,request,spider):
        # 配置settings获取ua的属性值；
        def get_ua():
            return getattr(self.ua,self.ua_type)
        random_agent = get_ua()
        print(random_agent)
        request.headers.setdefault('user-agent',random_agent)




# 设置headers的middleware
class HeadersMiddleware(object):
    def __init__(self,crawler):
        super(HeadersMiddleware,self).__init__()
        self.my_headers = crawler.settings.get("DEFAULT_REQUEST_HEADERS")

    @classmethod
    def from_crawler(cls,crawler):
        # 将它传递给self
        return cls(crawler)

    def process_request(self,request,spider):
        request.headers.setdefault('headers',self.my_headers)


# realtor处理302 重定向问题,对于外部写脚本;(考虑到之前有浏览器被封了)(利用user-agent)user-agent是随机获取的)
class Process302Middleware(object):
    def __init__(self):
        # super(Process302Middleware,self).__init__()
        self.stop_signal = 1

    def process_response(self, request, response, spider):
        print(response.status)
        if response.status == 302:
            self.stop_signal += 1
            print(self.stop_signal)
            if self.stop_signal > 10:
                spider.crawler.engine.close_spider(spider, '遇到302错误大于50次,爬虫已经被服务器发现')
            return request
        return response


# realtor,当一个user-agent被封之后进行替换user-agent,这种就不需要启用随机的user-agent了
class AlertUserAgentWhenEncounter302Middleware(object):
    def __init__(self):
        super(AlertUserAgentWhenEncounter302Middleware,self).__init__()
        self.stop_signal = 1
        self.user_agent_index = 0

    def proces_request(self,request,spider):
        print(request.meata['302error'])
        if request.meta['302error']:
            print('接受302 meta信息,更换user-agent')
            request.headers.setdefault('User-Agent', realtor_user_agent_list[self.user_agent_index])
            self.user_agent_index += 1

    def process_response(self, request, response, spider):
        print(response.status)

        if response.status == 302:
            print('被发现了,更换user-agent')
            import time
            time.sleep(1)
            self.stop_signal += 1
            print(self.stop_signal)

            if self.stop_signal > 50:
                spider.crawler.engine.close_spider(spider, '更换了1000次user-agent了,爬虫已经被发现了')
                # # 停止爬虫
                # # 定义一个其实时间变量 a
                # # a = time.time
                # # while (b:time.time-a>10)
                # # 开启爬虫;
                # spider.crawler.engine.pause()
                # while
            if self.user_agent_index > 120:
                self.user_agent_index =0
            print(realtor_user_agent_list[self.user_agent_index])
            # request.headers.setdefault('User-Agent',realtor_user_agent_list[self.user_agent_index])
            request.headers.setdefault('User-Agent', 'fjdalfjdlajfdlajf')
            request.headers['user-agent'] = 'yuanshide '
            # 这个只能在process_request 中才能起作用
            # request.headers = "{'user-agent': realtor_user_agent_list[self.user_agent_index]}"
            # request.headers={b'Authority': [b'www.realtor.com'], b'Method': [b'GET'], b'Scheme': [b'https'], b'Accept': [b'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'], b'Accept-Encoding': [b'gzip, deflate, br'], b'Accept-Language': [b'zh-CN,zh;q=0.9,ja;q=0.8'], b'Cache-Control': [b'no-cache'], b'Upgrade - Insecure - Requests': [b'1'], b'Referer': [b'www.realtor.com'],b'UserAgent':['xxxxxxxxlajfdakjsf']}
            # request.headers['User-Agent'] = 'hdalhfdlahfdlah'
            # request.meta['User-Agent'] = 'xxxxxxxxxxxxxxjflajflafxxxxxxxxxxxx'
            # new_request = request.copy()
            # new_request.meta['302error'] = 'yes'
            # new_request.headers['cookie'] = '12345678cookie'
            # new_request.headers.setdefault('User-Agent','hahahhahahahha')
            # new_request.headers['user-agent'] = realtor_user_agent_list[self.user_agent_index]
            self.user_agent_index += 1
            return request
        return response





class NewAlertUserAgentWhenEncounter302Middleware(object):
    def __init__(self):
        super(NewAlertUserAgentWhenEncounter302Middleware,self).__init__()
        self.stop_signal = 1
        self.user_agent_index = 0
        self.change_user_agent = False
        self.is_first_get_user_agent = True

    def process_request(self,request,spider):
        # 第一次随机获取一个列表中的user-agent
        if self.is_first_get_user_agent:
            random_index = random.randint(0, len(realtor_user_agent_list))
            request.headers.setdefault('User-Agent', realtor_user_agent_list[random_index])
            self.is_first_get_user_agent = False

        if self.change_user_agent:
            random_index = random.randint(0, len(realtor_user_agent_list))
            request.headers.setdefault('User-Agent', realtor_user_agent_list[random_index])
            self.change_user_agent = False

    def process_response(self, request, response, spider):
        print(response.status)
        if response.status == 302:
            print('被发现了,更换user-agent')
            # 设置暂停时间
            import time
            time.sleep(1)
            self.stop_signal += 1
            print(self.stop_signal)
            #
            if self.stop_signal > 50:
                spider.crawler.engine.close_spider(spider, '更换了1000次user-agent了,爬虫已经被发现了')


            # 去掉该user-agent,同时将change_user_agent置为True
            print(request.headeres['user-agent'])
            realtor_user_agent_list.remove(request.headers['user-agent'])
            self.change_user_agent = True
            return request
        return response


# 被发现之后换一个固定得user-agent

class AlterUserAgentWhenEncounter302Middleware(object):
    def __init__(self):
        super(AlterUserAgentWhenEncounter302Middleware,self).__init__()
        self.stop_signal = 1
        self.user_agent_index = 0

    def process_request(self,request,spider):
        # 第一次从一个列表中的顺序取一个user-agent
        request.headers.setdefault('User-Agent', realtor_user_agent_list[self.user_agent_index])

    def process_response(self, request, response, spider):
        print(response.status)
        if response.status == 302:

            print('被发现了,更换user-agent')
            # 设置暂停时间
            import time
            time.sleep(60)
            self.stop_signal += 1
            print(self.stop_signal)
            #
            if self.stop_signal > 50:
                spider.crawler.engine.close_spider(spider, '更换了60次user-agent了,爬虫已经被发现了')

            # 去掉该user-agent,同时将change_user_agent置为True
            print(request.headeres['user-agent'])
            realtor_user_agent_list.remove(request.headers['user-agent'])
            request.headers['User-Agent'] = spider.user_agent_list[self.user_agent_index]

            return request
        return response


# 将爬取过的url 和爬取失败的url 以及未爬取的url进行分开，还有user-agent
class SaveCrawledAndNotCrawledUrlMiddleware(object):
    def __init__(self):
        super(SaveCrawledAndNotCrawledUrlMiddleware,self).__init__()
        self.stop_signal = 1
        self.user_agent_index = 0

    def process_request(self,request,spider):
        pass

    def process_response(self, request, response, spider):
        print(response.status)

        if response.status == 200:
            with open('./success_crawled_url.txt', 'a+') as f:
                f.write(response.url + '\n')

        if response.status == 302:
            with open('./failed_url.txt', 'a+') as f:
                f.write(response.url + '\n')

            with open('./failed_user_agent.txt', 'a+') as f:
                f.write(request.headeres['user-agent'] + '\n')

            print('被发现了,更换user-agent')
            # 设置暂停时间
            import time
            time.sleep(60)
            self.stop_signal += 1
            print(self.stop_signal)
            #
            if self.stop_signal > 50:
                spider.crawler.engine.close_spider(spider, '更换了60次user-agent了,爬虫已经被发现了')

            # 去掉该user-agent,同时将change_user_agent置为True
            print(request.headeres['user-agent'])
            realtor_user_agent_list.remove(request.headers['user-agent'])
            request.headers['User-Agent'] = spider.user_agent_list[self.user_agent_index]

            return request
        return response




class Process302MetaMiddleware(object):
    def process_request(self,request,spider):
        print(request.meta)
        print(type(request.meta))

        if '302error' in request.meta.keys():
            print(request.meta['302error'])
            print('接受302 meta信息,更换user-agent')
            request.headers['User-Agent'] = 'my user agent hahaha'
            request.headers.setdefault('user-agent','defualt-user-agent')
            print('.......')


# 测试获取spider中的一些参数:从spider中更换user-agent参数;
class TestGetSpiderAttrMiddleware(object):

    def process_request(self, request, spider):
        # # 随机停顿
        random_seed = [0,1]
        from random import choice
        a = choice(random_seed)
        print('a:-----------------',a)
        if a == 1:
            time.sleep(3)

        # 爬虫爬取3个小时后停止31分钟
        spider_scrapy_start_time = spider.scrapy_start_time
        if spider_scrapy_start_time is not None:
            scrapy_time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            true_scrapy_time_now = datetime.datetime.strptime(scrapy_time_now, '%Y-%m-%d %H:%M:%S')
            time_seconds_subtract = true_scrapy_time_now-spider_scrapy_start_time
            time_hour_subtract = int(time_seconds_subtract/3600)
            print('时间间隔：',time_hour_subtract)
            if time_hour_subtract%3 ==0:
                time.sleep(1890)

        # 判断当前的url是不是网页url：如果是就设置：
        if len(re.findall(r'realestateandhomes-search',request.url)) > 0:
            realtor_web_headers = {
                'authority': 'www.realtor.com',
                'method': 'GET',
                # 'path':'/sitemap/Alabama-real-estate/',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
                # 'accept-language': 'en-US,en;q=0.5',
                'cache-control': 'no-cache',
                'upgrade-insecure-requests': '1',
                # 'cookie': '_ss=1366x768; threshold_value=89; clstr=v; clstr_tcv=54; split_tcv=60; __vst=fd0f0f5d-d57b-48c8-84f7-ee9332f86618; __gads=ID=c9c6bc68343b1c38:T=1547191429:S=ALNI_MbEoOR211jKBxjj3c6AxORc9rNejw; _gcl_au=1.1.462908694.1547191500; ajs_user_id=null; ajs_group_id=null; _ga=GA1.2.1809646443.1547191147; __qca=P0-1856484682-1547191544959; ajs_anonymous_id=%22db0f4b00-cb6b-4f3b-b074-13c91af6e735%22; _ncg_g_id_=4911c6ac-7925-4d04-8b99-bce40fcc0b74; AMCV_8853394255142B6A0A4C98A4%40AdobeOrg=-179204249%7CMCIDTS%7C17919%7CMCMID%7C78470061863700216203027265384897932330%7CMCAAMLH-1548725294%7C11%7CMCAAMB-1548725295%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C-549291961%7CMCOPTOUT-1548127694s%7CNONE%7CMCAID%7CNONE; _gid=GA1.2.1644294370.1548120496; _ncg_id_=1682b97e315-51c4ce99-0b7f-4994-8781-14746f45fe7f; __ssn=dae48bd1-8575-48ac-9d51-27bd07bacfca; __ssnstarttime=1548221607; userStatus=return_user; automation=false; split=n; bcc=false; bcvariation=SRPBCRR%3Av1%3Adesktop; header_slugs=gs%3DAdair-County_MO%26lo%3DAdair%26st%3Dcounty; ab_srp_viewtype=ab-list-view; criteria=loc%3DAdair+County%2C+MO%26locSlug%3DAdair-County_MO%26lat%3D40.190562%26long%3D-92.600719%26status%3D1%26pg%3D1%26pgsz%3D48%26sprefix%3D%2Frealestateandhomes-search%26city%3DAdair+County%26state_id%3DMO; srchID=be158ecc1301418f8a3b881bc47a8bc5; _ncg_sp_ses.cc72=*; _fbp=fb.1.1548229728818.1374132530; AWSALB=/bTmyIu5nlvbnACPmfjR1nAT2QtPGZjWun45It7FAVGsHuftFBvIWLc+38t9pAsLy2yUqUXMNpha1iMQGBv+ATeWIch7JhWPNybKy8LzVYGMFSQiF6Z8kJfP3hHV3m40228anyBezHl3NwQiHhK4s/nNH5zibgotk1hn86s0opoCavwjXQTIiP5doylcUQ==; _rdc-next_session=dDNod0Nvd1ZDdEZDV0xQV242U2lYdTI0aVZKR1J3dkN2MTkzL055RzVmMGFxS0xML2xFeXhZNHpOMnZadkVUNU5lUDlTU0xuU0d3VTh6ajlJTEN2MGozcHNDc1VUOGhEQUZMb2VSN2dkUHV1UVI1SDhFTm1QR0M2SHRQek1udHVwZjV2cmpvdW5TVkNlcXBxNTVLUTVLcmQxbUJzL0dqcXF3ZzBwZWF5SmVtUXZHL0E5dW4wUDM0V1hWSThHSGd2SmN3TFpPNXY5NkJkNno0OGNPWEFyQnVqUXJaUWRjcE5SUXNyaWMvb2NwTG0rbklXZ0hKeFEyWUJzRnFNclY0WS0tRHMzZDFtcjNEKzBWTDhTWUtwVVRjQT09--7f95f7bded29d4ea1340c765bec95c793a17ace9; _ncg_sp_id.cc72=c8b8f168-bbc0-4797-b97c-384bcd5da00d.1548122553.5.1548231603.1548143865.7e020ece-e650-47b8-a75b-5cc6c9b51159; _4c_=fVLbctowEP2VjJ5j0P3CGyGdJm0JhCSlfWKEJYOLgz2ygZDAv3cF5DJtp36Qd1dnd492zwvazP0SdYjgmjJilJSanaOF39ao84LSKp7reKxCgTpo3jRV3Wm3N5tNK3hbNGVopeVjO9q%2Bbmzj7dLNy0dfJ7W3IZ23u87mIemVq2WznfQH6BylpfNQipiWalHwm2fwuMZgVqF0q7SZNNsqQjZ%2Bela7BVx8LstZ4a8vIZg5nOFMuMQJNU24TnWieaYS7w1jNNNSEg0Z3%2FM6B3aHlIQoQzGn3Oz6vevL%2B7sdBEh0%2BteXO6W5whiyJIM%2FJZJihqmiUjDNtVGGUcYwgLvd%2FrerJI5KUUEN3xFyjF68B8Vu9HVejZ71Isxo820gq9nqx7gSZbHopg%2FL%2FPbn8Mr2x%2BOZ%2B8Kenofj20f3C2%2BhDPC62iWCGwrMZCw8GN4PHu4PpQlV0vB6dzO4%2BRRbAutoxuHNg6%2FnZeEma1us4tC0gXA9Wedgv89hchgE%2BBe29ql9hMWiG3Cn6dqG3DZ5CSpAd6PhRW806qxJx%2Fl60ZRV3FdRNwEu1xEeyk3to9ebB1jzmSIQLUEsaJwvHVyCG3zmQzigIpW8ibQ%2BqOUUBJG9x%2BPy11EVDKyiTEFO4IE0YffdycOBPdHYSC45Zy0YiiKGEK7Q%2Fhw9HQXMAICZpBTG0oBateQ4foAIuTspGWWWWDwVTmdcS0UJMZ5IlWEq0sx64tCpnhAauhktpNgfyR3yCfuzH%2FlHv%2BOc%2FpNE%2Bd9JVfEKf0NTJjEDGuKEJvwNHRd8fBHmYioFyaS2GuvUeuG1YsSxjOM0Swn6UI5xzIR5bR65xGr7%2FW8%3D',
                # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
                # 'user-agent':'Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50',
                # 'user-agent': 'Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50',
                # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0',
                # 'User-Agent': start_user_agent,
                # 'referer': 'www.realtor.com',
            }
            for k, v in realtor_web_headers.items():
                request.headers.setdefault(k, v)

            random_seed = [0, 1]
            from random import choice
            a = choice(random_seed)
            print('a:-----------------', a)
            if a == 1:
                time.sleep(10)

        if len(re.findall(r'/api/v1/', request.url)) > 0:
            realtor_web_headers = {
            "Cache-Control": "public",
            "Mapi-Bucket": "for_sale_v2:on,for_rent_ldp_v2:on,for_rent_srp_v2:on,recently_sold_ldp_v2:on,recently_sold_srp_v2:on,not_for_sale_ldp_v2:on,not_for_sale_srp_v2:on,search_reranking_srch_rerank1:variant1",
            "Host": "mapi-ng.rdc.moveaws.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.10.0",
        }
            for k, v in realtor_web_headers.items():
                request.headers.setdefault(k, v)



        if getattr(spider, 'user_agent_list', None) is not None :
            print(spider.user_agent_list)
            spider_user_agent_list = spider.user_agent_list
            print(len(spider_user_agent_list))
            if len(spider_user_agent_list) != 0:
                # 每次固定取第零个
                # 每次随机获取一个：
                print('设置的user-agent',spider_user_agent_list[0])
                request.headers.setdefault('User-Agent',spider_user_agent_list[0])

                agent_random_seed = [0, 1,2,3,4,5,6,7,8,9]
                from random import choice
                a = choice(agent_random_seed)
                if a == 1:
                    user_agent_random_index = choice(
                        [random_seed for random_seed in range(len(spider_user_agent_list))])
                    print('设置的user-agent', spider_user_agent_list[user_agent_random_index])
                    request.headers.setdefault('User-Agent', spider_user_agent_list[user_agent_random_index])

                # request.headers.setdefault('User-Agent', spider_user_agent_list[0])
                print('设置固定随机的user-agent')

    def process_response(self,request,response,spider):
        # random_seed = [0, 1]
        # from random import choice
        # a = choice(random_seed)
        # if a == 1:
        #     time.sleep(5)
        response_url = response.url
        if len(re.findall('property-overview',response_url))==0 and response.status == 200:
            with open('./has_already_crawl_url.txt','a+') as f:
                f.write(response_url+'\n')
        if response.status == 302:
            time.sleep(1890)
            print('被发现了，沉睡30分钟切换user-agent')
            print('byte user agent',request.headers['User-Agent'])
            invalidation_user_agent = request.headers['User-Agent'].decode()
            print(invalidation_user_agent)

            with open('./invalidation_user_agent_file.txt','a+') as f:
                # f.write('\n')
                f.write('\n'+invalidation_user_agent)
                # f.write('\n')

            spider.user_agent_list.remove(invalidation_user_agent)

            if len(spider.user_agent_list) == 0:
                print('user-agent没有了')
                spider.crawler.engine.close_spider(spider, 'user-agent 更换完了，已经没有了')
                # spider.crawler.engine.stop(spider,'user_agent_list 没有了')
                # from scrapy.crawler.engine import CloseSpider
                # raise CloseSpider()
                # spider.crawler.engine.pause()
                # from scrapy import cmdline
                # cmdline.execute('ctrl c')

            if len(spider.user_agent_list) > 0:
                request.headers['User-Agent'] = spider.user_agent_list[0]

            return request
        return response


# realtor list page middleware
# mainly add time delay
class RealtorListPageDelayAnd302Middleware1(object):
    def __init__(self):
        super(RealtorListPageDelayAnd302Middleware1,self).__init__()
        self.stop_signal = 1
        # self.user_agent_index = 0
    def process_request(self, request, spider):
        # # 随机停顿
        random_seed = [0, 1]
        from random import choice
        a = choice(random_seed)
        print('a:-----------------', a)
        if a == 1:
            time.sleep(5)

        # 爬虫爬取3个小时后停止31分钟
        spider_scrapy_start_time = spider.scrapy_start_time
        if spider_scrapy_start_time is not None:
            scrapy_time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            true_scrapy_time_now = datetime.datetime.strptime(scrapy_time_now, '%Y-%m-%d %H:%M:%S')
            time_seconds_subtract = true_scrapy_time_now - spider_scrapy_start_time

            time_hour_subtract = int(time_seconds_subtract.seconds / 3600)

            print('时间间隔：', time_hour_subtract)
            if time_hour_subtract % 2 == 0 and time_hour_subtract !=0:
                time.sleep(1200)


    def process_response(self, request, response, spider):
        print(response.status)
        if response.status in [x for x in range(300,500)]:
            print('当前的status code：', response.status)
            # 设置暂停时间
            import time
            time.sleep(1)
            self.stop_signal += 1
            print(self.stop_signal)

            if self.stop_signal > 100:
                spider.crawler.engine.close_spider(spider, '爬虫已经被发现了')


            # # 去掉该user-agent,同时将change_user_agent置为True
            # print(request.headeres['user-agent'])
            # realtor_user_agent_list.remove(request.headers['user-agent'])
            # self.change_user_agent = True
            # return request
        return response


class RealtorListPageDelayAnd302Middleware(object):
    def __init__(self):
        super(RealtorListPageDelayAnd302Middleware,self).__init__()
        self.stop_signal = 1
        # self.user_agent_index = 0
    def process_request(self, request, spider):
        # # 随机停顿
        random_seed = [0, 1]
        from random import choice
        a = choice(random_seed)
        print('a:-----------------', a)
        if a == 1:
            time.sleep(3)


    def process_response(self, request, response, spider):
        print(response.status)
        if response.status in [x for x in range(300,500)]:
            print('当前的status code：', response.status)
            # 设置暂停时间
            import time
            time.sleep(1)
            self.stop_signal += 1
            print(self.stop_signal)

            if self.stop_signal > 100:
                spider.crawler.engine.close_spider(spider, '爬虫已经被发现了')


            # # 去掉该user-agent,同时将change_user_agent置为True
            # print(request.headeres['user-agent'])
            # realtor_user_agent_list.remove(request.headers['user-agent'])
            # self.change_user_agent = True
            # return request
        return response




# 使用代理ip进行抓取:
class AlterProxyIPMiddleware(object):

    def process_request(self, request, spider):
        if getattr(spider, 'proxy_ip_list', None) is not None:
            print(spider.proxy_ip_list)
            spider_proxy_ip_list = spider.proxy_ip_list
            print(len(spider_proxy_ip_list))
            if len(spider_proxy_ip_list) != 0:
                # 每次固定取第零个
                print('设置代理ip并打印', spider_proxy_ip_list[0])
                request.meta["proxy"] = spider_proxy_ip_list[0]
                print('设置固定的proxy_ip')

    def process_response(self,request,response,spider):
        if response.status == 302:
            print(request.meta['proxy'])
            print(request.headers['proxy'].decode())

            spider.proxy_ip_list.remove((request.meta['proxy']).decode())

            if len(spider.proxy_ip_list) == 0:
                print('user-agent没有了')
                spider.crawler.engine.close_spider(spider, '更换了1000次user-agent了,爬虫已经被发现了')
                # spider.crawler.engine.stop(spider,'user_agent_list 没有了')
                # from scrapy.crawler.engine import CloseSpider
                # raise CloseSpider()
                # spider.crawler.engine.pause()
                # from scrapy import cmdline
                # cmdline.execute('ctrl c')

            if len(spider.proxy_ip_list) > 0:
                request.meta['proxy'] = spider.proxy_ip_list[0]

            return request
        return response





class Test(object):
    def __init__(self):
        self.test = 1


# if hasattr(Test, 'attr1'):
#     if Test.attr1 != 0:
#         pass






# trulia change cookie when encounter 403
class AlertCookieWhenEncounter403Middleware(object):
    def __init__(self):
        super(AlertCookieWhenEncounter403Middleware,self).__init__()
        self.stop_signal = 1

    def process_response(self, request, response, spider):
        print(response.status)
        if response.status == 302:
            self.stop_signal += 1
            print(self.stop_signal)

            if self.stop_signal > 200:
                spider.crawler.engine.close_spider(spider, '更换了200次user-agent了,user-agent已经没有了')
            request.headers.setdefault('cookie','cookie')
            return request
        return response


# #动态ip代理
# class RandomProxyMiddleware(object):
#     # 动态设置ip代理
#     def process_request(self,request,spider):
#         get_ip = GetIP()
#         request.meta["proxy"] = get_ip.get_random_ip()


# 多进程+代理ip
# class RandomProxyMiddleware(object):
#     # 动态设置ip代理
#     def process_request(self,request,spider):
#         get_ip = GetIP()
#         request.meta["proxy"] = get_ip.get_random_ip()


# 测试代理的使用
class RandomProxyMiddleware(object):
    # 动态设置ip代理
    def process_request(self,request,spider):
        # 通过meta传递
        request.meta["proxy"] = 'http://121.61.3.143:9999',


# 从csv中加载代理ip,然后...
'''
csv文件中加载不好删除,还是放到数据库中好了,
取得时候随机取,这样就可以让不同进程取到相同代理ip得概率变低,并且可以减少不同进程爬虫在获取ip得逻辑
    2:然后判断,如果延迟时间太大了,或者是出现状态码非200-300之间就从数据库中删除该代理ip,然后,在随机获取一个然后保持不变;(这个在middleware中处理)
    3:多进程调度程序(或者是多线程),user-agent从列表中获取(可以从文件中读取,也可以直接设置在setting中)
        但是这里存在一个问题就是怎样维护一个列表(必须是全局的,然后可以改变)这种方式写的时候可能不成熟;
        还有一种就是放到文件中(数据库中也可以,但是没有必要),如果发现user-agent不能用了,就直接删除掉(可以用到文件的操作,
        同时将不能用的user-agnent,存到一个新的文件中;
        
        这里还有一个问题就是切换user-agent和ip_proxy的问题,如果使用了ip-proxy起始不用从列表中删除user-agent,因为ip变了;
        但是如果不使用代理ip的情况下,那就只能从列表中删除,然后重新获取一个user-agent,设置到请求中后 ,在再middleware中的process_response 中返回(这里还存在一个问题就是到底要不要使用request.headers.setdefault 方法);测试一下,结果是:
'''


# 测试scrapy 自带的断点续爬:
class TestCrawlerBreakContinuedClimb(object):
    def __init__(self):
        # super(Process302Middleware,self).__init__()
        self.stop_signal = 1

    def process_response(self, request, response, spider):
        print(response.status)
        if response.status == 302:
            self.stop_signal += 1
            print(self.stop_signal)
            print('response.url', response._url)
            if self.stop_signal > 2:
                spider.crawler.engine.close_spider(spider, '遇到302错误大于3次,爬虫已经被服务器发现')
            return request
        return response


#trulia website
# trulia process 403 problem according to alert cookie
class ProcessTrulia403Middleware(object):

    def process_request(self, request, spider):
        if getattr(spider, 'trulia_cookies_list', None) is not None:
            print(spider.trulia_cookies_list)
            spider_trulia_cookies_list = spider.trulia_cookies_list
            print(len(spider_trulia_cookies_list))
            if len(spider_trulia_cookies_list) != 0:
                # 每次固定取第零个
                print('设置的cookie:',spider_trulia_cookies_list[0])
                request.headers.setdefault('cookie',spider_trulia_cookies_list[0])
                print('设置固定的cookie')

    def process_response(self,request,response,spider):
        if response.status == 302:
            import time
            time.sleep(600)
            print(request.headers['cookie'])
            print(request.headers['cookie'].decode())

            spider.trulia_cookies_list.remove((request.headers['cookie']).decode())

            if len(spider.trulia_cookies_list) == 0:
                print('cookie没有了')
                spider.crawler.engine.close_spider(spider, 'cookie has already none')

            if len(spider.trulia_cookies_list) > 0:
                request.headers['cookie'] = spider.trulia_cookies_list[0]

            return request
        return response


# realtor middleware
'''
list 页面，就加一个
'''

class RealtorListPageMiddleware(object):
    def __init__(self):
        super(RealtorListPageMiddleware,self).__init__()
        self.stop_signal = 1
        # self.user_agent_index = 0

    def process_request(self, request, spider):
        # # 随机停顿
        random_seed = [0, 1]
        from random import choice
        a = choice(random_seed)
        print('a:-----------------', a)
        if a == 1:
            time.sleep(3)


    def process_response(self, request, response, spider):
        print(response.status)
        if response.status in [x for x in range(300,500)]:
            print('当前的status code：', response.status)
            # 设置暂停时间
            import time
            time.sleep(1)
            self.stop_signal += 1
            print(self.stop_signal)

            if self.stop_signal > 100:
                spider.crawler.engine.close_spider(spider, '爬虫已经被发现了')


            # # 去掉该user-agent,同时将change_user_agent置为True
            # print(request.headeres['user-agent'])
            # realtor_user_agent_list.remove(request.headers['user-agent'])
            # self.change_user_agent = True
            # return request
        return response


class RealtorListPageSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)

        return s

    def update_detail_data(self,conn, time):
        print("更新detail数据")
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()
        realtor_update_property_id_sql_str = '''
        SELECT
        	rl."propertyId" AS "listPropertyId",
        	rl."lastUpdate" AS "listLastUpdate",
        	rl.address AS "listAddress"
        FROM
        	realtor_list_page_json_splite rl
        	INNER JOIN realtor_detail_page_json rd ON rl."propertyId" = rd."propertyId"
        	WHERE rl."lastUpdate"!=rd."lastUpdate"
        	OR rl.address!=rd.address
        '''

        # 获取需要更新的数据
        results2 = cursor2.execute(realtor_update_property_id_sql_str)

        # 批量更新数据
        sql_string1 = '''
        UPDATE
        realtor_detail_page_json rj
        set
        "isDirty" = '1', "lastUpdate" = tmp."lastUpdate", address = tmp.address，"optionDate"=now()
        FROM(
        values
        '''

        sql_string2 = '''
         ) as tmp("propertyId", "lastUpdate",address)
         WHERE rj."propertyId" =tmp."propertyId"
        '''
        sql_string3_list = []
        j = 1
        if time == 1:
            print('第一次更新跟新了{}'.format(cursor2.rowcount))
            batch_size = 100
        if time == 2:
            batch_size = cursor2.rowcount
            print('第2次更新跟新了{}'.format(cursor2.rowcount))

        for i in cursor2.fetchall():
            # print("跟新"+str(i))
            if len(re.findall(r"'", i[2])) > 0:
                # print(i[2])
                i = list(i)
                i[2] = i[2].replace("'", "''")
                i = tuple(i)
                i = str(i)
                i = i.replace('"', "'")
            i = str(i)
            # print(i)
            sql_string3_list.append(i)
            if len(sql_string3_list) == batch_size:
                sql_string3 = ','.join(sql_string3_list)
                final_string = sql_string1 + sql_string3 + sql_string2
                # print(final_string)
                cursor1.execute(final_string)
                conn.commit()
                sql_string3_list = []

    def splite_list_data(self,conn):
        print("拆分数据")
        cursor = conn.cursor()
        sql_string_splite = '''
            INSERT INTO realtor_list_page_json_splite ( "propertyId", "lastUpdate", address, "optionDate" ) (
            SELECT DISTINCT ON
                ( n_table."propertyId" ) n_table."propertyId",
                n_table."lastUpdate",
                n_table.address,
                n_table."optionDate" 
            FROM
                (
                SELECT
                    to_number( json_array_elements ( "jsonData" -> 'listings' ) ->> 'property_id', '9999999999' ) AS "propertyId",
                    json_array_elements ( "jsonData" -> 'listings' ) ->> 'last_update' AS "lastUpdate",
                    json_array_elements ( "jsonData" -> 'listings' ) ->> 'address' AS address,
                    now() AS "optionDate" 
                FROM
                    realtor_list_page_json 
                ) n_table 
            WHERE
                n_table."propertyId" IS NOT NULL 
                AND n_table."lastUpdate" IS NOT NULL 
            AND n_table.address IS NOT NULL 
            )
        '''
        cursor.execute(sql_string_splite)
        print("拆分了{}条数据".format(cursor.rowcount))
        conn.commit()

    def insert_detail_data(self,conn):
        print('插入detail没有的propertyId')
        cursor = conn.cursor()
        sql_string_insert= '''
            INSERT INTO realtor_detail_page_json( "propertyId", "lastUpdate", address,"isDirty","optionDate")
        (SELECT
            rl."propertyId" AS "listPropertyId",
            rl."lastUpdate" AS "listLastUpdate",
            rl.address AS "listAddress",
            0,
            now()
        FROM
            realtor_list_page_json_splite rl
            left JOIN realtor_detail_page_json rd ON rl."propertyId" = rd."propertyId"
            WHERE 
            rd."propertyId" is NULL 
            and rl."propertyId" is NOT null
             and rl."lastUpdate" is NOT NULL
             and rl.address is NOT NULL
            )
        '''
        cursor.execute(sql_string_insert)
        print("插入detail 表没有的数据：{}条".format(cursor.rowcount))
        conn.commit()

    def get_detail_url(self,conn):
        print("将数据插入redis")
        import redis
        pool = redis.ConnectionPool(host='127.0.0.1',
                                    # password='123456'
                                    )
        redis_pool = redis.Redis(connection_pool=pool)
        redis_pool.flushdb()
        cursor = conn.cursor()
        sql_string = '''
            SELECT
        	"propertyId" 
        FROM
        	realtor_detail_page_json 
        WHERE
        	"isDirty" = '1' 
        	OR "detailJson" IS NULL
        '''
        cursor.execute(sql_string)
        print("将{}条properyId 插入redis".format(cursor.rowcount))
        for result in cursor.fetchall():
            redis_pool.lpush('realtor:property_id', 'http://{}'.format(result[0]))
        conn.commit()


    def spider_closed(self, spider):
        # spider.logger.info('Spider closed: %s', spider.name)
        conn = get_psql_con.get_psql_con()
        # 将realtor_list_json表中的数据拆分开,并删除空的情况
        self.splite_list_data(conn)
        # 找到有的propertyId 并且lastUpate和address字段改变了的，这里应该使用批量更新
        self.update_detail_data(conn,1)
        self.update_detail_data(conn,2)
        # 找到detail_page_json 表中没有的propertyId，并将它插入到该表中；
        self.insert_detail_data(conn)
        self.get_detail_url(conn)
        conn.close()
        print('完成sql插入---------------------------------------------')


class RealtorListPageMysqlSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)

        return s

    def update_detail_data(self,conn, update_time, batch_size):
        print("更新detail数据")
        cursor1 = conn.cursor()
        cursor2 = conn.cursor()
        realtor_update_property_id_sql_str = '''
            SELECT
                rl.propertyId AS listPropertyId,
                rl.lastUpdate AS listLastUpdate,
                rl.address AS listAddress 
            FROM
                realtor_list_page_json_splite rl
                INNER JOIN realtor_detail_json rd ON rl.propertyId = rd.propertyId
            WHERE
                rl.lastUpdate != rd.lastUpdate
                OR rl.address != rd.address
        '''

        # 获取需要更新的数据
        results2 = cursor2.execute(realtor_update_property_id_sql_str)

        # 批量更新数据
        sql_string1 = '''
            UPDATE
              realtor_detail_json rj
            set
              isDirty = '1', lastUpdate = %s, address = %s,optionDate=now()
            WHERE rj.propertyId =%s
        '''
        sql_string3_list = []
        if update_time == 1:
            print('第一次更新跟新了{}'.format(cursor2.rowcount))
            batch_size = batch_size
        if update_time == 2:
            batch_size = cursor2.rowcount
            print('第2次更新跟新了{}'.format(cursor2.rowcount))

        for i in cursor2.fetchall():
            # print(i)
            sql_string3_list.append([i[1], i[2], i[0]])
            if len(sql_string3_list) == batch_size:
                cursor1.executemany(sql_string1, sql_string3_list)
                conn.commit()
                sql_string3_list = []

    def splite_list_data(self,conn):
        print("拆分数据")
        cursor = conn.cursor()
        sql_string_splite = '''
            INSERT INTO realtor_list_page_json_splite ( propertyId, lastUpdate, address, optionDate ) (
                SELECT 
                    n_table.propertyId,
                    n_table.lastUpdate,
                    n_table.address,
                    n_table.optionDate
                FROM
                    (
                    SELECT
                        cast(JSON_EXTRACT( rj.jsonData, '$.property_id') as SIGNED) as propertyId ,
                        JSON_EXTRACT( rj.jsonData, '$.last_update') as lastUpdate,
                        JSON_EXTRACT( rj.jsonData, '$.address') as address,
                        now( ) AS optionDate
                    FROM
                        realtor_list_page_json rj
                    ) n_table 
                    
                WHERE
                    n_table.propertyId IS NOT NULL 
                    AND n_table.lastUpdate IS NOT NULL 
                AND n_table.address IS NOT NULL 
                    GROUP BY n_table.propertyId
                )

        '''
        cursor.execute(sql_string_splite)
        print("拆分了{}条数据".format(cursor.rowcount))
        conn.commit()

    def insert_detail_data(self,conn):
        print('插入detail没有的propertyId')
        cursor = conn.cursor()
        sql_string_insert= '''
            INSERT INTO realtor_detail_json ( propertyId, lastUpdate, address, isDirty, optionDate ) (
                SELECT
                    rl.propertyId AS listPropertyId,
                    rl.lastUpdate AS listLastUpdate,
                    rl.address AS listAddress,
                    0,
                    now( ) 
                FROM
                    realtor_list_page_json_splite rl
                    LEFT JOIN realtor_detail_json rd ON rl.propertyId = rd.propertyId
                WHERE
                    rd.propertyId IS NULL 
                    AND rl.propertyId IS NOT NULL 
                    AND rl.lastUpdate IS NOT NULL 
                    AND rl.address IS NOT NULL 
                )
        '''
        cursor.execute(sql_string_insert)
        print("插入detail 表没有的数据：{}条".format(cursor.rowcount))
        conn.commit()

    def get_detail_url(self,conn):
        import redis
        pool = redis.ConnectionPool(host='127.0.0.1',
                                    # password='123456'
                                    )
        redis_pool = redis.Redis(connection_pool=pool)
        redis_pool.flushdb()
        cursor = conn.cursor()
        sql_string = '''
            SELECT
        	 propertyId
        FROM
        	 realtor_detail_json 
        WHERE
        	 isDirty = '1' 
        	 OR detailJson IS NULL
        '''
        cursor.execute(sql_string)
        print("将{}条properyId 插入redis".format(cursor.rowcount))
        for result in cursor.fetchall():
            redis_pool.lpush('realtor:property_id', 'http://{}'.format(result[0]))
        conn.commit()

    def spider_closed(self, spider):
        # spider.logger.info('Spider closed: %s', spider.name)
        conn = get_sql_con()
        # 将realtor_list_json表中的数据拆分开,并删除空的情况
        self.splite_list_data(conn)
        # 找到有的propertyId 并且lastUpate和address字段改变了的，这里应该使用批量更新
        self.update_detail_data(conn, 1, 100)
        self.update_detail_data(conn, 2, 100)
        # 找到detail_page_json 表中没有的propertyId，并将它插入到该表中；
        self.insert_detail_data(conn)
        self.get_detail_url(conn)
        conn.close()
        print('完成sql插入---------------------------------------------')




class RealtorDetailPageAMiddleware(object):
    def __init__(self):
        super(RealtorDetailPageAMiddleware,self).__init__()
        self.stop_signal = 1
        # self.user_agent_index = 0
    def process_request(self, request, spider):
        # # 随机停顿
        # random_seed = [0, 1]
        # from random import choice
        # a = choice(random_seed)
        # print('a:-----------------', a)
        # if a == 1:
        #     time.sleep(5)

        # 爬虫爬取3个小时后停止31分钟
        spider_scrapy_start_time = spider.scrapy_start_time
        if spider_scrapy_start_time is not None:
            scrapy_time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            true_scrapy_time_now = datetime.datetime.strptime(scrapy_time_now, '%Y-%m-%d %H:%M:%S')
            time_seconds_subtract = true_scrapy_time_now - spider_scrapy_start_time
            print(time_seconds_subtract.seconds)
            time_seconds_subtract = int(time_seconds_subtract.seconds)

            # time_hour_subtract = int(time_seconds_subtract.seconds / 3600)

            print('时间间隔：', time_seconds_subtract)
            if time_seconds_subtract % 3600 == 0 and time_seconds_subtract !=0:
                print('sleep中')
                time.sleep(900)


    def process_response(self, request, response, spider):
        print(response.status)
        if response.status in [x for x in range(300,500)]:
            print('当前的status code：', response.status)
            with open('./url.text','w')as f:
                f.write(response.url+'\n')
            # 设置暂停时间
            import time
            time.sleep(300)
            self.stop_signal += 1
            print(self.stop_signal)

            if self.stop_signal > 100:
                spider.crawler.engine.close_spider(spider, '爬虫已经被发现了')


            # # 去掉该user-agent,同时将change_user_agent置为True
            # print(request.headeres['user-agent'])
            # realtor_user_agent_list.remove(request.headers['user-agent'])
            # self.change_user_agent = True
            # return request
        return response


class RealtorDetailPageWMiddleware(object):

    def process_request(self, request, spider):
        # # 随机停顿
        random_seed = [0,1]
        from random import choice
        a = choice(random_seed)
        print('a:-----------------',a)
        if a == 1:
            time.sleep(3)

        # 爬虫爬取3个小时后停止31分钟
        spider_scrapy_start_time = spider.scrapy_start_time
        if spider_scrapy_start_time is not None:
            scrapy_time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            true_scrapy_time_now = datetime.datetime.strptime(scrapy_time_now, '%Y-%m-%d %H:%M:%S')
            time_seconds_subtract = true_scrapy_time_now - spider_scrapy_start_time
            print(time_seconds_subtract.seconds)
            time_seconds_subtract = int(time_seconds_subtract.seconds)


            print('时间间隔：', time_seconds_subtract)
            if time_seconds_subtract % 3600 == 0 and time_seconds_subtract !=0:
                print('sleep中')
                time.sleep(900)
        if getattr(spider, 'user_agent_list', None) is not None :
            print(spider.user_agent_list)
            spider_user_agent_list = spider.user_agent_list
            print(len(spider_user_agent_list))
            if len(spider_user_agent_list) != 0:
                # 每次固定取第零个
                # 每次随机获取一个：
                print('设置的user-agent',spider_user_agent_list[0])
                request.headers.setdefault('User-Agent',spider_user_agent_list[0])

                agent_random_seed = [0, 1,2,3,4,5,6,7,8,9]
                from random import choice
                a = choice(agent_random_seed)
                if a == 1:
                    user_agent_random_index = choice(
                        [random_seed for random_seed in range(len(spider_user_agent_list))])
                    print('设置的user-agent', spider_user_agent_list[user_agent_random_index])
                    request.headers.setdefault('User-Agent', spider_user_agent_list[user_agent_random_index])

                # request.headers.setdefault('User-Agent', spider_user_agent_list[0])
                print('设置固定随机的user-agent')

    def process_response(self,request,response,spider):
        response_url = response.url
        if len(re.findall('property-overview',response_url))==0 and response.status == 200:
            with open('./has_already_crawl_url.txt','a+') as f:
                f.write(response_url+'\n')
        if response.status == 302:
            time.sleep(1890)
            print('被发现了，沉睡30分钟切换user-agent')
            print('byte user agent',request.headers['User-Agent'])
            invalidation_user_agent = request.headers['User-Agent'].decode()
            print(invalidation_user_agent)

            with open('./invalidation_user_agent_file.txt', 'a+') as f:
                f.write('\n'+invalidation_user_agent)

            spider.user_agent_list.remove(invalidation_user_agent)

            if len(spider.user_agent_list) == 0:
                print('user-agent没有了')
                spider.crawler.engine.close_spider(spider, 'user-agent 更换完了，已经没有了')

            if len(spider.user_agent_list) > 0:
                request.headers['User-Agent'] = spider.user_agent_list[0]

            return request
        return response


class RealtorDetailPageAProcessUrlMiddleware(object):
    def __init__(self):
        super(RealtorDetailPageAProcessUrlMiddleware, self).__init__()

    def process_request(self, request, spider):
        print(request.url)
        property_id = re.search(r'\d+',request.url).group()
        request._url='https://mapi-ng.rdc.moveaws.com/api/v1/properties/{}?client_id=rdc_mobile_native%2C9.3.7%2Candroid'.format(property_id)
        print(request.url)

    def process_response(self, request, response, spider):

        return response


class RealtorDetailPageWProcessUrlMiddleware(object):
    def __init__(self):
        super(RealtorDetailPageWProcessUrlMiddleware, self).__init__()

    def process_request(self, request, spider):
        print(request.url)
        property_id = re.search(r'\d+',request.url).group()
        request._url = 'https://www.realtor.com/property-overview/M{}'.format(property_id)
        print(request.url)

    def process_response(self, request, response, spider):

        return response












