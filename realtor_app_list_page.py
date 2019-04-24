# -*- coding: utf-8 -*-
import scrapy


class RealtorAppListPageSpider(scrapy.Spider):
    name = 'realtor_app_list_page'
    allowed_domains = ['mapi-ng.rdc.moveaws.com']
    start_urls = ['http://mapi-ng.rdc.moveaws.com/']

    def parse(self, response):
        pass
