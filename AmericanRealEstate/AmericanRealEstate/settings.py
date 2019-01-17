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
CONCURRENT_REQUESTS = 100
# 降低log级别：降低到INFO级别就不能获取重定向的一些信息了
LOG_LEVEL = 'INFO'
# 对于不需要登陆的网站禁用cookies
COOKIES_ENABLED = False
# 禁止重试:对于失败的http请求取消重试；但是这个还需要考虑
RETRY_ENABLED = False

# 如果您对一个非常慢的连接进行爬取(一般对通用爬虫来说并不重要)， 减小下载超时能让卡住的连接能被快速的放弃并解放处理其他站点的能力。
DOWNLOAD_TIMEOUT = 15 # 其中15是设置的下载超时时间

# 禁止重定向
REDIRECT_ENABLED = False
# 设置代理ip池，可以使用downloadermiddleware
# 配置请求头


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

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
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

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
DOWNLOADER_MIDDLEWARES = {
   # 'AmericanRealEstate.middlewares.AmericanrealestateDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'AmericanRealEstate.middlewares.RandomUserAgentMiddleware': 543,
}
RANDOM_UA_TYPE = "random"


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
realtor_search_criteria = list(pd.read_csv(r'J:\PycharmProject\EstateProject\AmericanRealEstate\crawl_tools\realtor_search_criteria.csv')['countyStateJoin'])

# post_url
post_interface_url = 'http://192.168.0.65:8080/America-DataSave/index/saveRealtorDataJson/'