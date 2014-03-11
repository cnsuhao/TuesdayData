//
//  NetWorkUtils.h
//  project
//
//  Created by http://www.9miao.com on 14-2-25.
//
//

#ifndef __project__NetWorkUtils__
#define __project__NetWorkUtils__

#include <iostream>

#include "platform/android/jni/JniHelper.h"
#include <android/log.h>
#include <jni.h>

typedef enum{
    NetWorkTypeNone,
    NetWorkType3G,
    NetWorkTypeWifi
}NetWorkType;

class NetWorkUtils
{
public:
    
    bool isNetWorkAvailble();
    
    NetWorkType getNewWorkType();
    
    static NetWorkUtils* getInstance();
};

#endif /* defined(__project__NetWorkUtils__) */
