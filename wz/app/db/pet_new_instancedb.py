#coding:utf-8
'''
Created on 2013-10-25
通关副本开启新宠物表主键id
@author: jiangtao
'''
from tool import dbto
#from twisted.python import log

def getAll():
    '''获取所有宠物信息'''
    sql="SELECT * FROM pet_new_instance"
    values=dbto.exeall(sql)
    data={}
    for item in values:
        data[item['instanceid']]=item
    return data

def add(instanceid,petid,silver):
    '''添加'''
    sql="insert  into `pet_new_instance`(`instanceid`,`petid`,`silver`) values (%d,%d,%d);"
    flag=dbto.exeupdate(sql)
    return flag