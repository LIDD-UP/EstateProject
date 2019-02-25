from AmericanRealEstate.crawl_tools import get_psql_con
import re


conn = get_psql_con.get_psql_con()

cursor1 = conn.cursor()
realtor_split_property_id_sql_str = '''
     UPDATE realtor_detail_page_json set "isDirty"='1'
      WHERE "propertyId" ='6264702487'
'''

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

'''

'''

results2 = cursor2.execute(realtor_update_property_id_sql_str)


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


sql_string3_list= []
j = 1
update_count = len(cursor2.fetchall())
for i in cursor2.fetchall():
    if len(re.findall(r"'",i[2])) >0:
        # print(i[2])
        i = list(i)
        i[2] = i[2].replace("'","''")
        i = tuple(i)
        i = str(i)
        i = i.replace('"',"'")
    i = str(i)

    sql_string3_list.append(i)
    if len(sql_string3_list)>10:
        print('第'+str(j)+'次执行更新')
        j +=1
        sql_string3 = ','.join(sql_string3_list)
        final_string = sql_string1 + sql_string3 + sql_string2
        print(final_string)
        cursor1.execute(final_string)
        conn.commit()
        sql_string3_list = []
    if j==1 or (j==update_count+1 and update_count %10 !=0 and len(sql_string3_list)==(update_count %10)):
        sql_string3 = ','.join(sql_string3_list)
        final_string = sql_string1 + sql_string3 + sql_string2
        print(final_string)
        cursor1.execute(final_string)
        conn.commit()






