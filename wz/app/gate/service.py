#coding:utf8
'''
Created on 2013-9-16
存储方法的类
@author: jt
'''
#from firefly.server.globalobject import rootserviceHandle,GlobalObject
from firefly.utils.services import CommandService

gateInMethod=CommandService("gatein")#gate拦截并处理的指令号方法

def gateIn(target):
    '''处理gate里面的端口号逻辑不对外开放'''
    gateInMethod.mapTarget(target)
    
    

    
    