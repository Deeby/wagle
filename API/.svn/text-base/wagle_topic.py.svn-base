# -*- coding:utf-8 -*-
'''
Created on 2013. 8. 30.

@author: deajang
'''
from topicnzin.engine.shared_data import SharedData
from topicnzin.engine.bit_mask import BitMask
from topicnzin.filter.title_word import TitleWord
from topicnzin.filter.use_filter import UseFilter
from topicnzin.token.tokenizer import Tokenizer
from topicnzin.engine.word_counter import WordCounter
from API.daum_twitter import DaumTwitter

# sysdict load
__shared  = SharedData()
__shared.load()

# __tokenizer setting
__tokenizer = Tokenizer(__shared.token_delemeter())
__tokenizer.head_dict = __shared.getfilteredDict(BitMask.head())
__tokenizer.tail_dict    = __shared.getfilteredDict(BitMask.tail() | BitMask.verb()) 
__tokenizer.use_dict   = __shared.getfilteredDict(BitMask.use_all())

# filter 
__titleFilter             = TitleWord(__shared.title_dict())
__multiFilter           = UseFilter(__shared.getfilteredDict(BitMask.food()  | BitMask.shop() | BitMask.local()))
        
'''
멀티펑션을 실행한다.
'''
def __chain_filter(word, *funcs):
    chain_word = word
    for func in funcs:
        chain_word = func(chain_word)
        if not chain_word:
            return None
    return chain_word

'''
    문서를 넣으면 토큰화 해준다.
    단,  불필요한 토큰은 제외한다.
    
    return word
'''
def wagle_token(text):
    for line in text.split():
        for word in __tokenizer(line):
            output = __chain_filter(word.index, __titleFilter, __multiFilter)
            if not output:
                continue 
                                             
            yield word.index

'''
문서 리스트를 넘겨주면 카운팅 해서 필요한 단어만 던져준다.

return  (단어 , 단어빈도, 문서빈도) 
'''
def wagle_group(generator_text=[]):
    if isinstance(generator_text, str) or isinstance(generator_text,unicode):
        generator_text = (generator_text,)
    
    counter = WordCounter(True)
    for text in generator_text:
        for word in wagle_token(text):
            counter.add(word)
        counter.groupEnd()      
        
    cntDict = counter.toDict()
    for key in cntDict:
        yield (key, cntDict[key][0],cntDict[key][1], )
        
    
def isFood(word):
    return bool(word in __shared.getfilteredDict(BitMask.food()))

def isShop(word):
    return bool(word in __shared.getfilteredDict(BitMask.shop()))

def isLocal(word):
    return bool(word in __shared.getfilteredDict(BitMask.local()))
    
def wagle_group_top_twitter(limit=500):
    seed_keyword = ["강추","추천","먹네","맛집","먹고","맛있","땡긴다", "먹을","먹자", "맛난", "마시고싶다","마시자", "음식" ,"요리", "폭풍흡입", "푸짐", "무한리필", "사줘", "냠냠"]
    twitter_contens = []
    for row  in DaumTwitter.searchs(seed_keyword, limit):
        twitter_contens.append(row['text'])
    
    for item in wagle_group(twitter_contens):
        yield item


if __name__ == "__main__":
    for word in wagle_token("안녕하세요\n 저는 오빠닭에서 치킨을 먹고 싶은 사람입니다."):
        print word
        
    print "~~~~~~~~~~~~~~"
    
    for obj in wagle_group(["안녕하세요\n 저는 오빠닭에서 치킨을 먹고 싶은 사람입니다.", "치킨먹고 싶다. 꼬꼬닭 짜파게티.", "배고프당 치킨 치킨 "]):
        word , word_cnt, doc_cnt =  obj
        print word, doc_cnt, word_cnt
        print "음식?" , isFood(word)
        print "가게?" , isShop(word)
        print "지역?" , isLocal(word)
        print ""
    
        