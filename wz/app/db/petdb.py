#coding:utf8
'''
Created on 2013-9-22
@author: jt
'''

from tool import dbto
from twisted.python import log

def getAllPets():
    '''获取所有宠物信息'''
    sql="SELECT * FROM pet";
    data=dbto.exeall(sql)
    jg={}
    for item in data:
        try:
            item['skilllist']=eval(item['skilllist'])
            jg[item['id']]=item
        except:
            log.err("skill table id=%d  skilllist is error"%item['id'])
    return jg


def getPetExp():
    '''获取宠物升级所需经验
    '''
    sql = "SELECT * FROM pet_exp"
    data = dbto.exeall(sql)
    result = {}
    for i in data:
        result[i["levelId"]] = i["exp"]
    return result