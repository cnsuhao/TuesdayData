//
//  Test.cpp
//  project
//
//  Created by 栗元峰 on 14-2-25.
//
//

#include "TuesdayData.h"
#include <time.h>
#include "SocketClient.h"
#include "message.h"
#include "NetWorkUtils.h"
#include "MacAddress.h"

static SocketClient* _socket = NULL;

const char* TuesdayData::sendTuesdayData(const char* event, const char* gameID, const char* userID)
{
    if (NetWorkUtils::getInstance()->isNetWorkAvailble() == false)
        return NULL;

    do
    {
        if (_socket && _socket->m_iState != SocketClient_DESTROY){
            break;
        }
        
        if (_socket == NULL)
        {
            _socket = new SocketClient(IP, HOST, 1, 1, NULL);
            _socket->start();
        }
        
        _socket->reconnect();
        
    }
    while (1);
    
    string send = gameID;
    
    if (userID)
        send = send + " ," + userID;
    
    send = send + " ," + event;
    
    time_t rawtime;
    struct tm * timeinfo;

    
    string macAddress = string(MacAddress::getInstance()->getMacAddress());
    
    send += string(" ,") + macAddress + " ";
    
    time ( &rawtime );
    timeinfo = localtime (&rawtime);
    char time[32];
    
    sprintf(time, "(%04d/%02d/%02d %02d:%02d:%02d)",
            timeinfo->tm_year+1900,
            timeinfo->tm_mon,
            timeinfo->tm_mday,
            timeinfo->tm_hour,
            timeinfo->tm_min,
            timeinfo->tm_sec);
    
    send += string(" ") + time;
    
    printf("\n\n%s\n\n",send.c_str());
    
    Message *msg=_socket->constructMessage(send.c_str(), 1000);
    _socket->sendMessage_(msg, true);
    
    return send.c_str();
}
