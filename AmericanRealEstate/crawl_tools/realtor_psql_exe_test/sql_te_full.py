from AmericanRealEstate.crawl_tools import get_psql_con
import re


conn = get_psql_con.get_psql_con()

# cursor1 = conn.cursor()
# cursor2 = conn.cursor()

# realtor_update_property_id_sql_str = '''
# SELECT
# 	rl."propertyId" AS "listPropertyId",
# 	rl."lastUpdate" AS "listLastUpdate",
# 	rl.address AS "listAddress"
# FROM
# 	realtor_list_page_json_splite rl
# 	INNER JOIN realtor_detail_page_json rd ON rl."propertyId" = rd."propertyId"
# 	WHERE rl."lastUpdate"!=rd."lastUpdate"
# 	OR rl.address!=rd.address
# '''
#
# # 获取需要更新的数据
# results2 = cursor2.execute(realtor_update_property_id_sql_str)
# print(cursor2.rowcount)
# print(len(cursor2.fetchall()))


# # 批量更新数据
# sql_string1 = '''
# UPDATE
# realtor_detail_page_json rj
# set
# "isDirty" = '0', "lastUpdate" = tmp."lastUpdate", address = tmp.address
# FROM(
# values
# '''
#
# sql_string2 = '''
#  ) as tmp("propertyId", "lastUpdate",address)
#  WHERE rj."propertyId" =tmp."propertyId"
# '''
#
# sql_string3_list= []
# j = 1
# batch_size = 10
# update_count = len(cursor2.fetchall())

# for i in cursor2.fetchall():
#     print("跟新"+str(i))
#     if len(re.findall(r"'", i[2])) > 0:
#         # print(i[2])
#         i = list(i)
#         i[2] = i[2].replace("'", "''")
#         i = tuple(i)
#         i = str(i)
#         i = i.replace('"', "'")
#     i = str(i)
#     sql_string3_list.append(i)
#     if len(sql_string3_list) ==batch_size:
#         sql_string3 = ','.join(sql_string3_list)
#         final_string = sql_string1 + sql_string3 + sql_string2
#         print(final_string)
#         cursor1.execute(final_string)
#         conn.commit()


# for i in cursor2.fetchall():
#     # print("跟新"+str(i))
#     if len(re.findall(r"'", i[2])) > 0:
#         # print(i[2])
#         i = list(i)
#         i[2] = i[2].replace("'", "''")
#         i = tuple(i)
#         i = str(i)
#         i = i.replace('"', "'")
#     i = str(i)
#     print(i)
#     sql_string3_list.append(i)
#     if len(sql_string3_list) == 10:
#         sql_string3 = ','.join(sql_string3_list)
#         final_string = sql_string1 + sql_string3 + sql_string2
#         print(final_string)
#         cursor1.execute(final_string)
#         conn.commit()
#         sql_string3_list=[]




# for i in cursor2.fetchall():
#     print(i)

# sql_string3_list= []
# j = 1
# batch_size = 10
# update_count = len(cursor2.fetchall())
# update_batch = update_count/batch_size
# remainder = update_count%batch_size

# for i in cursor2.fetchall():
#     if update_count<=batch_size:
#         print("跟新"+str(i))
#         if len(re.findall(r"'", i[2])) > 0:
#             # print(i[2])
#             i = list(i)
#             i[2] = i[2].replace("'", "''")
#             i = tuple(i)
#             i = str(i)
#             i = i.replace('"', "'")
#         i = str(i)
#         sql_string3_list.append(i)
#         if len(sql_string3_list) ==update_count:
#             sql_string3 = ','.join(sql_string3_list)
#             final_string = sql_string1 + sql_string3 + sql_string2
#             print(final_string)
#             cursor1.execute(final_string)
#             conn.commit()
#     else:
#         if remainder ==0:
#             if len(re.findall(r"'",i[2])) >0:
#                 # print(i[2])
#                 i = list(i)
#                 i[2] = i[2].replace("'","''")
#                 i = tuple(i)
#                 i = str(i)
#                 i = i.replace('"',"'")
#             i = str(i)
#
#             sql_string3_list.append(i)
#             if len(sql_string3_list)==batch_size:
#                 print('第'+str(j)+'次执行更新')
#                 j +=1
#                 sql_string3 = ','.join(sql_string3_list)
#                 final_string = sql_string1 + sql_string3 + sql_string2
#                 print(final_string)
#                 cursor1.execute(final_string)
#                 conn.commit()
#                 sql_string3_list = []
#         else:
#             if len(re.findall(r"'", i[2])) > 0:
#                 # print(i[2])
#                 i = list(i)
#                 i[2] = i[2].replace("'", "''")
#                 i = tuple(i)
#                 i = str(i)
#                 i = i.replace('"', "'")
#             i = str(i)
#
#             sql_string3_list.append(i)
#             if len(sql_string3_list) == batch_size:
#                 print('第' + str(j) + '次执行更新')
#                 j += 1
#                 sql_string3 = ','.join(sql_string3_list)
#                 final_string = sql_string1 + sql_string3 + sql_string2
#                 print(final_string)
#                 cursor1.execute(final_string)
#                 conn.commit()
#                 sql_string3_list = []
#
#             if j==update_batch+1 and len(sql_string3_list)==remainder:
#                 sql_string3 = ','.join(sql_string3_list)
#                 final_string = sql_string1 + sql_string3 + sql_string2
#                 print(final_string)
#                 cursor1.execute(final_string)
#                 conn.commit()
#
#
#


