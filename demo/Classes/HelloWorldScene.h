//
//  HelloWorldScene.h
//  project
//
//  Created by http://www.9miao.com on 14-2-25.
//
//

#ifndef __HELLOWORLD_SCENE_H__
#define __HELLOWORLD_SCENE_H__

#include "cocos2d.h"
#include "cocos-ext.h"

USING_NS_CC;
USING_NS_CC_EXT;

class HelloWorld : public cocos2d::CCLayer
{

    void setUp(CCObject* sender = NULL, CCControlEvent controlEvents = NULL);
    
    void menuCloseCallback(CCObject* sender = NULL, CCControlEvent controlEvents = NULL);
    
    CCLabelTTF* ttf;
    
public:

    virtual bool init();  

    static cocos2d::CCScene* scene();

    CREATE_FUNC(HelloWorld);

};

#endif // __HELLOWORLD_SCENE_H__
