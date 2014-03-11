#coding:utf-8
'''
Created on 2013-12-30

@author: jiangtao
'''
from tool import dbto
from twisted.python import log


def getListByPid(pid):
    '''获取角色携带的出战宠物'''
    sql="SELECT * FROM player_fight WHERE pid=%s"%pid;
    data=dbto.exeone(sql)
    if data:
        return eval(data['fightpet'])
    return None
    