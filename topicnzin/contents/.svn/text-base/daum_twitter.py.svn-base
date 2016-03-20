# -*- coding: utf-8 -*-
import urllib2
import json
'''
Created on 2013. 8. 10.

@author: deajang
'''

class DaumTwitter(object):
    seed_url = u"http://m.search.daum.net/qsearch?w=realtime&search_option=mobile&n={{limit}}&p=0&enddate=&begindate=&q={{kwd}}&uk=null&viewtype=json"
    
    '''
    classdocs
    '''
    @staticmethod
    def search(keyword, limit=30):
        if not isinstance(keyword, unicode):
            keyword = unicode(keyword)
                
        find_url = DaumTwitter.seed_url.replace("{{kwd}}", keyword).replace("{{limit}}",str(limit))
        response = urllib2.urlopen(find_url)
        json_data = response.read()
        no_filter = json.loads(json_data)[u'RESULT'][u'REALTIME'][u'r'][u'ds'][u'data']
        
        return map(lambda x: {"text":str(x[u'text'].replace("<b>","").replace("</b>","")), "docid":str(x[u'docid']), "pub_date":str(x[u'pub_date']) }, no_filter) 
    
    
    @staticmethod
    def searchs(keyword_list):
        unique_dict ={} #중복되는 docid 를 제거해준다.
        for keyword in keyword_list:
            for result in DaumTwitter.search(keyword):
                if not unique_dict.has_key(result["docid"]):
                    unique_dict[result["docid"]] = result
        
        return [val for val in sorted(unique_dict.values(), key=lambda result : result["pub_date"], reverse=True)]
    
                     
                
    
if __name__ == "__main__":
    result = DaumTwitter.searchs([u"맛집",u"먹고싶다",u"맛있겠다",u"맛있",u"맛있져",u"땡긴다",u"먹을까",u"먹자",u"먹을래",u"먹어"])
    cnt = 0
    for item in result:
#         print "%s" %  (item["text"])
        cnt += 1
        print "%d [%s] %s : %s" %  (cnt , item["docid"], item["pub_date"], item["text"])
        
 