# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: mysql_batch_update_test.py
@time: 2019/2/28
"""
import re
from AmericanRealEstate.crawl_tools.get_sql_con import get_sql_con


def update_detail_data(self, conn, time):
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
    isDirty = '0', lastUpdate = tmp.lastUpdate, address = tmp.address
    FROM(
    values
    '''

    sql_string2 = '''
     ) as tmp(propertyId, lastUpdate,address)
     WHERE rj.propertyId =tmp.propertyId
    '''
    sql_string3_list = []
    j = 1
    if time == 1:
        print('第一次更新跟新了{}'.format(cursor2.rowcount))
        batch_size = 100
    if time == 2:
        batch_size = cursor2.rowcount
        print('第2次更新跟新了{}'.format(cursor2.rowcount))

    for i in cursor2.fetchall():
        # print("跟新"+str(i))
        if len(re.findall(r"'", i[2])) > 0:
            # print(i[2])
            i = list(i)
            i[2] = i[2].replace("'", "''")
            i = tuple(i)
            i = str(i)
            i = i.replace('"', "'")
        i = str(i)
        # print(i)
        sql_string3_list.append(i)
        if len(sql_string3_list) == batch_size:
            sql_string3 = ','.join(sql_string3_list)
            final_string = sql_string1 + sql_string3 + sql_string2
            # print(final_string)
            cursor1.execute(final_string)
            conn.commit()
            sql_string3_list = []


# conn = get_sql_conn()
#
# update_detail_data(conn,2)



# 构造mysql批量跟新语句：

sql = '''
    UPDATE
    realtor_detail_page_json rj
    set
    isDirty = '0', 
    optionDate=now(),
    lastUpdate = CASE id 
        WHEN 1 THEN 3  
    END, 
    address = CASE id 
        WHEN 1 THEN 'New Title 1'
        WHEN 2 THEN 'New Title 2'
        WHEN 3 THEN 'New Title 3'
    END
WHERE id IN (1,2,3)

'''

sql_1 = '''
UPDATE
    realtor_detail_page_json rj
    set
    isDirty = '0',
    optionDate=now()
     lastUpdate = CASE id 
'''

sql2 = ''

for i in range(10):
    str_tmp = "when {}".format(i)+"then {}".format(i)+'\n'
    sql2 += str_tmp

print(sql2)
