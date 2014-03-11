#coding:utf8
'''
Created on 2013-9-16

@author: jt
'''
from app.db import playerdb

class User(object):
    '''用户类'''


    def __init__(self,did,uName):
        '''
        @param uName: str 登陆账号
        @param did: id    角色登陆动态id
        '''
        self.uName=uName; #角色登陆账号
        self.did=did;  #角色动态id
        self.pwd=None;  #角色登陆密码
        self.pid=0; #角色id
        self.tid=0; #角色现在正在哪个场景服务器中
        info=playerdb.getByuname(uName)
        self.pid=info.get("id")
        self.pwd=info.get("pwd")
        
        