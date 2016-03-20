# *-* coding: UTF-8 -*-
'''
Created on 2013. 8. 30.

@author: deajang
'''
from API.wagle_topic import wagle_group, isFood, isLocal, isShop, wagle_token,\
    wagle_group_top_twitter
from API.friend_word import FriendWord
from topicnzin.common.utils import toUnicode, toStr
from API.daum_twitter import DaumTwitter


if __name__ == '__main__':
    """
        1. 토픽 사용하기 
    """
#     for word in wagle_token("안녕하세요. 저는 오빠닭에서 갈릭치킨을 먹고 싶어요. 치킨 치킨 그것은 운명 서울이다."):
#         print word
#         
#     
#     print "~~~~~~~~~"
#     for words in wagle_group(["안녕하세요. 저는 오빠닭에서 갈릭치킨을 먹고 싶어요. 치킨 치킨 그것은 운명 ","치킨"]):
#         word, word_cnt, doc_cnt = words
#         
#          
#         print word, word_cnt, doc_cnt
#         print "food" , isFood(word)
#         print "local", isLocal(word)
#         print "shop", isShop(word)
#         print ""
        
    """
        2. 연관단어 검색 현재 지역데이터는 안뽑혔는지 안나옴. 
    """
    friendword = FriendWord()
    for results in friendword.food2shop(toUnicode("파스타"), 10):
# #     for results in friendword.shop2shop(toUnicode("피자헛"), 10):    
    #for results in friendword.shop2food(toUnicode("제인스 피키 피자"), 10):
# #     for results in friendword.food2food(toUnicode("치킨"), 10):÷
        word , cnt = results
        print "단어: " , word, " , 갯수:", cnt

        
    """
        3.다음  트위터 검색결과를 의미한다. 
        하나의 단어를 검색하는 메소드와 여러개의 메소드를 검색하는 메소드 두개가 있다.
        pub_date
        user_name
        doc_id
        doc_url
        thumbnail_image
        text
    """
    
#     # 여러개의 단어 (동일한 doc_id 값 처리를 해서 던져줌)
#     for idx, row in  enumerate(DaumTwitter.searchs(["맛집","먹고싶다"], 50)): # limit 기본은 30개, 50개를 가져옴.
#         print  idx+1 , "] date=" , row["pub_date"] ,",user_name", row["user_name"],  ", doc_id, =", row["doc_id"] , ", doc_url=", row["doc_url"], ", thumbnail_image=", row["thumbnail_image"], ", text=", row["text"]
#         
#     # 단어 하나만 
#     for idx, row in  enumerate(DaumTwitter.search("맛집", 50)): # limit 기본은 30개, 50개를 가져옴.
#         print  idx+1 , "] date=" , row["pub_date"] ,",user_name", row["user_name"],  ", doc_id, =", row["doc_id"] , ", doc_url=", row["doc_url"], ", thumbnail_image=", row["thumbnail_image"], ", text=", row["text"]
        
    
    """
        4. 트위터에서 언급된 최근 데이터의 음식과 상호명, 지역을 리턴받는다.
        단 걸러낼땐 isFood    isShop    isLocal 로 걸러내자.
    """
#     for words in wagle_group_top_twitter():  # 음식,상호명, 지역 모두
#     for words in filter(lambda x: isFood(x[0]), wagle_group_top_twitter()):  # 음식만 필터링함.
#     for words in sorted( filter(lambda x: isFood(x[0]), wagle_group_top_twitter()) , key=lambda a : a[2], reverse=True):  # 음식만 필터링함.    
#         word, word_cnt, doc_cnt = words
#           
#         print word, word_cnt, doc_cnt
#         print "food" , isFood(word)
#         print "local", isLocal(word)
#         print "shop", isShop(word)
#         print ""

    print "OK"