import datetime
from scrapy.cmdline import execute
from crawl_tools.get_psql_con import get_psql_con


truncate_realtor_list_str = '''
    TRUNCATE realtor_list_page_json;
'''

truncate_realtor_list_splite_str = '''
    TRUNCATE realtor_list_page_json_splite
'''
conn = get_psql_con()
cursor = conn.cursor()
cursor.execute(truncate_realtor_list_str)
conn.commit()
cursor.execute(truncate_realtor_list_splite_str)
conn.commit()
conn.close()


scrapy_start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

execute(['scrapy', 'crawl',
         # 'realtor',
         # 'realtor_app',
         # 'realtor_property_web',
         'realtor_app_list_page',
         # "-a",
         # "start_urls={}".format(start_urls),
         # "-a",
         # "user_agent_list={}".format(user_agent_list),
         # "-a",
         # "scrapy_start_time={}".format(scrapy_start_time)
         # "-s",
         # "JOBDIR=crawls/realtor{}".format(num),
         ])


print('yes--------------------------->>>>>>')

















