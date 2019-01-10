# -*- coding: utf-8 -*-
import re

import scrapy
from urllib.parse import urljoin

from AmericanRealEstate.items import StateNameCountyNameItem,CountyNameZipCodeItem


class TruliaStateCountyZipSpider(scrapy.Spider):
    name = 'trulia_state_county_zip'
    allowed_domains = ['trulia.com']
    # 这里的custom_settings可能没有起作用，
    start_urls = ['https://www.trulia.com/sitemap/']


    def parse(self, response):
        # states = response.text
        # with open('./test.html','w') as f:
        #     f.write(states)
        states = response.css('.real-estate-markets li a')
        # 获取详情页的连接

        for state in states:
            states_real_estate_urls = state.css('::attr(href)').extract_first()
            # print(states_real_estate_urls)
            # states_name = state.css('::text').extract_first()
            # print(states_name)
            next_url = urljoin(response.url,states_real_estate_urls)
            # print(next_url)
            # print(state.replace(' real estate',''))
            yield scrapy.Request(url=next_url,callback=self.parse_counties)

    def parse_counties(self, response):
        counties = response.css('.all-counties-sitemap-links li a')
        state_county_item = StateNameCountyNameItem()
        for county in counties:
            states_real_estate_urls = county.css('::attr(href)').extract_first()
            # print(states_real_estate_urls)
            county_name = county.css('::text').extract_first()
            state_county_item['county'] = county_name
            if len(re.findall(r'County',county_name)) != 0:
                true_county_name = county_name.replace(' County', '')
            if len(re.findall(r'Parish',county_name)) != 0:
                true_county_name = county_name.replace(' Parish', '')
            if len(re.findall(r'Borough',county_name)) != 0:
                true_county_name = county_name.replace(' Borough', '')

            # print(true_county_name)
            state_name = re.findall(r'sitemap/(.*)-real-estate',response.url)[0].replace('-',' ')
            state_county_item['stateName'] = state_name
            state_county_item['countyName'] = true_county_name
            yield state_county_item

            next_url = urljoin(response.url, states_real_estate_urls)
            # print(next_url)
            # print(state.replace(' real estate',''))
            yield scrapy.Request(url=next_url, callback=self.parse_zipcode)

    def parse_zipcode(self,response):
        zip_codes = response.css('.all-zip-codes-sitemap-links li a')
        county_zip_item = CountyNameZipCodeItem()
        for zip_code in zip_codes:
            zip_number = zip_code.css('::text').extract_first()
            if len(re.findall(r'County',response.url)) != 0:
                county_name = re.findall(r'real-estate/(.*)-County',response.url)[0].replace('-',' ')
            if len(re.findall(r'Parish',response.url)) !=0:
                county_name = re.findall(r'real-estate/(.*)-Parish', response.url)[0].replace('-', ' ')
            if len(re.findall(r'Borough',response.url)) !=0:
                county_name = re.findall(r'real-estate/(.*)-Borough', response.url)[0].replace('-', ' ')
            county_zip_item['countyName'] = county_name
            county_zip_item['zipCode'] = zip_number
            yield county_zip_item