def update_detail_data(conn, time):
    print('更新detail表的数据')
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    realtor_update_property_id_sql_str = '''
    SELECT
    	rl."propertyId" AS "listPropertyId",
    	rl."lastUpdate" AS "listLastUpdate",
    	rl.address AS "listAddress"
    FROM
    	realtor_list_page_json_splite rl
    	INNER JOIN realtor_detail_page_json rd ON rl."propertyId" = rd."propertyId"
    	WHERE rl."lastUpdate"!=rd."lastUpdate"
    	OR rl.address!=rd.address
    '''

    # 获取需要更新的数据
    results2 = cursor2.execute(realtor_update_property_id_sql_str)

    # 批量更新数据
    sql_string1 = '''
    UPDATE
    realtor_detail_page_json rj
    set
    "isDirty" = '0', "lastUpdate" = tmp."lastUpdate", address = tmp.address
    FROM(
    values
    '''

    sql_string2 = '''
     ) as tmp("propertyId", "lastUpdate",address)
     WHERE rj."propertyId" =tmp."propertyId"
    '''
    sql_string3_list = []
    j = 1
    if time == 1:
        print("第{}次更新，更新了：{}".format(time, cursor2.rowcount))
        batch_size = 100
    if time == 2:
        batch_size = cursor2.rowcount
        print("第2次更新，更新了：{}条".format(cursor2.rowcount))

    for i in cursor2.fetchall():
        print("跟新"+str(j))
        j +=1
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



def splite_list_data(conn):
    print("拆分list data 数据到split 表里面")
    cursor = conn.cursor()
    sql_string_splite = '''
        INSERT INTO realtor_list_page_json_splite ( "propertyId", "lastUpdate", address, "optionDate" ) (
        SELECT DISTINCT ON
            ( n_table."propertyId" ) n_table."propertyId",
            n_table."lastUpdate",
            n_table.address,
            n_table."optionDate" 
        FROM
            (
            SELECT
                to_number( json_array_elements ( "jsonData" -> 'listings' ) ->> 'property_id', '9999999999' ) AS "propertyId",
                json_array_elements ( "jsonData" -> 'listings' ) ->> 'last_update' AS "lastUpdate",
                json_array_elements ( "jsonData" -> 'listings' ) ->> 'address' AS address,
                now() AS "optionDate" 
            FROM
                realtor_list_page_json 
            ) n_table 
        WHERE
            n_table."propertyId" IS NOT NULL 
            AND n_table."lastUpdate" IS NOT NULL 
        AND n_table.address IS NOT NULL 
        )
    '''
    cursor.execute(sql_string_splite)
    conn.commit()



def insert_detail_data(conn):
    print("将detail没有的propertyId进行插入")
    cursor = conn.cursor()
    sql_string_insert = '''
        INSERT INTO realtor_detail_page_json( "propertyId", "lastUpdate", address,"isDirty","optionDate")
    (SELECT
        rl."propertyId" AS "listPropertyId",
        rl."lastUpdate" AS "listLastUpdate",
        rl.address AS "listAddress",
        0,
        now()
    FROM
        realtor_list_page_json_splite rl
        left JOIN realtor_detail_page_json rd ON rl."propertyId" = rd."propertyId"
        WHERE 
        rd."propertyId" is NULL 
        and rl."propertyId" is NOT null
         and rl."lastUpdate" is NOT NULL
         and rl.address is NOT NULL
        )
    '''
    cursor.execute(sql_string_insert)
    conn.commit()




# 将realtor_list_json表中的数据拆分开,并删除空的情况
# splite_list_data(conn)
# 找到有的propertyId 并且lastUpate和address字段改变了的，这里应该使用批量更新
update_detail_data(conn,1)
update_detail_data(conn,2)
# 找到detail_page_json 表中没有的propertyId，并将它插入到该表中；
# insert_detail_data(conn)
conn.close()
print('完成sql插入---------------------------------------------')