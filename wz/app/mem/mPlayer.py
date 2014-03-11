#coding:utf8
'''
Created on 2013-9-17
角色相关
@author: jt
'''

from firefly.dbentrust.mmode import MAdmin

#角色表
player_m = MAdmin('player','id',incrkey='id',timeout=600)


#角色拥有的宠物表
playerPet_m = MAdmin('player_pet','id',incrkey='id',timeout=600)


#宠物出战列表
playerFight_m = MAdmin('player_fight','pid',timeout=600)


#角色通关记录
playerInstance_m=MAdmin('player_instance','pid',timeout=600)


#角色福利任务记录表
playerWelfare_m = MAdmin('player_welfare','id',timeout=600)
