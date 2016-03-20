# -*- coding: utf-8 -*- 
 
from api_type import *
from image import *
from blog import *
from xhtmlparser import *; 
from mlstripper import *; 
 
import urllib

class NaverSearchAPI:

    apikey = "776db691996584df9385aa576bd4dcef"
    search_base = "http://openapi.naver.com/search"

    api_type = API_TYPE.IMAGE
    
    xhtmlParser = XHtmlParser(); 

    def searchImage(self, keyword, pageCount, pageNo):
        
        self.search_base ="http://openapi.naver.com/search"
        self.api_type = API_TYPE.IMAGE

        args ={}
        args.update({
            'display': pageCount,
            'start':pageNo, 
            'target': 'image'
            }) 

        keyword = unicode(keyword).encode('utf-8')
        soup = self.search(keyword, **args)
        return self.parse(self.api_type, soup.channel)
        
        
    def searchBlog(self, keyword, pageCount, pageNo):
        self.api_type = API_TYPE.BLOG

        args ={}
        args.update({
            'display': pageCount,
            'start':pageNo, 
            'target': 'blog'
            }) 

        keyword = unicode(keyword).encode('utf-8')
        
        soup = self.search(keyword, **args)
        return self.parse(self.api_type, soup.channel)
        
    def searchLocal(self, keyword, pageCount, pageNo):
        self.api_type = API_TYPE.LOCAL

        args ={}
        args.update({
            'display': pageCount,
            'start':pageNo, 
            'target': 'blog'
            }) 

        keyword = unicode(keyword).encode('utf-8')
        
        soup = self.search(keyword, **args)
        return self.parse(self.api_type, soup.channel)
        


    def search(self, query, **args):
        args.update({
            'key': self.apikey,
            'query': query
             
            })

        url = self.search_base + '?' + urllib.urlencode(args) 
        return self.xhtmlParser.parse(url, 'xml')

    def parse(self, api_type, channel):
         
        
        if self.api_type is API_TYPE.IMAGE:
            
            items = channel.findAll('item')
            imgList = [] 
            for item in items:               
                img = Image() 
                img.image = item.link.contents[0]
                img.thumbnail = item.thumbnail.contents[0]
                img.width = item.sizewidth.contents[0]
                img.height = item.sizeheight.contents[0]
                imgList.append(img)


            return imgList; 
        
        elif self.api_type is API_TYPE.BLOG:
            items = channel.findAll('item')
            blogList = []
            for item in items:
                blog = Blog()
   
                blog.title = strip_tags(item.title.contents[0]);
                blog.link = item.link.contents[0]
                blog.description = strip_tags(item.description.contents[0]) 
                blog.bloggername = item.bloggername.contents[0]
                
                blogList.append(blog)
            
            return blogList;  
        
            
 