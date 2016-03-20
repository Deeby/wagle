# -*- coding:utf-8 -*-
'''
Created on 2013. 8. 12.

@author: deajang
'''
from topicnzin.common.utils import toUnicode,leftCut,toLen, to_index_key
from topicnzin.dictionary.submatch_key_finder import SubMatchKeyFinder

'''
    띄어쓰기가 안된 텍스트를 조각내는 기능을 담당한다.
    
    사전은 크게 3개로 구분된다.
    
    WORD = head{0,1} + use{1,N} + tail{0,1}
           head{0,1} + WORD{1,N} + tail{0,1}
     
'''
class TokenSlice(object):
    def __init__(self, delemeters={}):
        self._delemeters = {toUnicode(key):True for key in delemeters}
        self.use_dict  = {}
        self.tail_dict = {}
        self.head_dict = {}
    
    @property
    def use_dict(self):
        return self._use_dict

    @use_dict.setter
    def use_dict(self, value):
        self._use_dict = SubMatchKeyFinder(value)
    
    @property
    def tail_dict(self):
        return self._tail_dict
    
    @tail_dict.setter
    def tail_dict(self, value):
        self._tail_dict = SubMatchKeyFinder(value)
    
    @property
    def head_dict(self):
        return self._head_dict
    
    @head_dict.setter
    def head_dict(self,value):
        self._head_dict = SubMatchKeyFinder(value)

    '''
    공백/소문자/구분자를 제외한다 (사전뒤지기위한용도)
    '''
    def to_index_key(self,value):
        return to_index_key(value, self._delemeters)
    

    '''
    구분자 캐릭터유무
    '''
    def has_delemter(self, delemeter):        
        return self._delemeters.has_key(delemeter)
        
    
    def slice_word(self, word):
        result = []
        self.__recursion_slice_word(word,result)
        return result
    
    def __recursion_slice_word(self, word, data=[]):
        current_word = self.to_index_key(word)
        ret = data
        if toLen(word)<=0:
            return ret 
        
        # head or tail
        center = self.use_dict.startLongMatch(current_word)
        head = self.head_dict.startLongMatch(current_word)
        tail = self.tail_dict.startLongMatch(current_word)
        if  toLen(center) <= 1 and toLen(head)>=1 and toLen(head)>=toLen(tail) :
            ret.append("<"+head)
            current_word = leftCut(current_word,head)
        if  toLen(center) <= 1 and toLen(tail)>=1 and toLen(head)<toLen(tail) :
            ret.append(">"+tail)
            current_word = leftCut(current_word,tail)                
            
        # center            
        center = self.use_dict.startLongMatch(current_word)
        if toLen(center)>0:
            ret.append("@"+center)
            current_word = leftCut(current_word,center)
        
        
        if len(current_word) >=3:
            center = self.use_dict.startLongMatch(current_word)
            head = self.head_dict.startLongMatch(current_word)
            tail = self.tail_dict.startLongMatch(current_word)
            if toLen(center)>=1 or toLen(head)>=2 or toLen(tail)>=2: #다음에 사전에서 추출가능한 패턴이라면 재귀돌림.
                self.__recursion_slice_word(current_word, ret) 
            else:
                start_idx = self._right_offset_dict_index_of_(current_word)
                slice_word= current_word[0:start_idx] if start_idx > 0 else None
                if slice_word:
                    ret.append("/"+slice_word)                    
                    current_word = leftCut(current_word, slice_word)
                    self.__recursion_slice_word(current_word, ret)
                else:
                    ret.append("."+current_word)
                    current_word = ""
        elif len(current_word)>0:
            ret.append(current_word)
            current_word = ""
        
                                        
    
    def _right_offset_dict_index_of_(self, word):
        if not word: return -1
        for start in range(1,len(word)-1):
            find_word = self.use_dict.startLongMatch(word[start:len(word)])
            if find_word:    return start
            
            find_word = self.head_dict.startLongMatch(word[start:len(word)])
            if find_word:    return start
            
        return -1
        
        
        
            
        
if __name__ == "__main__":
    pass
#     list_token_delemeter = fileToData("/Users/deajang/Documents/Aptana Studio 3 Workspace/topicnzin/dict_data/token.txt")
#     tokenSlice = TokenSlice(list_token_delemeter)
#     
#     dict_use     = {tokenSlice.to_index_key(key):True for key in fileToData("/Users/deajang/Documents/Aptana Studio 3 Workspace/topicnzin/dict_data/food.txt")
# #     dict_stop    = {tokenSlice.to_index_key(key):True for key in fileToData("/Users/deajang/Documents/Aptana Studio 3 Workspace/topicnzin/dict_data/stop.txt")}
#     dict_head    = {tokenSlice.to_index_key(key):True for key in fileToData("/Users/deajang/Documents/Aptana Studio 3 Workspace/topicnzin/dict_data/head.txt")}
#     dict_tail    = {tokenSlice.to_index_key(key):True for key in fileToData("/Users/deajang/Documents/Aptana Studio 3 Workspace/topicnzin/dict_data/tail.txt")}
#     
#     
# #     tokenSlice.stop_dict = dict_stop
#     tokenSlice.use_dict  = dict_use
#     tokenSlice.head_dict = dict_head
#     tokenSlice.tail_dict = dict_tail
#     
# #     print toStr(tokenSlice.slice_word("비빔밥먹으려 여기까지와? ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 나 집에서랑 학교 급식서 나온 비빔밥외에는 따로 음식점서 먹어본적없는데 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 흥 그럴리가요! 그리고 전주비빔밥보다는 이번주비빔밥이 더 맛있...(...)"))
# #     print toStr(tokenSlice.slice_word(" 비빔밥외에는 따로 음식점서 먹어본적없는데 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 흥 그럴리가요! 그리고 전주비빔밥보다는 이번주비빔밥이 더 맛있...(...)"))
#     print toStr(tokenSlice.slice_word("@AhnSB_bot 응! 어제 그 닭강정.....인데 왜 맛있눈거 올려....그거 지금 먹고있어?ㅠㅠ"))
#         