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



def update_detail_data(conn,time):
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
    if time==1:
        batch_size=100
    if time==2:
        batch_size = cursor2.rowcount

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
        print(i)
        sql_string3_list.append(i)
        if len(sql_string3_list) == batch_size:
            sql_string3 = ','.join(sql_string3_list)
            final_string = sql_string1 + sql_string3 + sql_string2
            print(final_string)
            cursor1.execute(final_string)
            conn.commit()
            sql_string3_list = []




update_detail_data(conn,1)