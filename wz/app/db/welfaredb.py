#coding:utf8
'''
Created on 2013-11-4

@author: ywq
'''

from tool import dbto

def getAllIntensifyInfo():
    '''获取福利配置表所有数据'''
    sql = "SELECT * FROM welfare"
    result = dbto.exeall(sql)
    data = {}
    for i in result:
        data[i['id']] = i
    return data


def getOrderInfo():
    '''按照顺序取出'''
    sql="SELECT * FROM welfare ORDER BY typeid,top"
    result=dbto.exeall(sql)
    
    data={} #key:任务类型 ，value:[welfare任务主键id,welfare任务主键id]
    sql="SELECT * FROM welfare_type"
    td=dbto.exeall(sql)
    for tinfo in td:
        data[tinfo['id']]=[]
    for row in result:
        data[row['typeid']].append(row['id'])
    return data

def getAllTypes():
    '''获取所有福利任务类型'''
    sql="SELECT * FROM welfare_type"
    result=dbto.exeall(sql)
    data={}
    for row in result:
        data[row['id']]=row
    return data