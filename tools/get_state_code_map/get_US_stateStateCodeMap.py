# -*- coding:utf-8 _*-  
""" 
@author:Administrator
@file: get_US_stateStateCodeMap.py
@time: 2019/1/9
"""
import pandas as pd
from sqlalchemy import create_engine

from tools.get_sql_con import get_sql_con


def get_data_from_html():
    """
    get state and state abbreviation csv file from html
    :return:
    """
    data = pd.read_html('./US_State_StateCode_Map.html')
    # print(data)
    print(data[0])
    data = pd.DataFrame(data[0])
    print(data.head())
    print(len(data.iloc[:,:]))
    data.to_csv('./state_code_map.csv',index=False)


def standard_data():
    """
    standard csv file to save in database
    :return:
    """
    state_code_data = pd.read_csv('./state_code_map.csv')
    state_code_data = state_code_data[['stateName','stateAbbreviation']]
    print(state_code_data.head())
    state_code_data.to_csv('real_state_code_map.csv',index=False)
    return state_code_data


if __name__ == '__main__':
    data = standard_data()
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/america_real_estate', echo=False)
    data.to_sql(name='state_code_map', con=engine, if_exists='append')
