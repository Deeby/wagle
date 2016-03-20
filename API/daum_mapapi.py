# -*- coding: utf-8 -*-
import simplejson, urllib
from api_type import * 
from mlstripper import *

class DaumMapAPI(object):
    apikey = "48408559bb754dd16c517a5fd6d01e376a4be151"
     
    api_type = API_TYPE.LOC_ADDR2COORD
    def convAddr2Coord(self, addr):
        api_type = API_TYPE.LOC_ADDR2COORD  
        self.search_base ="http://apis.daum.net/local/geo/addr2coord"
 
        addr = unicode(addr).encode('utf-8')         
        args ={}
        args.update({
            'q': addr,  
            }) 
 
        result = self.request(**args)
        return self.parse(result);
    
    def convCoord2Addr(self, latitude, longitude):
        api_type = API_TYPE.LOC_COORD2ADDR
        self.search_base ="http://apis.daum.net/local/geo/coord2addr"
        args ={}
        args.update({
            'latitude': latitude,
            'longitude':longitude,  
           
            'apikey': self.apikey, 
            'output': 'json'
            })

        url = self.search_base + '?' + urllib.urlencode(args)
        result = simplejson.load(urllib.urlopen(url))
        return self.parse(result);
        
 
    def request(self, **args):
        args.update({
            'apikey': self.apikey, 
            'output': 'json'
            })

        url = self.search_base + '?' + urllib.urlencode(args)
        result = simplejson.load(urllib.urlopen(url))
        return result['channel']

    def parse(self, result):
        
        if self.api_type is API_TYPE.LOC_ADDR2COORD:
            coord = {}
            for item in result['item']:                 
                coord['lat']= item['lat']
                coord['lng']= item['lng'] 
            
            return coord; 
                
        if self.api_type is API_TYPE.LOC_COORD2ADDR:
            return result["fullName"]
            
        
                    
                    