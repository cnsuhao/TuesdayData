#coding:utf8
'''
Created on 2013-8-30

@author: jt
'''
from firefly.server.globalobject import GlobalObject,remoteserviceHandle

@remoteserviceHandle('gate')
def pushData(cid,data,sendList):
    '''向网页客户端发送信息
    @param cid:      int      指令号
    @param data:     str      proto字符串
    @param sendList: list    [did] 
    '''
    GlobalObject().netfactory.pushObject(cid,data,sendList)

@remoteserviceHandle('gate')
def cloeClient(did):
    '''关闭与游戏客户端的连接
    @param did: int 与游戏客户端连接的动态id
    '''
    GlobalObject().netfactory.loseConnection(did)
    
