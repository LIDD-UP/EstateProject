import datetime
from scrapy.cmdline import execute

scrapy_start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

execute(['scrapy', 'crawl',
         # 'realtor',
         # 'realtor_app',
         # 'realtor_property_web',
         'realtor_web_app_merge_by_property',
         # "-a",
         # "start_urls={}".format(start_urls),
         # "-a",
         # "user_agent_list={}".format(user_agent_list),
         "-a",
         "scrapy_start_time={}".format(scrapy_start_time)
         # "-s",
         # "JOBDIR=crawls/realtor{}".format(num),
         ])