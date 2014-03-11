#coding:utf-8
'''
Created on 2013-10-25

@author: jiangtao
'''
from tool import dbto

def geConfigs():
    '''获取所有宠物成长信息'''
    sql="SELECT * FROM configs";
    configList=dbto.exeall(sql)
    data={}
    for item in configList:
        data[item['id']]=item['datas']
    return data