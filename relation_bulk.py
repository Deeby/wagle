# -*- coding:utf-8 -*-
'''
Created on 2013. 8. 27.

@author: deajang
'''
from topicnzin.contents.database_contents import DataBaseContents
from topicnzin.contents.relation_foods import RelationFoods
from topicnzin.engine.shared_data import SharedData
from topicnzin.engine.bit_mask import BitMask
from topicnzin.filter.title_word import TitleWord
from topicnzin.filter.use_filter import UseFilter
from sets import Set
from topicnzin.common.utils import toUnicode, toStr
from topicnzin.token.tokenizer import Tokenizer


#필터관련 함수를 여러개 호출한다 
def chain_filter(word, *funcs):
    chain_word = word
    for func in funcs:
        chain_word = func(chain_word)
        if not chain_word:
            return None
    return chain_word

#db loop
def generator_database(start_num, end_num):
    database = DataBaseContents()    
    for row in database.documents(range(start_num, end_num)):
        yield row
            

        
    
if __name__ == '__main__':
    
    shared = SharedData()
    shared.load()    
    
    # tokenizer
    tokenizer = Tokenizer(shared.token_delemeter())
    tokenizer.head_dict = shared.getfilteredDict(BitMask.head())
    tokenizer.tail_dict = shared.getfilteredDict(BitMask.tail() | BitMask.verb()) 
    tokenizer.use_dict  = shared.getfilteredDict(BitMask.use_all())
    titleFilter         = TitleWord(shared.title_dict())
    myWordFilter        = UseFilter(shared.getfilteredDict(BitMask.food() | BitMask.shop() | BitMask.local()))
    
    food_dict = shared.getfilteredDict(BitMask.food())
    shop_dict = shared.getfilteredDict(BitMask.shop())
    local_dict= shared.getfilteredDict(BitMask.local())
    
    
    #mongo = RelationFoods(table_name="wagle")
    mongo = RelationFoods(table_name="wagle2")
    
    for row in generator_database(1,267526):
        if not row:
            continue
             
        food_set = Set()
        shop_set = Set()
        local_set = Set()
            
        for word in tokenizer(row["title"] +" " + row["contents"]):
            output_word =  chain_filter(word.index, titleFilter, myWordFilter)
            if not output_word:
                continue
            
            find_key = shared.to_index_key(toUnicode(output_word))
            if find_key in food_dict:
                food_set.add(find_key)
            if find_key in shop_dict:
                shop_set.add(find_key)
            if find_key in local_dict:
                local_set.add(find_key)
        
        if len(food_set) + len(shop_set) + len(local_set) > 0:
#             print row["docid"], row["regdate"], [toStr(item) for item in food_set], [toStr(item) for item in shop_set], [toStr(item) for item in local_set]
#         else:
#             print "else"
            mongo.add(row["docid"], row["regdate"], [toStr(item) for item in food_set], [toStr(item) for item in shop_set], [toStr(item) for item in local_set])

        