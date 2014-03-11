#coding:utf8
'''
Created on 2013-10-17

@author: jt
'''
from tool import dbto
from twisted.python import log

def getByPid(pid):
    '''获取角色解锁和未解锁的宠物'''
    sql="SELECT * FROM player_pet WHERE pid=%d ORDER BY id"%pid;
    data=dbto.exeall(sql)
    return data

def selectBypidAndpetid(pid,petid):
    '''
    @return: bool 是否存在
            判断是否存在'''
    
    sql="SELECT * FROM player_pet WHERE pid=%d AND petid=%d"%(pid,petid)
    if dbto.exeone(sql):
        return True
    return False
#
#def updateByPidPetid(pid,petid):
#    '''设置角色宠物解锁，根据角色id和宠物id'''
#    sql="UPDATE player_pet SET unlocks=1 WHERE pid=%d AND petid=%d"%(pid,petid)
#    flg=dbto.exeupdate(sql)
#    return flg

#def addNewPet(pid,petid,unlocks,silver):
#    '''添加新的宠物
#    @param pid: int 角色id
#    @param petid: int 宠物id
#    @param unlocks: int 0未解锁 1已经解锁
#    @param silver: int 解锁需要花费的金币
#    '''
#    sql="insert  into `player_pet`(`pid`,`petid`,`level`,`exp`,`unlocks`,`silver`,`newgid`,`qhhplv`,`qhattlv`) \
#    values (%d,%d,1,0,%d,%d,0,0,0)"%(pid,petid,unlocks,silver)
#    flg=dbto.exeupdate(sql)
#    return flg