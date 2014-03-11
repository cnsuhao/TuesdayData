#coding:utf8
'''
Created on 2013-10-8
副本
@author: jt
'''
from twisted.python import log
from tool import dbto
def getAllInstance():
    sql="SELECT * FROM instance ORDER BY id"
    data=dbto.exeall(sql)
    jg={}
    for item in data:
        try:
            item['mlist']=eval(item['mlist'])
            jg[item['id']]=item
        except:
            log.err("instancedb  mlist error  id=%d"%item['id'])
    return jg



def getInstanceIdList():
    '''获取所有副本id列表'''
    sql="SELECT id FROM instance ORDER BY id"
    data=dbto.exeall(sql)
    jg=[]
    for item in data:
        jg.append(item['id'])
    return jg

def addInstance(data):
    '''添加副本'''
    sql="insert  into `instance`(`typeid`,`iname`,`mlist`,`monster_increase`,`pet_increase`,`silver`,`exp`,`condition`,`udlf`) values \
    (%d,'%s','%s','%s','%s',%d,%d,'%s','%s')"%(data.get('typeid',0),data.get('iname','name'),data.get('mlist'),'()'),data.get('monster_increase','0'),\
                                         data.get('pet_increase','0',data.get('silver',1),data.get('exp',1),data.get('condition','0'),data.get('udlf','[1,1,1,1]'));
    flag=dbto.exeupdate(sql)
    return flag
    
    
    
    
    
    
    
    
