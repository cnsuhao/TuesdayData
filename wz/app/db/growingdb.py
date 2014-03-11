#coding:utf8
'''
Created on 2013-9-22

@author: jt
'''
from tool import dbto

def getAllGrowing():
    '''获取所有宠物成长信息'''
    sql="SELECT * FROM growing";
    data=dbto.exeall(sql)
    return data