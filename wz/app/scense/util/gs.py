#coding:utf8
'''
Created on 2012-4-20
工具类方法 处理各种公式算法
@author: jt
'''
import math
import datetime

def ceiling(a,b):
    '''Excel 中的算法'''
    a=float(a)
    b=float(b)
    
    da=0
    if a<=b:
        da= b
    else:
        da=math.ceil(a/b)*b
    print "ceiling(%s,%s)=%s  ,  %s"%(a,b,da,int(da))
    print ""
    
    return da

def addDict(a,b):
    '''两个字典类型相加，有相同key的value值相加，不同的key合并,只支持value值为数值类型
    '''
    allkeys = set(a.keys()).union(b.keys())
    info = {}
    for key in allkeys:
        info[key] = a.get(key,0)+ b.get(key,0)
    return info
    
    
def differTime(h,m,s):
    '''到达预设时间执行函数  return与当前时间相差的秒数
    @param h,m,s: int 预设 时,分,秒 
    return int 秒数
    '''
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    old=h*3600+m*60+s #预设时间 据0点得秒数
    young=hour*3600+minute*60+second #当前时间据0点得秒数
    
    if old>=young:
        return old-young
    else:
        return 24*3600-(young-old)
    
#reactor.callLater(differTime(19,10,0), GuildFightHandle,ldID)