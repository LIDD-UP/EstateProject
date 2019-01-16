# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import pymysql

from AmericanRealEstate.items import StateNameCountyNameItem,CountyNameZipCodeItem,RealtorHouseInfoJsonItem
from tools.get_sql_con import get_sql_con
from tools.test_file import post_url


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


'''
当item插入速度跟不上页面的解析速度的时候，普通的mysql插入方式并不好：

所以twisted提供了一个连接池的概念：

可以异步的插入数据；
twisted本身是没有连接池的，但是它提供了一个异步的机制；
用的连接池还是对应数据库的连接池；
但是存在一个问题就是不知道是否可以通过ssh连接；
算了不搞了；
'''

class MysqlTwistedPipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool
    # scrapy有一个特点，让我们定义一个静态方法的时候，可以传入一些scrapy的对象，通过这些对象获取一些数据；
    # 通过函数也可以，这里是通过函数来调用的，而且函数名称是固定的；
    @staticmethod
    def from_settings(cls,settings):
        # python 可变化参数：变成dict传值：
        dbparms = dict(
        host=settings['MYSQL_PORT'],
        db=settings['MYSQL_DBNAME'],
        user = settings['MYSQL_USER'],
        passwd = settings['MYSQL_PASSWORD'],
        charset = 'utf8',
        cursorclass = pymysql.cursors.DictCursor,
        use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb",**dbparms)
        # 这里相当于实例化这个pipeline，然后给这个pipeline传入一个dbpool，所以init方法需要接受这个参数；
        return cls(dbpool)

    def process_item(self, item, spider):
        if isinstance(item,RealtorHouseInfoJsonItem):
            # 使用twisted将mysql插入变成异步执行；
            query = self.dbpool.runInteraction(self.do_insert,item)
            # 错误处理函数
            query.addErrback(self.handle_error,item,spider)

    def handle_error(self,failure,item,spider):
        print(failure)


    def do_insert(self,cursor,item):
        # 执行具体的插入
        cursor.execute(
            '''
            insert into realtor_house_json_data(houseData) values(%s)
            ''', [item['houseData']
                  ]
        )


class RealtorHouseInfoTestPipeline(object):
    house_list = []

    def process_item(self, item, spider):
        if isinstance(item,RealtorHouseInfoJsonItem):
            self.house_list.append(str(item['houseData']))
            if len(self.house_list) >= 3:
                print('数据显示',self.house_list)
                post_data = {
                    "data": self.house_list
                }
                result = post_url('http://192.168.0.126:8080/America-DataSave/index/saveRealtorDataJson/', post_data)
                print(result == 'success')

                del self.house_list[:]
        return item