# -*- coding: utf-8 -*-

import  pywapi
import string

#날씨 API, 현재 사용하지 않음. 
class YahooAPI(object): 
 
    
    def getTemperature(self, address):
        yahoo_result = pywapi.get_weather_from_yahoo(self.getLocationCode(address))
        return yahoo_result['condition']['temp']
    
    
    def getLocationCode(self, address):
        return pywapi.get_location_ids(self.getCityStrFromAddr(address))
    
    def getCityStrFromAddr(self, address):
        
        cityStrEng = None; 
        cityStrKor = address.split(" ")[0]
        
        
        if cityStrKor.startswith('서울'):
            cityStrEng = "Seoul"
        
        return cityStrEng; 
            