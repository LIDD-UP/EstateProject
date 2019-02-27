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


class TruliaHouseInfoItem(scrapy.Item):
    price = scrapy.Field()
    pass


class RealtorDetailDomItem(scrapy.Item):
    price = scrapy.Field()
    address = scrapy.Field()
    bedrooms = scrapy.Field()
    bath = scrapy.Field()
    zipCode = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()


class SearchCriteriaItem(scrapy.Item):
    stateName = scrapy.Field()
    fullCountyName = scrapy.Field()
    countyName = scrapy.Field()
    zipCode = scrapy.Field()


class StatisticRealtorHouseCountItem(scrapy.Item):
    county = scrapy.Field()
    count = scrapy.Field()


class RealtorPropertyIdItem(scrapy.Item):
    propertyId = scrapy.Field()


class RealtorListPageJsonItem(scrapy.Item):
    jsonData = scrapy.Field()


class RealtorDetailPageJsonItem(scrapy.Item):
    detailJson =scrapy.Field()
    propertyId = scrapy.Field()


class RealtorDetailPageJsonWebItem(scrapy.Item):
    detailJson =scrapy.Field()
    propertyId = scrapy.Field()


