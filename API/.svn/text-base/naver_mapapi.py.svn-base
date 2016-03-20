# -*- coding: utf-8 -*-
'''
Created on 2013. 8. 31.

@author: kall99
'''

import urllib2
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup


from htmlparser import *; 
from mlstripper import *

class NaverMapAPI(object):
    
    
   
    def getLocalPlaceList(self, keyword):
        
        
        
        keyword = unicode(keyword).encode('utf-8')
        
        print "getLocalPlaceList : " + keyword
         
        url = "http://m.map.naver.com/search.nhn?query="+keyword+"&sm=hty&type=SITE_1&siteSort=1";
        raw = urllib2.urlopen(url)
        html = raw.read()
        
        titleIdxList = [m.start() for m in re.finditer('\"title\"', html)]
        telIdxList = [m.start() for m in re.finditer('\"tel\"', html)]
        addrIdxList = [m.start() for m in re.finditer('\"addr\"', html)]
        descIdxList = [m.start() for m in re.finditer('\"desc\"', html)]
        optionsIdxList = [m.start() for m in re.finditer('\"options\"', html)]
        longitudeIdxList = [m.start() for m in re.finditer('\"coordinateX\"', html)]
        latitudeIdxList = [m.start() for m in re.finditer('\"coordinateY\"', html)]
        
#         
#         print "titleIdxList count : " + str(len(titleIdxList))
#         print "addrIdxList count : " + str(len(addrIdxList))
#         print "descIdxList count : " + str(len(descIdxList)) 
#         print "optionsIdxList count : " + str(len(optionsIdxList))
#         print "latitudeIdxList count : " + str(len(latitudeIdxList))
#         print "longitudeIdxList count : " + str(len(longitudeIdxList))
#         
        count = len(titleIdxList)
        
        resultDictList = []
        #extract title 
        for i in range(0, count):
            resultDict = {}
            resultDict["name"]= strip_tags(html[titleIdxList[i]:].split(":")[1].split(",")[0]).replace('\"', "");
            resultDict["tel"]= html[telIdxList[i]:].split(":")[1].split(",")[0].replace('\"', "");
            resultDict["addr"]= html[addrIdxList[i]:].split(":")[1].split(",")[0].replace('\"', "");
            resultDict["detail"]= html[descIdxList[i]:].split(":")[1].split(",")[0].replace('\"', "");
            resultDict["second_info"]= html[optionsIdxList[i]:].split(":")[1].split(",")[0].replace('\"', "");
            resultDict["latitude"]= html[latitudeIdxList[i]:].split(":")[1].split(",")[0].replace('\"', "");
            resultDict["longitude"]= html[longitudeIdxList[i]:].split(":")[1].split(",")[0].replace('\"', "");
            
            resultDictList.append(resultDict)
            
        return resultDictList
        
         
        
        

if __name__ == '__main__':
    nm = NaverMap();
    nm.getLocalPlaceList("스타벅스")
    
    
