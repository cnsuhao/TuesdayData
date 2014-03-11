'''
Created on 2014-2-25

@author: jiangtao
'''
from tool import dbto
from twisted.python import log

def add(pid,msg):
    sql="INSERT  INTO `record`(`pid`,`msg`) VALUES ('%s','%s')"%(pid,msg);
    flag=dbto.exeupdate(sql)
    return flag