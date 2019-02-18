import psycopg2
import json

from AmericanRealEstate.AmericanRealEstate import settings


def get_psql_con():
    mysql_con = psycopg2.connect(
        host=settings.PSQL_HOST,
        port=settings.PSQL_PROT,
        user=settings.PSQL_USER,
        password=settings.PSQL_PASSWORD,
        database=settings.PSQL_DBNAME,
        # charset='utf8',
    )
    return mysql_con


if __name__ == '__main__':
    dict_test ='{"li":"test"}'

    test_conn = get_psql_con()
    cursor = test_conn.cursor()
    print(test_conn)
    cursor.execute(
        '''
        insert into realtor_list_page_json(jsonData) values(%s)
        ''', [dict_test]

    )
    test_conn.commit()