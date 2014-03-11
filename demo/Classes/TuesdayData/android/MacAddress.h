//
//  MacAddress.h
//  project
//
//  Created by http://www.9miao.com on 14-2-25.
//
// on 14-2-26.
//
//

#ifndef __project__MacAddress__
#define __project__MacAddress__

#include <iostream>

#include "platform/android/jni/JniHelper.h"
#include <android/log.h>
#include <jni.h>

class MacAddress {
    
public:
    
    const char* getMacAddress();
    
    static MacAddress* getInstance();
    
};

#endif /* defined(__project__MacAddress__) */
