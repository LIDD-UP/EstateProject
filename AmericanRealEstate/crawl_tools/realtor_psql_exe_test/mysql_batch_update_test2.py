# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: mysql_batch_update_test2.py
@time: 2019/3/1
"""
from AmericanRealEstate.crawl_tools.get_sql_con import get_sql_con
import re


conn = get_sql_con()


def update_detail_data(conn, time, batch_size):
    print("更新detail数据")
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    realtor_update_property_id_sql_str = '''
        SELECT
            rl.propertyId AS listPropertyId,
            rl.lastUpdate AS listLastUpdate,
            rl.address AS listAddress 
        FROM
            realtor_list_page_json_splite rl
            INNER JOIN realtor_detail_page_json rd ON rl.propertyId = rd.propertyId
        WHERE
            rl.lastUpdate != rd.lastUpdate
            OR rl.address != rd.address
    '''

    # 获取需要更新的数据
    results2 = cursor2.execute(realtor_update_property_id_sql_str)

    # 批量更新数据
    sql_string1 = '''
        UPDATE
          realtor_detail_page_json rj
        set
          isDirty = '1', lastUpdate = %s, address = %s,optionDate=now()
        WHERE rj.propertyId =%s
    '''
    sql_string3_list = []
    if time == 1:
        print('第一次更新跟新了{}'.format(cursor2.rowcount))
        batch_size = batch_size
    if time == 2:
        batch_size = cursor2.rowcount
        print('第2次更新跟新了{}'.format(cursor2.rowcount))

    for i in cursor2.fetchall():
        print(i)
        sql_string3_list.append([i[1],i[2],i[0]])
        if len(sql_string3_list) == batch_size:
            cursor1.executemany(sql_string1,sql_string3_list)
            conn.commit()
            sql_string3_list = []


update_detail_data(conn,2,100)


