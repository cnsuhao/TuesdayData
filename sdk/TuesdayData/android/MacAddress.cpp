//
//  MacAddress.cpp
//  project
//
//  Created by 栗元峰 on 14-2-26.
//
//

#include "MacAddress.h"
#include "cocos2d.h"
USING_NS_CC;
static MacAddress* instance = NULL;

MacAddress* MacAddress::getInstance()
{
	if (instance == NULL)
	{
		instance = new MacAddress();
	}
    
	return instance;
}

const char* MacAddress::getMacAddress()
{
    std::string str;
    
    JniMethodInfo minfo;
    bool isHave = JniHelper::getStaticMethodInfo(minfo,"com/jni/PhoneNet","returnMacString","()Ljava/lang/String;");
    jstring jstr;
    
    
    if (isHave)
    {
        jstr = (jstring)minfo.env->CallStaticObjectMethod(minfo.classID, minfo.methodID);
        str = JniHelper::jstring2string(jstr);
    }

	return str.c_str();
}

