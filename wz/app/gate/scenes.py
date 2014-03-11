#coding:utf8
'''
Created on 2013-9-17
场景-服务器
@author: jt
'''

class Scenes(object):
    '''游戏场景类'''


    def __init__(self,tid,name):
        '''初始化场景类'''
        self._tid=tid
        self._name=name
        self.playersSet=set([]) #角色账号
        
    def addPlayer(self,uname):
        '''角色进入场景服务器'''
        self.playersSet.add(uname)
        
    def delPlayer(self,uname):
        '''角色退出场景服务器'''
        try:
            self.playersSet.remove(uname)
        except:
            pass
        
    def getCounts(self):
        '''获取场景服务器中的用户数量'''
        return len(self.playersSet)
        
        