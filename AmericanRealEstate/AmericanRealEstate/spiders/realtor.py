# -*- coding: utf-8 -*-
import scrapy


class RealtorSpider(scrapy.Spider):
    name = 'realtor'
    allowed_domains = ['realtor.com']
    start_urls = ['https://www.realtor.com/realestateandhomes-search/New-York_NY']

    def parse(self, response):
        pass
