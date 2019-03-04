import os
import sys
# print(os.path.abspath(__file__))
# sys.path.append(os.path.abspath(__file__))

import datetime
from scrapy.cmdline import execute
from crawl_tools.get_psql_con import get_psql_con


def get_detail_url():
    conn = get_psql_con()
    cursor = conn.cursor()
    sql_string = '''
        SELECT
    	"propertyId"
    FROM
    	"realtor_detail_json" 
    WHERE
    	"isDirty" = '1' 
    	OR "detailJson" IS NULL
    '''
    url_lists=[]
    cursor.execute(sql_string)
    for result in cursor.fetchall():
        # print(result)
        url = 'https://mapi-ng.rdc.moveaws.com/api/v1/properties/{}?client_id=rdc_mobile_native%2C9.3.7%2Candroid'.format(result[0])
        url_lists.append(url)
    print(len(url_lists))
    url_lists_string = ','.join(url_lists)
    cursor.close()
    conn.commit()
    conn.close()
    return url_lists_string


# get_detail_url()

# 传入时间和start_urls
scrapy_start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')



execute(['scrapy', 'crawl',
         # 'realtor',
         # 'realtor_app',
         # 'realtor_property_web',
         'realtor_web_app_merge_by_property',
         "-a",
         "start_urls={}".format(get_detail_url()),
         # "-a",
         # "user_agent_list={}".format(user_agent_list),
         "-a",
         "scrapy_start_time={}".format(scrapy_start_time)
         # "-s",
         # "JOBDIR=crawls/realtor{}".format(num),
         ])