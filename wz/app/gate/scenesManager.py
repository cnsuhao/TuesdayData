#coding:utf8
'''
Created on 2013-9-17
场景管理器
@author: jt
'''
from scenes import Scenes
from firefly.utils.singleton import Singleton

class ScenesManager(object):
    '''场景管理器'''

    __metaclass__ = Singleton

    def __init__(self):
        
        self.scenesDict={}   #key:gate连接动态id ， values:场景服务器类
        self.maxPlayerCount=80 #场景服务角色上限
    
    def addScense(self,tid,name):
        '''添加一个场景服务器
        @param tid: int gate中连接的动态id
        @param name: str 场景服务器的名称
        '''
        scenes=Scenes(tid, name)
        self.scenesDict[tid]=scenes
    
    
    def delScense(self,tid):
        '''删除一个场景服务器'''
        if self.scenesDict.has_key(tid):
            del self.scenesDict[tid]
    
    def getScenes(self):
        '''选择一个人数最少的场景服务器
        @return: int 场景服务器连接id
        '''
        tid=-1
        ct=100000
        for item in self.scenesDict.values():
            if item.getCounts()<80:
                return item._tid
            else:
                if item.getCounts()<ct:
                    ct=item.getCounts()
                    tid=item._tid
        return tid
        