# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from fake_useragent import UserAgent
from scrapy import Request
from AmericanRealEstate.settings import realtor_user_agent_list


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
        # random_agent = get_ua()
        request.headers.setdefault('User-Agent',get_ua())


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

    def process_response(self, request, response, spider):
        print(response.status)
        if response.status == 302:
            import time
            time.sleep(300)
            self.stop_signal += 1
            print(self.stop_signal)

            if self.stop_signal > 1000:
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
            request.headers.setdefault('user-agent',realtor_user_agent_list[self.user_agent_index])
            self.user_agent_index += 1
            return request
        return response


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


