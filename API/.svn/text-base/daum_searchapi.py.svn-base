# -*- coding: utf-8 -*- 
import simplejson, urllib
from api_type import *
from image import *
from blog import *
from mlstripper import *

class DaumSearchAPI:

    apikey = "97a3f99c0d5a6b2fdd60e915668366f63939e1b6"
    search_base = ""
    api_type = API_TYPE.IMAGE  
  

    def searchImage(self, keyword, pageCount, pageNo):
        
        self.search_base ="http://apis.daum.net/search/image"
        self.api_type = API_TYPE.IMAGE

        args ={}
        args.update({
            'result': pageCount, 
            'pageno': pageNo,
            'sort': 'accu'
            }) 

        keyword = unicode(keyword).encode('utf-8')
        print keyword

        result = self.search(keyword, **args)
        return self.parse(self.api_type, result);


    def searchBlog(self, keyword, pageCount, pageNo):
        
        self.search_base ="http://apis.daum.net/search/blog"
        self.api_type = API_TYPE.BLOG

        args ={}
        args.update({
            'result': pageCount, 
            'pageno': pageNo,
            'sort': 'accu'
            }) 

        keyword = unicode(keyword).encode('utf-8')
         

        result = self.search(keyword, **args)
        return self.parse(self.api_type, result);
    
    
    
    
    

    def search(self, query, **args):
        args.update({
            'apikey': self.apikey,
            'q': query,
            'output': 'json'
            })

        url = self.search_base + '?' + urllib.urlencode(args)
         
        
        result = simplejson.load(urllib.urlopen(url))
        return result['channel']

    def parse(self, api_type, result):
        
        if self.api_type is API_TYPE.IMAGE:
            imgList = []
            
            if int(result['totalCount']) > 0:
                
                for item in result['item']:     
                    img = Image()
                    img.image = item['image']
                    img.thumbnail = item['thumbnail']
                    img.width = item['width']
                    img.height = item['height']
                    imgList.append(img)
            else:
                print "image search total count : " + str(result['totalCount']); 


            return imgList; 
            
            
        if self.api_type is API_TYPE.BLOG:
            blogList = [];
            if int(result['totalCount']) > 0:
                for item in result['item']:
                    blog = Blog(); 
                    blog.title = strip_tags(item['title']) 
                    blog.description = strip_tags(item['description']) 
                    blog.link = item['link']
                    blog.bloggername = item['author'] 
                    blogList.append(blog)
            else:
                print "blog search total count : " + str(result['totalCount']); 
                    
                    
            return blogList; 
                    
                    

