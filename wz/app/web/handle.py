#coding:utf8
'''
Created on 2013-9-4

@author: hg (www.9miao.com)
'''

from twisted.web import resource
from firefly.server.globalobject import webserviceHandle#,GlobalObject
#from twisted.web.resource import ErrorPage
#from firefly.server.globalobject import GlobalObject
#from urls import getDayRecordList,getStatistics
from app import js
from app.db import monsterdb, instancedb, pet_new_instancedb


@webserviceHandle("addmonster")
class addMonster(resource.Resource):
    
    def render(self,request):
        data = request.args['json'][0]
        info = js.load(data) #宠物信息
        flag=monsterdb.addMonster(info)
        return js.dumps(flag)

@webserviceHandle("addinstance")
class updateMonster(resource.Resource):
    
    def render(self,request):
        data = request.args['json'][0]
        info = js.load(data) #宠物信息
        flag=instancedb.addInstance(data)
        if flag:
            return '1'
        return '0'

@webserviceHandle("gtmonster")
class getTypeMonster(resource.Resource):
    '''根据怪物类型查看所有怪物信息'''
    def render(self,request):
        data = request.args['json'][0]
        info = js.load(data) 
        typeid=info.get('typeid',1) #宠物类型
        rtn=monsterdb.getTypeMonster(typeid)
        rt=js.dumps(rtn)
        return rt
    
    
    
@webserviceHandle("addpetnewinstance")
class addPetNewInstance(resource.Resource):
    '''添加通关关卡开启宠物'''
    def render(self,request):
        data = request.args['json'][0]
        info = js.load(data) #宠物信息
        instanceid=info.get('instanceid') #副本id
        petid=info.get("petid") #宠物id
        silver=info.get("silver") #花费需要的银币
        rtn=pet_new_instancedb.add(instanceid, petid, silver)
        rt=js.dumps(rtn)
        return rt
    
    
    
    