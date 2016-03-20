# -*- coding: UTF-8 -*-
from pymongo import MongoClient  # @UnresolvedImport
from bson.son import SON  # @UnresolvedImport
class FriendWord:
    def __init__(self, uri="mongodb://indf:konan415@ds041218.mongolab.com:41218/indf", table_name="wagle2", db="indf"):
        self._mongo_client = MongoClient(uri)
        
        self._db = self._mongo_client[db]
        self._table = table_name
    
    def about(self):
        return self._mongo_client.server_info()
        
    def __del__(self):
        self._mongo_client.close()

    def add(self, key, regdate, food=[], shop=[], local=[]):
        self._db[self._table].insert({"docid":key, "regdate":regdate, "food":food, "shop":shop, "local":local})

    def food2local(self, keyword, limit=50):
        return FriendWord.result_filter(self._db[self._table].aggregate([{"$match" : {"food": keyword}},{"$unwind" : "$local"},{"$group" : { "_id"   : "$local", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : 50 }] ))

    
    def food2food(self, keyword, limit=50):
        return FriendWord.result_filter(self._db[self._table].aggregate([{"$match" : {"food": keyword}},{"$unwind" : "$food"},{"$group" : { "_id"   : "$food", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : limit }] ))

    def food2shop(self, keyword, limit=50):
        return FriendWord.result_filter(self._db[self._table].aggregate([{"$match" : {"food": keyword}}, {"$unwind" : "$shop"}, {"$group" : { "_id"   : "$shop", "count" : {"$sum": 1} }  }, {"$sort":SON([("count", -1)])}, { "$limit" : limit }]))
    
    def shop2food(self, keyword, limit=50):
        return FriendWord.result_filter(self._db[self._table].aggregate([{"$match" : {"shop": keyword}},{"$unwind" : "$food"},{"$group" : { "_id"   : "$food", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : limit }] ))
    
    def shop2shop(self, keyword, limit=50):
        return FriendWord.result_filter(self._db[self._table].aggregate([{"$match" : {"shop": keyword}},{"$unwind" : "$shop"},{"$group" : { "_id"   : "$shop", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : limit }] ))
    
    def shop2local(self, keyword, limit=50):
        return FriendWord.result_filter(self._db[self._table].aggregate([{"$match" : {"shop": keyword}},{"$unwind" : "$local"},{"$group" : { "_id"   : "$local", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : limit }] ))
    
    
    def local2local(self, keyword, limit=50):
        return FriendWord.result_filter(self._db[self._table].aggregate([{"$match" : {"local": keyword}},{"$unwind" : "$local"},{"$group" : { "_id"   : "$local", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : limit }] ))
    
    def local2shop(self, keyword, limit=50):
        return FriendWord.result_filter(self._db[self._table].aggregate([{"$match" : {"local": keyword}},{"$unwind" : "$shop"},{"$group" : { "_id"   : "$shop", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : limit }] ))

    def local2food(self, keyword, limit=50):
        return FriendWord.result_filter(self._db[self._table].aggregate([{"$match" : {"local": keyword}},{"$unwind" : "$food"},{"$group" : { "_id"   : "$food", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : limit }] ))

    
    @staticmethod
    def result_filter(result):
        if u'ok' in result and u'result' in result:
            rows = result[u'result']
            return [ (item["_id"] , item["count"],) for item in rows]

        
        return (None,0,)
  
    def test(self):
        return self._db.name


'''
Created on 2013. 8. 30.

@author: deajang
'''

if __name__ == '__main__':
    pass
