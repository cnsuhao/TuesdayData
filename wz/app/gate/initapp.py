#coding:utf8
'''
Created on 2013-9-2

@author: jt
'''
from firefly.server.globalobject import GlobalObject
from childManager import ChildsManager


GlobalObject().root.childsmanager=ChildsManager()

def loadModule():
    from netapp import *

    
    



#reactor.callLater(differTime(8,0,0), addEnergyPerDay)