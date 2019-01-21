# -*- coding: utf-8 -*-
import re

import scrapy
from urllib.parse import urljoin
from scrapy_redis.spiders import RedisSpider
import pandas as pd

from AmericanRealEstate.items import RealtorHouseInfoJsonItem, RealtorDetailDomItem
from AmericanRealEstate.settings import realtor_search_criteria, realtor_domain_url



class RealtorSpider(scrapy.Spider):
    name = 'realtor'
    allowed_domains = ['realtor.com']
    # redis_key = "realtor:start_urls"

    # start_urls = ['https://www.realtor.com/realestateandhomes-search/Adair-County_MO']
    start_urls = [url for url in realtor_search_criteria][0:1]


    custom_settings = {
        "ITEM_PIPELINES": {
            # 'AmericanRealEstate.pipelines.RealtorHouseInfoPipeline': 301,
            'AmericanRealEstate.pipelines.RealtorDetailDomPipeline': 302,
            # 'AmericanRealEstate.pipelines.RealtorHouseInfoTestPipeline': 302,
            # 'scrapy_redis.pipelines.RedisPipeline': 300

        },
        "DEFAULT_REQUEST_HEADERS": {
                "referer": "https://www.realtor.com/"
        },
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

    def parse(self, response):
        # css
        # houses = response.css('ul.prop-list li.js-quick-view')
        # xpath
        houses = response.xpath("//ul[contains(@class,'prop-list')]/li[contains(@class,'js-quick-view')]")
        # houses = [1,2,3,4,5]
        for house in houses:
            # print(house)
            # css
            # detail_url = house.css('.photo-wrap a::attr(href)').extract_first()
            # xpath
            detail_url = house.xpath(".//div[contains(@class,'photo-wrap')]/a/@href").extract_first()

            #
            # # 以防数据接口消失只能用
            true_detail_url = urljoin(realtor_domain_url, detail_url)
            print('true', true_detail_url)
            yield scrapy.Request(url=true_detail_url,callback=self.parse_content)

            # 使用接口方式获取数据
            # x = re.findall(r'(M\d{5}-\d{5})', detail_url)
            # if len(x) != 0:
            #     x = x[-1]
            #     x = x.replace('-', '')
            #     print(x)
            # next_detail_page_url = 'https://www.realtor.com/property-overview/{}'.format(x)
            # yield scrapy.Request(url=next_detail_page_url,callback=self.parse_content)

        next_page_url = response.xpath("//span[@class='next ']/a[@class='next']/@href").extract_first()
        if next_page_url is not None:
            true_next_page_url = urljoin(response.url,next_page_url)
            yield scrapy.Request(url=true_next_page_url, callback=self.parse)


    def parse_content(self,response):
        # 接口的parse
        # realtor_house_info_item = RealtorHouseInfoJsonItem()
        # realtor_house_info_item['houseData'] = response.text

        # 通过dom解析
        realtor_detail_dom_item = RealtorDetailDomItem()
        price = response.xpath("//span[contains(@itemprop,'price')]/text()").extract_first()
        print(price)
        realtor_detail_dom_item['price'] = price
        # address = response.xpath("//span[contains(@itemprop,'streetAddress')]/text()").extract_first()
        # bedrooms = response.xpath("'//ul[contains(@class,'property-meta')]//li[contains(@data-label,'property-meta-beds')]//span[contains(@class,'data-value')]")
        # bath = scrapy.Field()
        # zipCode = scrapy.Field()
        # city = scrapy.Field()
        # state = scrapy.Field()
        yield realtor_detail_dom_item

