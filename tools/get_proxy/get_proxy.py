# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: get_proxy.py
@time: 2019/1/28
"""
import os
import sys
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
new_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '\AmericanRealEstate'
print(new_path)
print(sys.path.append(new_path))


import pandas as pd
import requests
import pymysql
from tools.get_sql_con import get_sql_con
conn = get_sql_con()
cursor = conn.cursor()


# 从网站上获取代理
def get_proxy_from_url(url=None):
    data = pd.read_html('https://www.kuaidaili.com/free/inha/',header=0)
    print(data[0].head())
    data[0].to_csv('./proxy_df.csv',index=False)


class GetIP(object):
    def delete_ip(self,ip):
        # 重数据库中删除无效的ip
        delete_sql = """
        delete from ip_proxy where ip = '{0}'
        """.format(ip)
        cursor.execute(delete_sql)
        conn.commit()
        return True
    def judge_ip(self,ip,port,proxy_type):
        #判断ip是否可用
        http_url = "http://www.baidu.com"
        proxy_url = "http://{0}:{1}".format(ip,port)
        try:
            if proxy_type == 'HTTP':
                proxy_dict = {
                    "http":proxy_url,
                }
            else:
                proxy_dict = {
                    "https": proxy_url,
                }

            response = requests.get(http_url, proxies=proxy_dict,)
        except Exception as e:
            print("invalid ip and port")
            # self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if code>=200 and code<=300:
                print("effective ip")
                return True
            else:
                print("invalid ip and port")
                # self.delete_ip(ip)
                return False
    def get_random_ip(self):
        '''
        从数据中随机回去ip
        '''
        random_sql = 'select ip,port,proxy_type from ip_proxy ORDER by RAND() LIMIT 1'
        result = cursor.execute(random_sql)
        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]
            proxy_type = ip_info[2]
            judge_result = self.judge_ip(ip,port,proxy_type)
            if judge_result:
                if proxy_type=='HTTP':
                    return 'http://{0}:{1}'.format(ip,port)
                else:
                    return 'https://{0}:{1}'.format(ip,port)
            else:
                self.get_random_ip()

    def remove_database_invalidation_ip(self):
        ip_sql ="select ip,port,proxy_type from ip_proxy"
        result = cursor.execute(ip_sql)
        count_validations = 0
        count_invalidataions =0
        for ip_info in cursor.fetchall():
            print(ip_info)
            ip = ip_info[0]
            port = ip_info[1]
            proxy_type = ip_info[2]
            judge_result = self.judge_ip(ip, port, proxy_type)
            if judge_result:
                count_validations +=1
            else:
                count_invalidataions +=1
        print("合法",count_validations,"不合法",count_invalidataions)

    def real_get_random_ip(self):
        random_sql = 'select ip,port,proxy_type from ip_proxy ORDER by RAND() LIMIT 1'
        result = cursor.execute(random_sql)
        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]
            proxy_type = ip_info[2]

            # scrapy直接传入一个ip代理：
            # if proxy_type == 'HTTP':
            #     return 'http://{0}:{1}'.format(ip, port)
            # else:
            #     return 'https://{0}:{1}'.format
            # 对于requests需要返回一个字典：
            if proxy_type == 'HTTP':
                return {'HTTP':'{0}:{1}'.format(ip, port)}
            else:
                return {'HTTPS':'{0}:{1}'.format(ip, port)}


    def get_single_ip(self):
        random_sql = 'select ip,port,proxy_type from ip_proxy LIMIT 1'
        result = cursor.execute(random_sql)
        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]
            proxy_type = ip_info[2]

            # scrapy直接传入一个ip代理：
            # if proxy_type == 'HTTP':
            #     return 'http://{0}:{1}'.format(ip, port)
            # else:
            #     return 'https://{0}:{1}'.format
            # 对于requests需要返回一个字典：
            if proxy_type == 'HTTP':
                return {'HTTP':'{0}:{1}'.format(ip, port)}
            else:
                return {'HTTPS':'{0}:{1}'.format(ip, port)}


    def get_csv_ip(self):
        # proxy_data = pd.read_csv('./proxy_df.csv')
        pass






if __name__ == '__main__':
    # get_proxy_from_url()
    proxy_data = pd.read_csv('./proxy_df.csv')

    get_ip = GetIP()
    validation_proxy_ip = 0
    for i in range(len(proxy_data)):

        result = get_ip.judge_ip(proxy_data['IP'].iloc[i], port=proxy_data['PORT'].iloc[i], proxy_type=proxy_data['类型'].iloc[i])
        if result:
            print({'HTTP':'{0}:{1}'.format(proxy_data['IP'].iloc[i], proxy_data['PORT'].iloc[i])})
            validation_proxy_ip += 1

    print(validation_proxy_ip)
