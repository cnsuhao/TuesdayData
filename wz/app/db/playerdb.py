#coding:utf8
'''
Created on 2013-9-17
player表数据库操作
@author: jt
'''
from tool import dbto

def getByuname(uname):
    '''根据角色账号获取角色信息
    @param uname: str 角色账号
    '''
    sql="SELECT * FROM player WHERE uname='%s'"%uname;
    data=dbto.exeone(sql)
    return data