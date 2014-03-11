#coding:utf8
'''
Created on 2013-9-28

@author: jt
'''
from tool import dbto
from twisted.python import log

def getAllMonster():
    '''获取所有宠物信息'''
    sql="SELECT * FROM monster";
    data=dbto.exeall(sql)
    jg={}
    for item in data:
        try:
            item['skilllist']=eval(item['skilllist'])
            jg[item['id']]=item
        except:
            log.err("monster skill table id=%d  skilllist is error"%item['id'])
    return jg


def getAllMonster_Json():
    '''获取所有宠物json信息'''
    sql="SELECT * FROM monster";
    data=dbto.exeall(sql)
    jg={}
    for item in data:
        try:
            item['skilllist']=eval(item['skilllist'])
            jg[item['id']]=item
        except:
            log.err("monster skill table id=%d  skilllist is error"%item['id'])
    return jg

def getTypeMonster(tyepid):
    '''获取某一类型的怪物'''
    sql="SELECT * FROM monster WHERE btype=%d"%tyepid;
    data=dbto.exeall(sql)
    return data

def addMonster(data):
    '''添加怪物
    @param data: dict 字典类型
    '''
    sql="insert  into `monster`(`pname`,`color`,`btype`,`hp`,`att`,`def`,`dex`,`agl`,`par`,`cri`,`crp`,`spd`,`mov`,`rng`,`skilllist`,`coatt`,`dou`,`tou`,`ske`,`resourceid`) values \
                                ('%s',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,'%s',%d,%d,%d,%d,%d)"%\
                                (data.get("pname",u'无名小怪'),data.get("color",1),data.get("btype",1),data.get("hp",1),data.get("att",1),\
                                 data.get('def',1),data.get('dex',1),data.get('agl',1),data.get('par',1),data.get('cri',1),data.get('crp',1),\
                                 data.get('spd',1),data.get('mov',1),data.get('rng',1),data.get('skilllist'),'[]',data.get('coatt',1),\
                                 data.get('dou',1),data.get('tou',1),data.get('ske',1),data.get('resourceid'),1);
    flag=dbto.exeupdate(sql)
    return flag