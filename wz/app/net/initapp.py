#coding:utf8
'''
Created on 2013-8-30

@author: jt
'''
from firefly.server.globalobject import GlobalObject
from firefly.netconnect.datapack import DataPackProtoc
from firefly.utils.services import CommandService
from twisted.python import log
from twisted.internet import defer


def callWhenConnLost(conn):
    '''当与游戏客户端连接断开时的处理'''
    did = conn.transport.sessionno #动态id
    GlobalObject().remote['gate'].callRemote("NetConnLost",did)


#dataprotocl = DataPackProtoc(78,37,38,48,9,0) #协议头
dataprotocl = DataPackProtoc(0,0,0,0,0,0) #协议头
GlobalObject().netfactory.setDataProtocl(dataprotocl)

GlobalObject().netfactory.doConnectionLost = callWhenConnLost
GlobalObject().remote['gate']._reference._service.unDisplay.add("pushData")
GlobalObject().remote['gate']._reference._service.unDisplay.add("pushObject")

def loadModule():
    import netapp
    
    

