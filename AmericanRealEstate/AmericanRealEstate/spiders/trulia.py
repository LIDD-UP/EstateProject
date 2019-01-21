# -*- coding: utf-8 -*-
import re
import scrapy
from urllib.parse import urljoin

from AmericanRealEstate.settings import trulia_search_criteria
from AmericanRealEstate.items import TruliaHouseInfoItem



class TruliaSpider(scrapy.Spider):
    name = 'trulia'
    allowed_domains = ['trulia.com']
    start_urls = ['https://www.trulia.com/County/NY/New_York_Real_Estate/']

    def parse(self, response):
            houses = response.xpath("//div[@class='backgroundControls']//div[@class='containerFluid']/ul//li[contains(@class,'xsCol12Landscape')]")
            for house in houses:
                detail_url = house.xpath(".//a[@class='tileLink']/@href").extract_first()
                true_detail_url = urljoin(response.url,detail_url)
                print(true_detail_url)

                yield scrapy.Request(url=true_detail_url,callback=self.parse_content)

            next_page_url = response.xpath("//span[@class='next ']/a[@class='next']/@href").extract_first()
            if next_page_url is not None:
                true_next_page_url = urljoin(response.url,next_page_url)
                yield scrapy.Request(url=true_next_page_url, callback=self.parse)

    def parse_content(self,response):

        trulia_house_info_item = TruliaHouseInfoItem()
        yield trulia_house_info_item
