# -*- coding: utf-8 -*-
import scrapy


class TruliaStateCountyZipSpider(scrapy.Spider):
    name = 'trulia_state_county_zip'
    allowed_domains = ['trulia.com']
    start_urls = ['https://www.trulia.com/sitemap/']

    def parse(self, response):
        states = response.css('.real-estate-markets li')
        for state in states:
            print(state)

    def parse_counties(self, response):
        pass