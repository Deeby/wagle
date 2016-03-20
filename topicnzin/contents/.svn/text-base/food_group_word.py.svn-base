# -*- coding:utf-8 -*-
from pymongo import MongoClient
from bson.son import SON
class FoodGroupWord:
    def __init__(self, host="localhost", port=27017, database="wagledb"):
        client = MongoClient('mongodb://'+str(host)+':'+str(port)+'/')
        self._db = client[database]
        self._collection = self._db['food_group_word']

    def add(self, docid, food=[], shop=[], local=[]):
        row = {"docid":docid, "food":food, "shop":shop,"local":local}
        self._collection.insert(row)

    def find(self, find_field, find_word, output_field):
        if not find_field in ["food","shop","local"] or not output_field in ["food","shop","local"]:
            raise "field name error"

        return self._collection.aggregate(self.__create_match(find_field, find_word, output_field))

    def __create_match(self, find_field, find_word, output_field):
        output_field = u"$"+output_field
        return [{"$match" : {find_field: find_word}},
                                    {"$unwind" : output_field},
                                    {"$group" : { "_id"   : output_field, "count" : {"$sum": 1} }  },
                                    {"$sort":SON([("count",-1)])}]

    def show_tables(self):
        self._db.collection_names()


if __name__ == '__main__':
    test_object = FoodGroupWord(host="indf.net", database="test")
    test_object.show_tables()
    print test_object.find("local",u"서울","food")
    # test_object.add("123",u["테스트"])

    # __insert( {"docid":1234, "food":[u" 냉면", u"비빔냉면"], "shop":[u"우레옥", u" 평양면옥"],"local":["서울","을지로"]})


    print "end."


