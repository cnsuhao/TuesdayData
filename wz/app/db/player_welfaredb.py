#coding:utf-8
'''
Created on 2014-1-26

@author: jiangtao
'''
from tool import dbto

def getByPid(pid):
    sql="SELECT * FROM player_welfare WHERE pid=%d ORDER BY typeid"%pid
    info=dbto.exeall(sql)
    return info
        