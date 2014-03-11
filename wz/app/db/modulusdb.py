#coding:utf8
'''
Created on 2013-9-22

@author: jt
'''
from tool import dbto

def getModulus():
    '''获取所有系数'''
    sql="SELECT * FROM modulus";
    data=dbto.exeall(sql)
    if not data:
        return {}
    return data[0]