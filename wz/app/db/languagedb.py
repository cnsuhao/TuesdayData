#coding:utf-8
'''
Created on 2013-10-30

@author: ywq
'''
from tool import dbto

def getAllLanguage():
    '''获取language表所有数据'''
    sql = "SELECT * FROM language"
    result = dbto.exeall(sql)
    data = {}
    for i in result:
        data[i['id']] = i['content']
    return data