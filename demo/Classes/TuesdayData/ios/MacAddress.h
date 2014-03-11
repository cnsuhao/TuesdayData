//
//  MacAddress.h
//  project
//
//  Created by 栗元峰 on 14-2-26.
//
//

#ifndef __project__MacAddress__
#define __project__MacAddress__

#include <iostream>

class MacAddress {
    
public:
    
    const char* getMacAddress();
    
    static MacAddress* getInstance();
    
};

#endif /* defined(__project__MacAddress__) */
