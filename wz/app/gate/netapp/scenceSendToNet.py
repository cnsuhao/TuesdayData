#coding:utf8
'''
Created on 2013-9-23

@author: jt
'''
from firefly.server.globalobject import rootserviceHandle, GlobalObject

@rootserviceHandle
def SenenceSendToNet(cid,data,didList):
    '''接收net转发过来的信息
    @param cid: int 指令号
    @param didList: [int] 玩家动态id列表
    @param data: obj proto内容
    '''
    GlobalObject().root.callChild('net','pushData',cid,data,didList)
    
@rootserviceHandle
def cloeNetClient(did):
    '''接收net转发过来的信息
    @param did: int 与游戏客户端连接的动态id
    '''
    GlobalObject().root.callChild('net','cloeClient',did)