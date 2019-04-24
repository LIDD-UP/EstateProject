# -*- coding: utf-8 -*-
import scrapy


class RealtorWebAppMergeByPropertySpider(scrapy.Spider):
    name = 'realtor_web_app_merge_by_property'
    allowed_domains = ['reator.com']
    start_urls = ['http://reator.com/']

    def parse(self, response):
        pass
