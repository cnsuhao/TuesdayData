#coding:utf8
'''
Created on 2013-9-16
接收net转发信息
@author: jt
'''
from firefly.server.globalobject import rootserviceHandle, GlobalObject
from app.gate.service import gateInMethod
from app.gate.core.userManager import UserManager
from app import js
from app.gate.netapp import scenceSendToNet
from app.gate.scenesManager import ScenesManager

@rootserviceHandle
def forwarding(cid,did,data):
    '''接收net转发过来的信息
    @param cid: int 指令号
    @param did: int 连接id
    @param data: obj proto内容
    '''
#    if cid in gateInMethod._targets.keys():
#        return gateInMethod.callTarget(cid,cid,did,data)
#    else:
#        user=UserManager().getUserBydid(did)
#        if not user:
#            info=js.load(data)
#            pid=info.get("pid",0)
#            if pid<=0:
#                print u"关闭与游戏客户端的连接"
#                scenceSendToNet.cloeNetClient(did)
#                return
#            user=UserManager().getUserByPid(pid)
#            if user==None:
#                return "关闭与游戏客户端的连接2"
#                return
#        return GlobalObject().root.callChild(user.tid,cid,did,data)

    tid=ScenesManager().getScenes() #获取一个合适的场景服务器
    return GlobalObject().root.callChild(tid,cid,did,data)


@rootserviceHandle
def NetConnLost(did):
    '''角色掉线时的处理
    @param did: int 动态id
    '''
    user=UserManager().getUserBydid(did)
    if not user:
        return
    tid=user.tid
    pid=user.pid
    GlobalObject().root.callChild(tid,1004,did,pid)
    UserManager().delUser(did)
    
    

    
    
    
    