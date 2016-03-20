#-*- coding: utf-8 -*-
from pymongo import MongoClient  # @UnresolvedImport
from bson.son import SON

class RelationFoods:
    def __init__(self, uri="mongodb://indf:konan415@ds041218.mongolab.com:41218/indf", table_name="test"):
        self._mongo_client = MongoClient(uri)
        self._db = self._mongo_client.get_default_database()
        self._table = table_name
    
    def about(self):
        return self._mongo_client.server_info()
        
    def __del__(self):
        self._mongo_client.close()

    def add(self, key, regdate, food=[], shop=[], local=[]):
        self._db[self._table].insert({"docid":key, "regdate":regdate, "food":food, "shop":shop, "local":local})

    def food2local(self, keyword):
        return RelationFoods.result_filter(self._db[self._table].aggregate([{"$match" : {"food": keyword}},{"$unwind" : "$local"},{"$group" : { "_id"   : "$local", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : 50 }] ))

    
    def food2food(self, keyword):
        return RelationFoods.result_filter(self._db[self._table].aggregate([{"$match" : {"food": keyword}},{"$unwind" : "$food"},{"$group" : { "_id"   : "$food", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : 50 }] ))

    def food2shop(self, keyword):
        return RelationFoods.result_filter(self._db[self._table].aggregate([{"$match" : {"food": keyword}},{"$unwind" : "$shop"},{"$group" : { "_id"   : "$shop", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : 50 }] ))
    
    def shop2food(self, keyword):
        return RelationFoods.result_filter(self._db[self._table].aggregate([{"$match" : {"shop": keyword}},{"$unwind" : "$food"},{"$group" : { "_id"   : "$food", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : 50 }] ))
    
    def shop2shop(self, keyword):
        return RelationFoods.result_filter(self._db[self._table].aggregate([{"$match" : {"shop": keyword}},{"$unwind" : "$shop"},{"$group" : { "_id"   : "$shop", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : 50 }] ))
    
    def shop2local(self, keyword):
        return RelationFoods.result_filter(self._db[self._table].aggregate([{"$match" : {"shop": keyword}},{"$unwind" : "$local"},{"$group" : { "_id"   : "$local", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : 50 }] ))
    
    
    def local2local(self, keyword):
        return RelationFoods.result_filter(self._db[self._table].aggregate([{"$match" : {"local": keyword}},{"$unwind" : "$local"},{"$group" : { "_id"   : "$local", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : 50 }] ))
    
    def local2shop(self, keyword):
        return RelationFoods.result_filter(self._db[self._table].aggregate([{"$match" : {"local": keyword}},{"$unwind" : "$shop"},{"$group" : { "_id"   : "$shop", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : 50 }] ))

    def local2food(self, keyword):
        return RelationFoods.result_filter(self._db[self._table].aggregate([{"$match" : {"local": keyword}},{"$unwind" : "$food"},{"$group" : { "_id"   : "$food", "count" : {"$sum": 1} }  }, {"$sort":SON([("count",-1)])},  { "$limit" : 50 }] ))

    
    @staticmethod
    def result_filter(result):
        if u'ok' in result and u'result' in result:
            return result[u'result']
        return []
  
    def test(self):
        return self._db.name
    
    
        
        
# - connect
# ./mongo ds041218.mongolab.com:41218/indf -u indf -p konan415
# 
# - uri
# 

if __name__ == "__main__":
    test = RelationFoods(table_name="wagle")    
#     print test.test()
    result = test.food2food(u"곱창")
    for row in result:        
        print row[u"_id"] , row[u"count"]
#     test.add("2","20130505",[u"밥"],           [u"아웃백"],[u"서울"])
#     test.add("3","20130505",[u"밥",u"국",u"떡볶이"],      [u"천국나라",u"김밥천국"],[u"서울","연신내"])
#     test.add("4","20130505",[u"비빔밥"],       [u"본비빔밥"],[u"서울"])
#     test.add("5","20130505",[u"떡볶이"],       [u"죠스떡볶이"],[u"서울","종로"])
#     test.add("6","20130505",[u"밥","비빔밥"],  [u"가정백반"],[u"서울","종로"])
#     test.add("7","20130505",[u"밥"],           [u"가정백반"],[u"분당","정자"])
#     test.add("8","20130505",[u"밥"],           [u"가정백반",u"김밥천국"],[u"서울",u"강남"])
    print "end"
