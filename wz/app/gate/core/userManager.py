#coding:utf8
'''
Created on 2013-9-16

@author: jt
'''
from firefly.utils.singleton import Singleton
from twisted.python import log
from firefly.server.globalobject import GlobalObject

class UserManager(object):
    '''角色管理类'''
    __metaclass__ = Singleton

    def __init__(self):
        '''初始化'''
        self._usersDict={} #key:账号,value User类
        self._didToUName={} #key:did,value 账号
        
        
    def _deleteByDid(self,did):
        '''根据角色动态id仅删除数据'''
        if self._didToUName.has_key(did):
            uName=self._didToUName[did] #角色账号
            del self._usersDict[uName]
            del self._didToUName[did]
            
    def _deleteByuName(self,uName):
        '''根据角色账号仅删除数据'''
        if self._usersDict.has_key(uName):
            user=self._usersDict[uName]
            did=user.did
            del self._didToUName[did]
            del self._usersDict[uName]
            
        
    def addUser(self,user):
        '''添加角色类
        @param did: int 角色登陆动态id
        @param user: obj User类
        '''
        self._didToUName[user.did]=user.uName
        self._usersDict[user.uName]=user
        
        
    def delUser(self,did):
        '''删除角色
        @param did: int 角色登陆动态id
        '''
        self._deleteByDid(did)
#        GlobalObject().root.callChild('net',"cloeClient",did) ##通知客户端角色掉线  did
            
    def updateUserDid(self,uName,newDid):
        '''更改角色动态链接id'''
        if self._usersDict.has_key(uName):
            user=self._usersDict[uName]
            oldDid=user.did
            user.did=newDid
            obj=self._didToUName[oldDid]
            del self._didToUName[oldDid]
            self._didToUName[newDid]=obj
#            GlobalObject().root.callChild('net',"cloeClient",oldDid) ##通知客户端角色掉线  did
            
    def isHaveUser(self,uName):
        '''判断是否角色是否正在游戏中'''
        return self._usersDict.has_key(uName)
    
    
    def getUserBydid(self,did):
        '''根据动态id获取角色实例'''
        if self._didToUName.has_key(did):
            uName=self._didToUName[did]
            user=self._usersDict[uName]
            if user:
                return user
            else:
                log.err('gate->core->userManager->getUserBydid(self,did)')
                
    def getUserByuName(self,uName):
        '''根据角色账号获取角色实例'''
        if self._usersDict.has_key(uName):
            user=self._usersDict[uName]
            if user:
                return user
            else:
                log.err('gate->core->userManager->getUserByuName(self,uName)')
                
    def getUserByPid(self,pid):
        '''根据角色账号获取角色实例'''
        for us in self._usersDict.values():
            if us.pid==pid:
                return us
        return None
        
        
        