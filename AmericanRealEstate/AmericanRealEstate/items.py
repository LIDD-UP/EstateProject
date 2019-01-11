# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmericanrealestateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class StateNameCountyNameItem(scrapy.Item):
    stateName = scrapy.Field()
    countyName = scrapy.Field()
    county = scrapy.Field()


class CountyNameZipCodeItem(scrapy.Item):
    countyName = scrapy.Field()
    zipCode = scrapy.Field()


class RealtorHouseInfoJsonItem(scrapy.Item):
    houseData = scrapy.Field()
