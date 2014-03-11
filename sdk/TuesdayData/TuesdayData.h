//
//  Test.h
//  project
//
//  Created by http://www.9miao.com on 14-2-25.
//
//

#ifndef __project__Test__
#define __project__Test__

#include <iostream>
using namespace std;

#define IP "183.60.243.195"

#define HOST 11009

class TuesdayData {
    
public:
    
    static const char* sendTuesdayData(const char* event, const char* gameID, const char* userID = NULL);
    
};


#endif /* defined(__project__Test__) */
