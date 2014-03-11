#coding:utf-8
'''
Created on 2014-2-17

@author: jiangtao
'''
from tool import dbto
from twisted.python import log

def getStartPets():
    '''获取角色初始化宠物'''
    sql="SELECT * FROM player_start_pet WHERE id=1";
    data=dbto.exeone(sql)
    pets=data['startpetids']
    try:
        rst=eval(pets)
    except:
        log.err("player_start_pet error")
    return rst