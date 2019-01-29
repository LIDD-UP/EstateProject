# -*- coding: utf-8 -*-

# Scrapy settings for AmericanRealEstate project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'AmericanRealEstate'

SPIDER_MODULES = ['AmericanRealEstate.spiders']
NEWSPIDER_MODULE = 'AmericanRealEstate.spiders'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'AmericanRealEstate (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 爬虫提升配置
# 并发：同时处理request的数量
# CONCURRENT_REQUESTS = 100
# 降低log级别：降低到INFO级别就不能获取重定向的一些信息了
# LOG_LEVEL = 'INFO'
# 对于不需要登陆的网站禁用cookies
# COOKIES_ENABLED = False
# 禁止重试:对于失败的http请求取消重试；但是这个还需要考虑
# RETRY_ENABLED = False

# 如果您对一个非常慢的连接进行爬取(一般对通用爬虫来说并不重要)， 减小下载超时能让卡住的连接能被快速的放弃并解放处理其他站点的能力。
# DOWNLOAD_TIMEOUT = 15 # 其中15是设置的下载超时时间

# 禁止重定向
# REDIRECT_ENABLED = False
# 设置代理ip池，可以使用downloadermiddleware
# 配置请求头


# 自动限速设置：
# AUTOTHROTTLE_ENABLED = True
# DOWNLOAD_DELAY = 1


# DOWNLOADER_MIDDLEWARES = {
#    # 'AmericanRealEstate.middlewares.AmericanrealestateDownloaderMiddleware': 543,
#    #  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#    #  'AmericanRealEstate.middlewares.RandomUserAgentMiddleware': 543,
# }
RANDOM_UA_TYPE = "random"





# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'AmericanRealEstate.middlewares.AmericanrealestateSpiderMiddleware': 543,
#}

# # redis 设置：
# # Enables scheduling storing requests queue in redis.
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# # Ensure all spiders share same duplicates filter through redis.
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html




# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'AmericanRealEstate.pipelines.AmericanrealestatePipeline': 300,
   #  'scrapy_redis.pipelines.RedisPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# mysql 本地数据库配置
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_DBNAME = 'america_real_estate'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'

# 日子输出：
# LOG_FILE="log.txt"

# redis settings

# 搜索条件设置
import pandas as pd
realtor_search_criteria = list(pd.read_csv(r'F:\PycharmProject\EstateProject\AmericanRealEstate\crawl_tools\realtor_search_criteria.csv')['countyStateJoin'])
trulia_search_criteria = list(pd.read_csv(r'F:\PycharmProject\EstateProject\AmericanRealEstate\crawl_tools\trulia_search_criteria.csv')['countyStateJoin'])


# post_url
post_interface_url = 'http://192.168.0.65:8080/America-DataSave/index/saveRealtorDataJson/'

# realtor domain url
realtor_domain_url = 'https://www.realtor.com/'
trulia_domain_url = 'https://www.trulia.com/'

# 代理ip列表:
proxy_ip_list = [
'119.101.124.223:9999',
    '119.101.125.75:9999',
    '58.240.7.195:32558',
    '222.217.68.51:39682',
    '119.101.125.180:9999',
    '119.101.126.9:9999',
# http://119.101.124.223:9999
# http://119.101.125.75:9999
# http://58.240.7.195:32558
# http://222.217.68.51:39682
# http://119.101.125.180:9999
# http://119.101.126.9:9999
]

# scrapy-proxie settings
# Retry many times since proxies often fail
RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
#     'scrapy_proxies.RandomProxy': 100,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
# }

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
PROXY_LIST = 'F:\PycharmProject\EstateProject\AmericanRealEstate\crawl_tools\get_proxy/list.txt'

# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
PROXY_MODE = 2

# If proxy mode is 2 uncomment this sentence :
CUSTOM_PROXY = "http://host1:port"


