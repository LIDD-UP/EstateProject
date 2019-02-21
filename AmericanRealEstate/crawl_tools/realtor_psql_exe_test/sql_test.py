from AmericanRealEstate.crawl_tools import get_psql_con


conn = get_psql_con.get_psql_con()

cursor1 = conn.cursor()
realtor_split_property_id_sql_str = '''
    select "propertyId","lastUpdate","address" from realtor_list_page_json_splite
'''

cursor2 = conn.cursor()
realtor_update_property_id_sql_str = '''
    SELECT
	rl."propertyId" AS "listPropertyId",
	rl."lastUpdate" AS "listLastUpdate",
	rl.address AS "listAddress",
	rd."propertyId" AS "detailPropertyId",
	rd."lastUpdate" AS "detailLastUpdate",
	rd.address AS "detailAddress" 
FROM
	realtor_list_page_json_splite rl
	INNER JOIN realtor_detail_page_json rd ON rl."propertyId" = rd."propertyId"
'''

# results1 = cursor1.execute(realtor_split_property_id_sql_str)
results2 = cursor2.execute(realtor_update_property_id_sql_str)
for i in cursor2.fetchall():
    if i[0] !=i[3] or i[1] !=i[4] or i[2] !=i[5]:
        print(i)

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

('4888990301', '2019-02-17T10:20:28Z', '4851 Hanoverville Rd, Bethlehem, 18020', '4888990301', '2019-02-12T09:55:00Z', '4851 Hanoverville Rd, Lower Nazareth Township, 18020')
('4888990301', '2019-02-12T09:55:00Z', '4851 Hanoverville Rd, Lower Nazareth Township, 18020', '4888990301', '2019-02-17T10:20:28Z', '4851 Hanoverville Rd, Bethlehem, 18020')
('7564433759', '2019-02-13T20:55:39Z', '406 Madrone Ln, Princeton, 75407', '7564433759', '2019-02-14T01:00:09Z', '406 Madrone Ln, Princeton, 75407')
('7564433759', '2019-02-14T01:00:09Z', '406 Madrone Ln, Princeton, 75407', '7564433759', '2019-02-13T20:55:39Z', '406 Madrone Ln, Princeton, 75407')
('1739576600', '2019-02-15T08:49:23Z', '10410 W Aztec Dr, Sun City, 85373', '1739576600', '2019-02-15T08:49:23Z', '10410 W Aztec Dr, Sun City, 873')
