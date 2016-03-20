# -*- coding: utf-8 -*- 
from naver_searchapi import *; 
from daum_searchapi import *; 
from daum_mapapi import *; 
from naver_mapapi import *; 


import json; 
#모든 OpenAPI는 본 클래스를 통해서 호출되어 진다. 
class OpenAPIController(object):
     
    daumApi = DaumSearchAPI()
    naverApi = NaverSearchAPI() 
    daumMapApi = DaumMapAPI();
    naverMapApi = NaverMapAPI();

    def __init__(self):
        pass 
    
    def convAddr2Coord(self, addr=None):
        if addr is None:
            return None;
         
        return self.daumMapApi.convAddr2Coord(addr);
    
    def convCoord2Addr(self, latitude=None, longitude=None): 
        return self.daumMapApi.convCoord2Addr(latitude, longitude);
        
    def getTastingPlaceImage(self, keyword=None, count=1):
        
        if keyword is None:
            return None; 

        imgList = self.naverApi.searchImage(keyword, count, 1);
            
        if imgList is None:
            imgList = self.daumApi.searchImage(keyword, count, 1)
        
        elif len(imgList) < count:
            diff  = count-len(imgList)
            for i in range(0,diff):
                imgList.extend( self.daumApi.searchImage(keyword, 1, 1))
 
        return imgList;
    
    def getBlogData(self, keyword=None, count=1):
        
        #블로그는 다음 > 네이버 
        
        if keyword is None:
            return None 
        
        blogList = self.daumApi.searchBlog(keyword, count, 1);
        
        if blogList is None:
            blogList = self.naverApi.searchBlog(keyword, count, 1)
            
        elif len(blogList) < count:
            diff  = count - len(blogList)
            for i in range(0, diff):
                blogList.extend(self.naverApi.searchBlog(keyword, 1, 1))
                
        return blogList; 
        
    def getFoodImage(self, keywordList=None):
        if keywordList is None:
            return None; 
        
        count = 20;
        
        foodImgList = []
        
        tmpImgList = [] 
        for keyword in keywordList:
            tmpImgList = self.naverApi.searchImage(keyword, count, 1);
            for tmpImg in tmpImgList:
                if tmpImg.width >300 or tmpImg.height >300:
                    if tmpImg.width > tmpImg.height:
                        foodImgList.append(tmpImg)
                        break;
                else:
                    print "small food image"
                
                    
        return foodImgList;
    
    
    def getLocalInfoList(self, keyword):
        return  self.naverMapApi.getLocalPlaceList(keyword)


if __name__ == "__main__": 
    openapi = OpenAPIController();
    
    resultDict = openapi.getLocalInfoList(u"롯데리아 명동역점")
           
    print json.dumps(resultDict)
    
        
        
        
         