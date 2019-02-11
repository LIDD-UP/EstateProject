# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
from scrapy import Request
from AmericanRealEstate.settings import realtor_user_agent_list, trulia_cookies_list
import random


class AmericanrealestateSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
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
        if getattr(spider, 'user_agent_list', None) is not None:
            print(spider.user_agent_list)
            spider_user_agent_list = spider.user_agent_list
            print(len(spider_user_agent_list))
            if len(spider_user_agent_list) != 0:
                # 每次固定取第零个
                print('设置的user-agent',spider_user_agent_list[0])
                request.headers.setdefault('user-agent',spider_user_agent_list[0])
                print('设置固定的user-agent')

    def process_response(self,request,response,spider):
        if response.status == 302:
            import time
            time.sleep(600)
            print('被发现了，沉睡10分钟切换user-agent')
            print(request.headers['user-agent'])
            print(request.headers['user-agent'].decode())

            spider.user_agent_list.remove((request.headers['user-agent']).decode())

            if len(spider.user_agent_list) == 0:
                print('user-agent没有了')
                spider.crawler.engine.close_spider(spider, '更换了1000次user-agent了,爬虫已经被发现了')
                # spider.crawler.engine.stop(spider,'user_agent_list 没有了')
                # from scrapy.crawler.engine import CloseSpider
                # raise CloseSpider()
                # spider.crawler.engine.pause()
                # from scrapy import cmdline
                # cmdline.execute('ctrl c')

            if len(spider.user_agent_list) > 0:
                request.headers['user-agent'] = spider.user_agent_list[0]

            return request
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