realtor_user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chome/41.0.2228.0 Saari/57.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppeWebKit/57.36 (KHTML, like Gecko) Chome/41.0.2227.1 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (HTML, like Gecko) Crome/41.0.2227.0 Saari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, lke Geko) Chrome/41.0.227.0 Safai/37.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) pplWebKit/537.36 (KHTML, like Gecko) Chrome/46.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.4; WOW64) ApplbKit/537.36 (KHTML, like Gecko) Chrome/41.0.22ari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWet/537.36 (KHTML, ike Geco) hrome/41.0.2225.0 Sfari/37.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebt/537.36 (KHTML, like Gecko) Chrome/41.0.224.3 Saari/537.36',
    'Mozilla/5.0 (Windos NT 10.0) ApplebKit/537.36 (KHTML, like Geko) Chrme/400.2214.93 Saari57.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/57.36 (KHTML, like Gecko) Crome/37.02062.124 Safari/537.36',
    'Mozilla/5.0 (Wndows NT 6.3; Win4; x64) AppleWebKit/537.36 (KTML, like Gecko) Chome/37..2049.0 Safari/57.36',
    'Mozilla/5.0 (Wndows T 4.0; WOW64) AppleWeKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
    'Mozilla/5.0 (X11; OpenBSD i386) AppleWbKit/537.36 (KHTML, like Gecko) Chome/36.01985.125 Safari/537.36',
    'Mozilla/5.0 (Macitosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
    'Mozilla/5.0 (Winows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
    'Mozilla/5.0 (Widows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chme/35.0.2309.372 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko)hrome/35.0.2117.157 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Geck Chrome/34.0.1866.237 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, liecko) Chrome/34.0.1847.137 Safari/4E423F',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, liGecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHT like Gecko) Chrome/33.0.1750.517 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit7.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) ApWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) pleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537. (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWeit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) ApplbKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) ApeWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 4319. AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; W4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.ppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36',
    'Mozilla/5.0 (Windows  6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
    'Mozilla/5.0 (WindowNT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Winds NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Winows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/5376',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari7.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrom7.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Che/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.Safari/537.36',
    'Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.1 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrom4.0.1312.60 Safari/537.17',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, likeecko) Chrome/24.0.1309.0 Safari/537.17',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Come/24.0.1295.0 Safari/537.15',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko)hrome/24.0.1292.0 Safari/537.14',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/1214',
    'Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 refox/4.0 Opera 12.14',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0)pera 12.14',
    'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.9 Version/12.02',
    'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/.181 Version/12.00',
    'Opera/9.80 (Windows NT 5.1; U; zh-sg) Pres2.9.181 Version/12.00',
    'Opera/12.0(Windows NT 5.2;U;en)Presto/22.168 Version/12.00',
    'Opera/12.0(Windows NT 5.1;U;en)Presto/2.9.168 Version/12.00',
    'Mozilla/5.0 (Windows NT 5.1) Gecko/2010101 Firefox/14.0 Opera/12.0',
    'Opera/9.80 (Windows NT 6.1; WOW64; pt) Presto/2.10.229 Version/11.62',
    'Opera/9.80 (Windows NT 6.0; U; plPresto/2.10.229 Version/11.62',
    'Opera/9.80 (Macintosh; Intel MaOS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
    'Opera/9.80 (Macintosh; Intel c OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52',
    'Opera/9.80 (Windows NT 5.1;; en) Presto/2.9.168 Version/11.51',
    'Mozilla/5.0 (compatible; IE 9.0; Windows NT 6.1; de) Opera 11.51',
    'Opera/9.80 (X11; Linux 6_64; U; fr) Presto/2.9.168 Version/11.50',
    'Opera/9.80 (X11; Linui686; U; hu) Presto/2.9.168 Version/11.50',
    'Opera/9.80 (X11; Lix i686; U; ru) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (X11; Lnux i686; U; es-ES) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/200618 Firefox/5.0 Opera 11.11',
    'Opera/9.80 (X11; Linux x86_64; U; bg) Presto/2.8.131 Veion/11.10',
    'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Versn/11.10',
    'Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.13Version/11.10',
    'Opera/9.80 (Windows NT 6.1; Opera Tablet/15165; Uen) Presto/2.8.149 Version/11.1',
    'Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 averick); pl) Presto/2.7.62 Version/11.01',
    'Opera/9.80 (X11; Linux i686; U; ja) Presto/2.762 Version/11.01',
    'Opera/9.80 (X11; Linux i686; U; fr) Presto/2.62 Version/11.01',
    'Opera/9.80 (Windows NT 6.1; U; zh-tw) Pres/2.7.62 Version/11.01',
    'Opera/9.80 (Windows NT 6.1; U; zh-cn) Prto/2.7.62 Version/11.01',
    'Opera/9.80 (Windows NT 6.1; U; sv) Preo/2.7.62 Version/11.01',
    'Opera/9.80 (Windows NT 6.1; U; en-USPresto/2.7.62 Version/11.01',
    'Opera/9.80 (Windows NT 6.1; U; cs)resto/2.7.62 Version/11.01',
    'Opera/9.80 (Windows NT 6.0; U; p Presto/2.7.62 Version/11.01',
    'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.7.62 Version/11.01',
    'Opera/9.80 (Windows NT 5.1; U;) Presto/2.7.62 Version/11.01',
    'Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.7.62ersion/11.01',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-USrv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 6.1; U; nl; rv:1.9) Gecko/20091201 Firefox/3.5.6 Opera 11.01',
    'Mozilla/5.0 (Windows NT 6.1; U; de; rv:.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01',
    'Mozilla/4.0 (compatible; MSIE 8.0; Wows NT 6.1; de) Opera 11.01',
    'Opera/9.80 (X11; Linux x86_64; U;) Presto/2.7.62 Version/11.00',
    'Opera/9.80 (X11; Linux i686; Ut) Presto/2.7.62 Version/11.00',
    'Opera/9.80 (Windows NT 6.1; zh-cn) Presto/2.6.37 Version/11.00',
    'Opera/9.80 (Windows NT 6 U; pl) Presto/2.7.62 Version/11.00',
    'Opera/9.80 (Windows N.1; U; ko) Presto/2.7.62 Version/11.00',
    'Opera/9.80 (WindowsT 6.1; U; fi) Presto/2.7.62 Version/11.00',
    'Opera/9.80 (Windo NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00',
    'Opera/9.80 (Windows NT 6.1 x64; U; en) Presto/2.7.62 Version/11.00',
    'Opera/9.80 (Windows NT 6.0; U; en) Presto/2.7.39 Version/11.00',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gko/20100101 Firefox/33.0',
    'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101refox/31.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko130401 Firefox/31.0',
    'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20101 Firefox/31.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0)cko/20120101 Firefox/29.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; 25.0) Gecko/20100101 Firefox/29.0',
    'Mozilla/5.0 (X11; OpenBSD amd64; rv:28 Gecko/20100101 Firefox/28.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:0) Gecko/20100101  Firefox/28.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:23) Gecko/20130101 Firefox/27.3',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0',
    'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0',
    'Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/23.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0',
    'Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/22.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/230328 Firefox/22.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20130405 Fifox/22.0',
    'Mozilla/5.0 (Microsoft Windows NT 6.2.9200.0); rv:22 Gecko/20130405 Firefox/22.0',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.Gecko/20121011 Firefox/21.0.1',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:161) Gecko/20121011 Firefox/21.0.1',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:.0.0) Gecko/20121011 Firefox/21.0.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv1.0) Gecko/20130331 Firefox/21.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; r:21.0) Gecko/20100101 Firefox/21.0',
    'Mozilla/5.0 (X11; Linux i686; rv:21.0) cko/20100101 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; r21.0) Gecko/20130514 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 6.2; rv:21. Gecko/20130326 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW6 rv:21.0) Gecko/20130401 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 6.1; WO4; rv:21.0) Gecko/20130331 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 6.1; W64; rv:21.0) Gecko/20130330 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 6.WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 1; rv:21.0) Gecko/20130401 Firefox/21.0',
    'Mozilla/5.0 (Windows N6.1; rv:21.0) Gecko/20130328 Firefox/21.0',
    'Mozilla/5.0 (Windows T 6.1; rv:21.0) Gecko/20100101 Firefox/21.0',
    'Mozilla/5.0 (WindowsNT 5.1; rv:21.0) Gecko/20130401 Firefox/21.0',
    'Mozilla/5.0 (Window NT 5.1; rv:21.0) Gecko/20130331 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20100101 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 5.0; rv:21.0) Gecko/20100101Firefox/21.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21) Gecko/20100101 Firefox/21.0',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64;) Geck100101 Firefox/20.0',
    'Mozilla/5.0 (Windows x86; rv:19.0) Gecko/20101 Firefox/19.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gec20100101 Firefox/19.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:14.0) cko/20100101 Firefox/18.0.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; :18.0)  Gecko/20100101 Firefox/18.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x864; rv:17.0) Gecko/20100101 Firefox/17.0.6',
    'Mozilla/5.0 (Windows NT 6.1; WO; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible, MSIE1, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSI 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0',
    'Mozilla/5.0 (compatible; ME 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)',
    'Mozilla/5.0 (compatible; SIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible;MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (compatible MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)',
    'Mozilla/5.0 (compatibl; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
    'Mozilla/4.0 (Compatibe; MSIE 8.0; Windows NT 5.2; Trident/6.0)',
    'Mozilla/4.0 (compatile; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/1.22 (compible; MSIE 10.0; Windows 3.1)',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))',
    'Mozilla/5.0 (Windws; U; MSIE 9.0; Windows NT 9.0; en-US)',
    'Mozilla/5.0 (comatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)',
    'Mozilla/5.0 (copatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)',
    'Mozilla/5.0 (cmpatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7',
    'Mozilla/5.0 (ompatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trdent/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x4; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win6464; Trident/5.0',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trint/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trdent/5.0; chromeframe/13.0.782.215)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Tident/5.0; chromeframe/11.0.696.57)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; rident/5.0) chromeframe/10.0.648.205',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.; Trident/5.0; chromeframe/11.0.696.57)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 61; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT .0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows N6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows T 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)',
    'Mozilla/5.0 (compatible; MSIE 8.0; WindowsNT 5.2; Trident/4.0; Media Center PC 4.0; SLCC1; .NET CLR 3.0.04320)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Window NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windos NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windws NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Winows NT 5.1; SLCC1; .NET CLR 1.1.4322)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Widows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)',
    'Mozilla/5.0 (compatible; MSIE 7.0; ndows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)',
    'Mozilla/4.0 (compatible; MSIE 8.0;Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0 Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)',
    'Mozilla/4.0 (compatible; MSIE 8.; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8',
    'Mozilla/4.0 (compatible; MSIE 80; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; Media Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)',
    'Mozilla/4.0 (compatible; MSIE .0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
    'Mozilla/4.0 (compatible; MSI8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 3.0)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
    'Mozilla/5.0 (iPad; CPU OS 60 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
    'Mozilla/5.0 (Macintosh; Inel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Macintosh; tel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10',
    'Mozilla/5.0 (iPad; CPU S 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3',
    'Mozilla/5.0 (Macintosh U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    'Mozilla/5.0 (Macintos; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Window U; Windows NT 6.1; ko-KR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; fr-FR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Windos; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Windws; U; Windows NT 6.1; cs-CZ) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Winows; U; Windows NT 6.0; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Widows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Verson/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; sv-se) AppleWebKit/533.20.25 (KHTML, like Gecko) Verion/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ko-kr) AppleWebKit/533.20.25 (KHTML, like Gecko) Vesion/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Vrsion/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; it-it) AppleWebKit/533.20.25 (KHTML, like Gecko) ersion/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-fr) AppleWebKit/533.20.25 (KHTML, like Gecko)Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; es-es) AppleWebKit/533.20.25 (KHTML, like Gecko Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.20.25 (KHTML, like Geck) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-gb) AppleWebKit/533.20.25 (KHTML, like Geco) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; de-de) AppleWebKit/533.20.25 (KHTML, like Geko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/533.19.4 (KHTML, like Gecko) Verson/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Vesion/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Vrsion/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; hu-HU) AppleWebKit/533.19.4 (KHTML, like Gecko) Vrsion/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko)Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.19.4 (KHTML, like Geck Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it-IT) AppleWebKit/533.20.25 (KHTML, like Gko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.20.25 (KHTML, like ecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-us) AppleWebKit/534.16+ (KHTM, like Gecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-ch) AppleWebKit/533.19.4 (KHML, like Gecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15+ (KHML, like Gecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; ar) AppleWebKit/533.19.4 (KHTL, like Gecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.1.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, ike Gecko) Version/5.0.2 Safari/533.18.5',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML,like Gecko) Version/5.0.2 Safari/533.18.5',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; tr-TR) AppleWebKit/533.18.1 (KHTML like Gecko) Version/5.0.2 Safari/533.18.5',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; nb-NO) AppleWebKit/533.18.1 (KHTM, like Gecko) Version/5.0.2 Safari/533.18.5',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTL, like Gecko) Version/5.0.2 Safari/533.18.5',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW) AppleWebKit/533.19.4 (KHML, like Gecko) Version/5.0.2 Safari/533.18.5',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KTML, like Gecko) Version/5.0.2 Safari/533.18.5',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-cn) AppleWebKit/53.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
]