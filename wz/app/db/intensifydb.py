#coding:utf-8
'''
Created on 2013-10-30

@author: ywq
'''
from tool import dbto

def getAllIntensifyInfo():
    '''获取宠物强化成功率和消耗表所有数据'''
    sql = "SELECT * FROM intensify"
    result = dbto.exeall(sql)
    data = {}
    for i in result:
        data[i['level']] = i
    return data