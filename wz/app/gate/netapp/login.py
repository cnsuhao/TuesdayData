#coding:utf8
'''
Created on 2013-9-16
@author: jt
'''
from app.gate.app import land_app
from app.gate.service import  gateIn
from app import js


#@gateIn
#def land_1000(cid,did,data):
#    '''角色登陆
#    @param cid: int 指令号
#    @param did: int 角色动态id
#    @param data: str proto字符串
#    '''
#    param=land_pb2.landRequest();
#    param.ParseFromString(data)
#    rtn=land_pb2.landResponse();
#    uname=param.uname #登陆账号
#    pwd=param.pwd     #登陆密码
#    land_app.land(uname, pwd, did,rtn)
#    return rtn.SerializeToString()

@gateIn
def land_1001(cid,did,data):
    '''角色登陆
    @param cid: int 指令号
    @param did: int 角色动态id
    @param data: str proto字符串
    '''
    info=js.load(data)
    uname=info['uname'] #登陆账号
    pwd=info['pwd']     #登陆密码
    rtn=js.Obj()
    land_app.land(uname, pwd, did,rtn)
    rst= js.objstr(rtn)
    return rst

@gateIn
def land_1002(cid,did,data):
    '''角色注册
    @param cid: int 指令号
    @param did: int 角色动态id
    @param data: str proto字符串
    '''
    info=js.load(data)
    uname=info['uname'] #注册账号
    pwd=info['pwd']     #注册密码
    rtn=js.Obj()
    land_app.login(uname, pwd, did,rtn)
    rst= js.objstr(rtn)
    return rst



