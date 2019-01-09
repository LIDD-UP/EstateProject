# -*- coding: utf-8 -*-
import scrapy


class TruliaSpider(scrapy.Spider):
    name = 'trulia'
    allowed_domains = ['trulia.com']
    start_urls = ['http://trulia.com/']

    def parse(self, response):
        pass
