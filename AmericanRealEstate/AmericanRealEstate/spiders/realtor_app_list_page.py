# -*- coding: utf-8 -*-
import json
import re

import scrapy

from AmericanRealEstate.settings import realtor_list_search_criteria
from AmericanRealEstate.items import RealtorListPageJsonItem


class RealtorAppListPageSpider(scrapy.Spider):
    name = 'realtor_app_list_page'
    allowed_domains = ['mapi-ng.rdc.moveaws.com']
    start_urls = [x for x in realtor_list_search_criteria]

    custom_settings = {
        "ITEM_PIPELINES": {
            'AmericanRealEstate.pipelines.RealtorListPagePsqlPipeline': 301,
            # 'AmericanRealEstate.pipelines.RealtorListPageMysqlsqlPipeline':302

            # 'AmericanRealEstate.pipelines.RealtorDetailDomPipeline': 302,
            # 'AmericanRealEstate.pipelines.RealtorHouseInfoTestPipeline': 302,
            # 'scrapy_redis.pipelines.RedisPipeline': 300

        },
        "DOWNLOADER_MIDDLEWARES": {
            # 'AmericanRealEstate.middlewares.AmericanrealestateDownloaderMiddleware': 543,
            # 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': None,
            # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
            # 'AmericanRealEstate.middlewares.RandomUserAgentMiddleware': 543,
            # 'AmericanRealEstate.middlewares.TestGetSpiderAttrMiddleware': 1,
            # 'AmericanRealEstate.middlewares.Process302Middleware' :544,
            # 'AmericanRealEstate.middlewares.AlertUserAgentWhenEncounter302Middleware': 545,
            # 'AmericanRealEstate.middlewares.RealtorListPageDelayAnd302Middleware': 545,

        },
        "SPIDER_MIDDLEWARES": {
           # 'AmericanRealEstate.middlewares.RealtorListPageSpiderMiddleware': 543,
            'AmericanRealEstate.middlewares.RealtorListPageMysqlSpiderMiddleware':544
        },
        "DEFAULT_REQUEST_HEADERS": {
            "Cache-Control": "public",
            "Mapi-Bucket": "for_sale_v2:on,for_rent_ldp_v2:on,for_rent_srp_v2:on,recently_sold_ldp_v2:on,recently_sold_srp_v2:on,not_for_sale_ldp_v2:on,not_for_sale_srp_v2:on,search_reranking_srch_rerank1:variant1",
            "Host": "mapi-ng.rdc.moveaws.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.10.0",
    },
        "COOKIES_ENABLED": False,
        "REDIRECT_ENABLED": False,
        "REFERER_ENABLED": False,
        "RETRY_ENABLED": False,
        "CONCURRENT_REQUESTS":  15,
    }

    def parse(self, response):
        res_text = response.text
        res_url = response.url
        realtor_list_page_item = RealtorListPageJsonItem()
        realtor_list_page_item['jsonData'] = res_text


        json_res_listings = json.loads(res_text)['listings']

        offset = int(re.findall(r'offset=(.*)&limit', res_url)[0])
        county_name = re.findall(r'county=(.*)&state_code', res_url)[0]
        state_code = re.findall(r'state_code=(.*)&sort=relevance', res_url)[0]
        if len(json_res_listings) != 0:
            yield realtor_list_page_item
            next_url = 'https://mapi-ng.rdc.moveaws.com/api/v1/properties?offset={}&limit=200&county={}&state_code={}&sort=relevance&schema=mapsearch&client_id=rdc_mobile_native%2C9.4.2%2Candroid'.format(offset+200,county_name,state_code)
            yield scrapy.Request(url=next_url,callback=self.parse)




