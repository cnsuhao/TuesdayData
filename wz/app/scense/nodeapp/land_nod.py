#coding:utf8
'''
Created on 2013-9-22
玩家登陆   gate服务传递过来的参数
@author: jt
'''
from firefly.server.globalobject import remoteserviceHandle
from app import js
from app.db import recorddb


print "load func"

@remoteserviceHandle('gate')
def land_1000(did,data):
    '''玩家登陆
    @param did: int 登陆动态id
    @param data: str 角色账号
    '''
    info=data.split(',')
    pid=info[0]
    msg=info[1]
    info=recorddb.add(pid, msg)
    
