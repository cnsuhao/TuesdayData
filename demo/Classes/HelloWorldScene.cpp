#include "HelloWorldScene.h"
#include "TuesdayData.h"
typedef enum
{
    TestConnectToServer = 1001,
    TestLoginAccount = 1002,
    TestToUpdate = 1003,
    TestSelectTheRegion = 1004,
    TestEnterTheGame = 1005,
    TestConnectToServerFailure = 1011,
    TestLoginAccountFailure = 1012,
    TestToUpdateFailure = 1013,
    TestSelectTheRegionFailure = 1014,
    TestEnterTheGameFailure = 1015
    
}TestEnum;

CCScene* HelloWorld::scene()
{
    CCScene *scene = CCScene::create();
    HelloWorld* _layer = HelloWorld::create();
    scene->addChild(_layer);
    return scene;
}

bool HelloWorld::init()
{

    if ( !CCLayer::init() )
    {
        return false;
    }
    CCSize size = CCDirector::sharedDirector()->getWinSize();

    CCLayerColor* layerColor = CCLayerColor::create(ccc4(127, 127, 127, 255), size.width, size.height);
    this->addChild(layerColor);
    
    std::vector<TestEnum> vec;
    vec.push_back(TestConnectToServer);
    vec.push_back(TestLoginAccount);
    vec.push_back(TestToUpdate);
    vec.push_back(TestSelectTheRegion);
    vec.push_back(TestEnterTheGame);
    vec.push_back(TestConnectToServerFailure);
    vec.push_back(TestLoginAccountFailure);
    vec.push_back(TestToUpdateFailure);
    vec.push_back(TestSelectTheRegionFailure);
    vec.push_back(TestEnterTheGameFailure);
    
    std::vector<std::string> stringVec;
    stringVec.push_back("连接服务器");
    stringVec.push_back("用户登录");
    stringVec.push_back("更新");
    stringVec.push_back("选择大区");
    stringVec.push_back("进入游戏");
    stringVec.push_back("连接服务器失败");
    stringVec.push_back("用户登录失败");
    stringVec.push_back("更新失败");
    stringVec.push_back("选择大区失败");
    stringVec.push_back("进入游戏失败");
    
    for (unsigned int i=0; i<vec.size(); i++)
    {
        CCControlButton* btn1 = CCControlButton::create(stringVec.at(i).c_str(), "fonts/Marker Felt.ttf", 25);
        btn1->setPosition(CCPoint(92.5 + 195 * (i%5), 140 + 80 * (i/5)));
        this->addChild(btn1, 0, vec.at(i));
        btn1->addTargetWithActionForControlEvents(this, cccontrol_selector(HelloWorld::setUp), CCControlEventTouchUpInside);
    }
    
    ttf = CCLabelTTF::create("发送数据", "Arial", 25);
    ttf->setPosition(CCPoint(size.width/2, size.height * 3/4.0f));
    this->addChild(ttf);
    
    return true;
}

void HelloWorld::setUp(CCObject* sender, CCControlEvent controlEvents)
{
    CCControlButton* btn = (CCControlButton*) sender;
    char event[32];
    sprintf(event, "%d", btn->getTag());
    
    CCString* str = NULL;
    
    const char* test = TuesdayData::sendTuesdayData(event, "gamdID");
    if (test)
    {
        str = CCString::createWithFormat("发送数据： %s", test);
    }
    else
    {
        str = CCString::create("无网络");
    }
    ttf->setString(str->getCString());
}

void HelloWorld::menuCloseCallback(CCObject* sender, CCControlEvent controlEvents)
{
#if (CC_TARGET_PLATFORM == CC_PLATFORM_WINRT) || (CC_TARGET_PLATFORM == CC_PLATFORM_WP8)
	CCMessageBox("You pressed the close button. Windows Store Apps do not implement a close button.","Alert");
#else
    CCDirector::sharedDirector()->end();
#if (CC_TARGET_PLATFORM == CC_PLATFORM_IOS)
    exit(0);
#endif
#endif
}
