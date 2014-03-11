#coding:utf8
'''
Created on 2013-8-14

@author: lan
'''
from dataloader import registe_madmin,CheckMemDB,MAdminManager
from firefly.dbentrust.memclient import mclient
from firefly.server.globalobject import GlobalObject
import mPlayer

def doWhenStop():
    """服务器关闭前的处理
    """
    print "##############################"
    print "##########checkAdmins#############"
    print "##############################"
    MAdminManager().checkAdmins()
    
GlobalObject().stophandler = doWhenStop


def loadModule():
    mclient.flush_all()
    mPlayer.player_m.insert()
    mPlayer.playerPet_m.insert()
    mPlayer.playerFight_m.insert()
    mPlayer.playerInstance_m.insert()
    mPlayer.playerWelfare_m.insert()
    registe_madmin()
    CheckMemDB(1800)