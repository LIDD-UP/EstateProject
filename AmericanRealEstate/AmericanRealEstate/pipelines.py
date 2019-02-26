# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import pymysql

from AmericanRealEstate.items import StateNameCountyNameItem,CountyNameZipCodeItem,RealtorHouseInfoJsonItem,RealtorDetailDomItem,TruliaHouseInfoItem,SearchCriteriaItem,StatisticRealtorHouseCountItem,RealtorPropertyIdItem,RealtorListPageJsonItem
from AmericanRealEstate.items import RealtorListPageJsonItem,RealtorDetailPageJsonItem
from crawl_tools.get_sql_con import get_sql_con
from crawl_tools.get_psql_con import get_psql_con
from crawl_tools.test_file import post_url
from AmericanRealEstate.settings import post_interface_url



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


class SearchCriteriaPipeline(object):
    def __init__(self):
        self.conn = get_sql_con()

    def process_item(self, item, spider):
        if isinstance(item,SearchCriteriaItem):
            cursor = self.conn.cursor()
            cursor.execute(
                '''
                insert into search_criteria(stateName,countyName,fullCountyName,zipCode) values(%s,%s,%s,%s)
                ''', [item['stateName'] ,item['countyName'] ,item['fullCountyName'] ,item['zipCode'] ,
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
                insert into realtor_house_json_data_new_4(houseData) values(%s)
                ''', [item['houseData']
                      ]
            )
        self.conn.commit()
        return item


class RealtorRealtorPropertyIdPipeline(object):
    def __init__(self):
        self.conn = get_sql_con()

    def process_item(self, item, spider):
        if isinstance(item,RealtorPropertyIdItem):
            cursor = self.conn.cursor()
            cursor.execute(
                '''
                insert into realtor_property_id(propertyId) values(%s)
                ''', [item['propertyId']
                      ]
            )
        self.conn.commit()
        return item


class RealtorListPageJsonPipeline(object):
    def __init__(self):
        self.conn = get_sql_con()

    def process_item(self, item, spider):
        if isinstance(item,RealtorListPageJsonItem):
            cursor = self.conn.cursor()
            cursor.execute(
                '''
                insert into realtor_list_page_json(jsonData) values(%s)
                ''', [item['jsonData']
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
                result = post_url(post_interface_url, post_data)
                print(result == 'success')

                del self.house_list[:]
        return item


class RealtorDetailDomPipeline(object):
    def __init__(self):
        self.conn = get_sql_con()

    def process_item(self, item, spider):
        if isinstance(item, RealtorDetailDomItem):
            cursor = self.conn.cursor()
            cursor.execute(
                '''
                insert into realtor_detail_dom(price) values(%s)
                ''', [item['price']
                      ]
            )
        self.conn.commit()
        return item


class TruliaDetailDomPipeline(object):
    def __init__(self):
        self.conn = get_sql_con()

    def process_item(self, item, spider):
        if isinstance(item, TruliaHouseInfoItem):
            cursor = self.conn.cursor()
            cursor.execute(
                '''
                insert into trulia_detail_dom(price) values(%s)
                ''', [item['price']
                      ]
            )
        self.conn.commit()
        return item


class StatisticRealtorHouseCountPipeline(object):
    def __init__(self):
        self.conn = get_sql_con()

    def process_item(self, item, spider):
        if isinstance(item, StatisticRealtorHouseCountItem):
            cursor = self.conn.cursor()
            cursor.execute(
                '''
                insert into realtor_count(realtor_count) values(%s)
                ''', [item['count']
                      ]
            )
        self.conn.commit()
        return item




# realtor postgresql pipeline

class RealtorListPagePsqlPipeline(object):
    def __init__(self):
        self.conn = get_psql_con()

    def process_item(self, item, spider):
        if isinstance(item,RealtorListPageJsonItem):
            cursor = self.conn.cursor()
            cursor.execute(
                '''
                insert into realtor_list_page_json("jsonData","optionDate") values(%s,now())
                ''', [item['jsonData']
                      ]

            )
        self.conn.commit()
        return item


# UPDATE realtor_detail_page_json set "detailJson"=%s ,"isDirty"='0',optionDate=now()
#  WHERE "propertyId" =%s

class RealtordetailPagePsqlPipeline(object):
    sql_string1 = '''
    UPDATE
    realtor_detail_page_json rj
    set
    "detailJson"=tmp."detailJson" ,"isDirty"='0',"optionDate"=now()
    FROM(
    values
    '''

    sql_string2 = '''
     ) as tmp("propertyId", "detailJson")
     WHERE rj."propertyId" =tmp."propertyId"
    '''
    sting3_list = []
    def __init__(self):
        self.conn = get_psql_con()



    def process_item(self, item, spider):
        if isinstance(item,RealtorDetailPageJsonItem):
            cursor = self.conn.cursor()


            cursor.execute(
                '''
                  UPDATE realtor_detail_page_json set "detailJson"=%s ,"isDirty"='0',"optionDate"=now()
                  WHERE "propertyId" =%s
                ''', [item['detailJson'], item['propertyId']
                      ]

            )
        self.conn.commit()

        return item






