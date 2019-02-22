from AmericanRealEstate.crawl_tools import get_psql_con


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
	WHERE  rl."propertyId" is NOT null
	 and rl."lastUpdate" is NOT NULL
	 and rl.address is NOT NULL
'''

# results1 = cursor1.execute(realtor_split_property_id_sql_str)
results2 = cursor2.execute(realtor_update_property_id_sql_str)
# conn.commit()
# print(results2)
# j=0

sql_string1 = '''
UPDATE
realtor_detail_page_json rj
set
"isDirty" = '0', "lastUpdate" = tmp."lastUpdate", address = tmp.address
FROM(
values
'''


sql_string2 = '''
 ) as tmp("propertyId", "lastUpdate")
 WHERE rj."propertyId" =tmp."propertyId"
'''

sql_string3 = ','.join([str(x) for x in cursor2.fetchall()])

final_string = sql_string1+sql_string3+sql_string2
print(final_string)

cursor1.execute(final_string)
conn.commit()




# for i in cursor2.fetchall():
#     # if i[0] !=i[3] or i[1] !=i[4] or i[2] !=i[5]:
#     tem_string = i
#     sql_string3 += str(i)
#     print(sql_string3)

print(sql_string3)

    # print(realtor_split_property_id_sql_str)
    # print(j)
    # j += 1
    # cursor1.execute(realtor_split_property_id_sql_str,(i[1],i[2],i[3]))
# conn.commit()

    # print(type(i))
    # for j in cursor2.fetchall():
    #     if i[0] in j:
    #         pass


# for i in cursor2.fetchall():
#     print(i)

# a = ('8135443778', '2019-02-07T20:29:24Z', '3725 Church St in Carver Park, Galveston, 77550')
#
# b = (1,3,4)
# print(a==b)

# ('4888990301', '2019-02-17T10:20:28Z', '4851 Hanoverville Rd, Bethlehem, 18020', '4888990301', '2019-02-12T09:55:00Z', '4851 Hanoverville Rd, Lower Nazareth Township, 18020')
# ('4888990301', '2019-02-12T09:55:00Z', '4851 Hanoverville Rd, Lower Nazareth Township, 18020', '4888990301', '2019-02-17T10:20:28Z', '4851 Hanoverville Rd, Bethlehem, 18020')
# ('7564433759', '2019-02-13T20:55:39Z', '406 Madrone Ln, Princeton, 75407', '7564433759', '2019-02-14T01:00:09Z', '406 Madrone Ln, Princeton, 75407')
# ('7564433759', '2019-02-14T01:00:09Z', '406 Madrone Ln, Princeton, 75407', '7564433759', '2019-02-13T20:55:39Z', '406 Madrone Ln, Princeton, 75407')
# ('1739576600', '2019-02-15T08:49:23Z', '10410 W Aztec Dr, Sun City, 85373', '1739576600', '2019-02-15T08:49:23Z', '10410 W Aztec Dr, Sun City, 873')


# fields = ('w', 'w2', 'w3')
# sql = "update tablename set "
# sql += ", ".join(["%s=%%s" % f for f in fields])
# sql += " where .."
# print(sql)
# update tablename set w=%s, w2=%s, w3=%s where ..
# curr.execute(sql, l1)


# update test set info=tmp.info from (values (1,'new1'),(2,'new2'),(6,'new6')) as tmp (id,info) where test.id=tmp.id

# sql = 'update '

# fields = ('w', 'w2', 'w3')
# values = (1, 2, 3)
# sql = "update tablename set "
# sql += ", ".join(["%s='%s'" % f for f in zip(fields, values)])
# sql += " where .."
# print(sql)
# update tablename set w='1', w2='2', w3='3' where ..
# curr.execute(sql)



