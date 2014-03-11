#coding:utf-8
'''
Created on 2013-11-14
消息提示类
@author: jiangtao
'''
from firefly.server.globalobject import GlobalObject
#from app import js


#@remoteserviceHandle('gate')
def sendMessage(cid,data,didList):
    '''向游戏客户端发送信息
    @param cid: int 指令号                                        # 1501-角色金钱     #1601-福利任务已达成完成条件
    @param data: json内容
    @param didList: [int] 玩家动态id列表
    '''
    GlobalObject().remote['gate'].callRemote("SenenceSendToNet",cid,data,didList)