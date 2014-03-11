#coding:utf8
'''
Created on 2013-8-30
@author: jt
'''
from firefly.server.globalobject import GlobalObject
from twisted.python import log
import gc
from twisted.internet import reactor
from app.scense import tables

    
def doWhenStop():
    '''服务器关闭前的操作'''
    pass

GlobalObject().stophandler = doWhenStop


def loadModule():
    from app.scense.nodeapp import *
    cleanMeM(1800)
    
#    from app.scense.nodeapp import messageshow
#    messageshow.sendMessage(1008, "[1,2,3]", "{name:张三}")

def cleanMeM(delta):
    '''内存清理
    '''
    gc.collect()
    reactor.callLater(delta,cleanMeM,delta)