#coding:utf8
'''
Created on 2013-9-16

@author: jt
'''
import datetime

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