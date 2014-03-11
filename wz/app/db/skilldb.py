#coding:utf8
'''
Created on 2013-9-23

@author: jt
'''

from tool import dbto
from twisted.python import log
import types

def getAllskill():
    '''获取所有技能信息'''
    sql="SELECT * FROM skill";
    data=dbto.exeall(sql)
    newdata={}
    for item in data:
#        try:
#            item['script']=eval(item['script'])
#        except:
#            log.err("skill table id=%d  script is error"%item['id'])
            
        newdata[item['id']]=item
    return newdata

