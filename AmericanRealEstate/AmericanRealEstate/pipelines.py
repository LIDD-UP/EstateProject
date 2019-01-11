# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from AmericanRealEstate.items import StateNameCountyNameItem,CountyNameZipCodeItem,RealtorHouseInfoJsonItem
from tools.get_sql_con import get_sql_con


class AmericanrealestatePipeline(object):
    def process_item(self, item, spider):
        return item


class StateNameCountyNamePipeline(object):
    def __init__(self):
        self.conn = get_sql_con()

    def process_item(self, item, spider):
        if isinstance(item,StateNameCountyNameItem):
            cursor = self.conn.cursor()
            cursor.execute(
                '''
                insert into state_county(stateName,countyName,county) values(%s,%s,%s)
                ''', [item['stateName'], item['countyName'],item['county']
                      ]
            )
        self.conn.commit()
        return item


class CountyZipCodePipeline(object):
    def __init__(self):
        self.conn = get_sql_con()

    def process_item(self, item, spider):
        if isinstance(item,CountyNameZipCodeItem):
            cursor = self.conn.cursor()
            cursor.execute(
                '''
                insert into county_zip_code(countyName,zipCode) values(%s,%s)
                ''', [item['countyName'], item['zipCode']
                      ]
            )
        self.conn.commit()
        return item


class RealtorHouseInfoPipeline(object):
    def __init__(self):
        self.conn = get_sql_con()

    def process_item(self, item, spider):
        if isinstance(item,RealtorHouseInfoJsonItem):
            cursor = self.conn.cursor()
            cursor.execute(
                '''
                insert into realtor_house_json_data(houseData) values(%s)
                ''', [item['houseData']
                      ]
            )
        self.conn.commit()
        return item