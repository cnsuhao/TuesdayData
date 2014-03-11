#coding:utf8
'''
Created on 2013-9-17
角色登陆
@author: jt
'''
from app.mem.mPlayer import player_m, playerPet_m, playerFight_m,\
    playerWelfare_m
from app.db import playerdb, player_petdb, welfaredb
from app.gate.core.user import User
from app.gate.core.userManager import UserManager
from app.gate.scenesManager import ScenesManager
from firefly.server.globalobject import GlobalObject
#from app.scense.core.language.language import Lg


def land(uname,pwd,did,rtn):
    '''登陆操作
    @param uname: str 登陆账号
    @param pwd:   str 登陆密码
    @param did:   int 角色登陆动态id
    @param rtn:   obj  需要返回给客户端的信息
    '''
    if not pwd: #没有密码
        pinfo=playerdb.getByuname(uname)  #角色信息
        if not pinfo:#如果是第一次进游戏
            mpinfo=player_m.new({"uname":uname}) #创建账号
            pid=mpinfo.get("id")
            mpinfo.syncDB()                  #同步数据库
            _loginScense(did, uname)
            info=playerdb.getByuname(uname) #player表数据
            if not info:
                rtn.result=False
            else:
                rtn.result=True 
                rtn.pid=info.get('id',-1)
                rtn.silverMoney=info.get('silvermoney',-1)
                rtn.gold=info.get('gold',-1)
                rtn.isfirst=True
        else:
            _loginScense(did, uname)
            rtn.result=True 
            rtn.pid=pinfo.get('id',-1)
            rtn.silverMoney=pinfo.get('silvermoney',-1)
            rtn.gold=pinfo.get('gold',-1)
            rtn.isfirst=False
    else:#如果有密码
        pinfo=playerdb.getByuname(uname)  #角色信息
        if not pinfo:
            rtn.result=False
            return
        if pwd==pinfo['pwd']:
            _loginScense(did, uname)
            rtn.result=True 
            rtn.pid=pinfo.get('id',-1)
            rtn.silverMoney=pinfo.get('silvermoney',-1)
            rtn.gold=pinfo.get('gold',-1)
            rtn.isfirst=False
            
def login(uname,pwd,did,rtn):
    '''注册账号
    @param uname: str 账号
    @param pwd:   str 密码
    @param did:   int 角色登陆动态id
    @param rtn:   obj  需要返回给客户端的信息
    '''
    pinfo=playerdb.getByuname(uname)  #角色信息
    if not pinfo:#如果是第一次进游戏
        mpinfo=player_m.new({"uname":uname,"pwd":pwd,"nickname":"","gold":100,"silvermoney":10000,"luck":0,"createtime":"2014-01-21 14:32:39"}) #创建账号
#        pid=mpinfo.data.get("id")
        mpinfo.syncDB()                  #同步数据库
        info=playerdb.getByuname(uname) #player表数据
        pid=info.get('id',-1)
        if not info:
            rtn.result=False
        else:
            _loginPlayerAndloginScense(did, uname,pid)
            rtn.result=True 
            rtn.pid=info.get('id',-1)
            rtn.silverMoney=info.get('silvermoney',-1)
            rtn.gold=info.get('gold',-1)
            rtn.isfirst=True
    else:
        rtn.result=False   
#        rtn.msg=Lg().g(1012) #注册失败原因
        
def _loginScense(did,uName):
    '''角色进入场景
    @param uName: str 登陆账号
    @param did:   int 角色登陆动态id
    '''
    isplaying=UserManager().isHaveUser(uName) #是否正在游戏中
    if isplaying:#如果真在游戏中
        user=UserManager().getUserByuName(uName)#获取角色实例
        tid=user.tid #角色现在正在哪个场景服务器中
        GlobalObject().root.callChild(tid,1001,did,uName) #更改玩家登陆动态id
        UserManager().updateUserDid(uName, did)
    else:
        user=User(did, uName)           #创建一个角色实例
        tid=ScenesManager().getScenes() #获取一个合适的场景服务器
        user.tid=tid                    #设置角色的服务器连接id
        UserManager().addUser(user)     #添加角色到角色管理器中
        
                           
        GlobalObject().root.callChild(tid,1000,did,uName)
        
def _loginPlayerAndloginScense(did,uName,pid):
    '''角色注册并角色进入场景
    @param uName: str 登陆账号
    @param did:   int 角色登陆动态id
    '''
    isplaying=UserManager().isHaveUser(uName) #是否正在游戏中
    if isplaying:#如果真在游戏中
        user=UserManager().getUserByuName(uName)#获取角色实例
        tid=user.tid #角色现在正在哪个场景服务器中
        GlobalObject().root.callChild(tid,1001,did,uName) #更改玩家登陆动态id
        UserManager().updateUserDid(uName, did)
    else:
        user=User(did, uName)           #创建一个角色实例
        tid=ScenesManager().getScenes() #获取一个合适的场景服务器
        user.tid=tid                    #设置角色的服务器连接id
        UserManager().addUser(user)     #添加角色到角色管理器中
        GlobalObject().root.callChild(tid,1002,did,uName,pid)
    