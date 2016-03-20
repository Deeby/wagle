# *-* coding: UTF-8 -*-
'''
Created on 2013. 8. 12.

@author: deajang
'''
import re
from topicnzin.common.utils import toUnicode, toLen, rightCut, leftCut, toLens
from topicnzin.token.token import Token
from topicnzin.token.token_slice import TokenSlice
from topicnzin.token.token_buffer import TokenBuffer

class Tokenizer(TokenSlice):
    
    def __init__(self, delemeters=[]):
        TokenSlice.__init__(self, delemeters)
        self._buffer = TokenBuffer()    # 띄어쓰기가 되어있는 문장형 값에서 '구' 데이터 추출  
        
            
    '''
        main
    '''
    def __call__(self, text):
        self._buffer.clear()
        for word in self.split(text): 
#             print ""
            if toLen(word)<=0: continue
            index = self.to_index_key(word)
            use  = self.use_dict.exactMatch(index)  #사전태깅
            tail = self.tail_dict.exactMatch(index) # 꼬리
            head = self.head_dict.exactMatch(index) # 머리 
            start_long = self.head_dict.startLongMatch(index)
            end_long   = self.tail_dict.endLongMatch(index)
            use_left_long= self.use_dict.startLongMatch(index)
            
            
            
#            print head , use, tail, word, index, self.head_dict.startLongMatch(index) ,self.tail_dict.endLongMatch(index)
            if toLen(index)>=2 and toLen(index)<=8 and toLens((tail, head, use, start_long, end_long,))==0: # 2~8글자의 완벽한글자는 기냥추출
#                 print "1"
                yield self.createToken(word)
            elif toLen(index)>=2 and toLen(index)<=8 and toLens((tail, head, use, end_long,))==0 and toLen(start_long)>=2: # 앞쪽에 아는 단어가 있다면
#                 print "2"
                tail_word = leftCut(index, use_left_long)
                yield self.createToken(use_left_long)
                for slice_word in TokenSlice.slice_word(self, tail_word):
                    yield self.createToken(slice_word)
            elif toLen(index)>=2 and toLen(index)<=8 and toLens([tail, head, use, start_long])==0 and toLen(end_long)>=1: # 잘 모르겠고... 꼬리글자 있으면 무조건 제거시도
#                 print "3"
                sum_useleftlong_end_long = toLen([use_left_long,end_long])
                index_len = toLen(index)  
                if sum_useleftlong_end_long == index_len: # 이상적인 조합.
#                     print "3-1"
                    yield self.createToken(use_left_long)
                    yield self.createToken(end_long)
                elif sum_useleftlong_end_long > index_len: #  over ? 그러면 꼬리가 잘못 분석될 확률이 높음. (냉면은 --> 냉면 , 면은 )
#                     print "3-2"
                    tail_word = leftCut(index, use_left_long)
                    yield self.createToken(use_left_long)
                    yield self.createToken(tail_word)
                elif sum_useleftlong_end_long < index_len: # under? 그럼 완벽한 단어를 못찾은거임  (미도리마의 -> 미도리 ,(마?) 의 )
#                     print "3-3"
                    
                    find_word = rightCut(index, end_long)
#                     print index
#                     print end_long
#                     print find_word
                    yield self.createToken(find_word)
                    yield self.createToken(end_long)
            elif toLen(index)>1 and toLens((tail, head, use, end_long,start_long,use_left_long))>0:
#                 print "4"
                for slice_word in TokenSlice.slice_word(self, word):
                    yield self.createToken(slice_word)
            else:
#                 print "5"
                yield self.createToken(word)
                
            # 버퍼
            self._buffer.add(word)
            for buff_word in self._buffer.createTokens():
#                 print "buff L" , buff_word 
                index = self.to_index_key(buff_word)
                use  = self.use_dict.exactMatch(index)  #사전태깅
                tail = self.tail_dict.endLongMatch(index) # 꼬리
                head = self.head_dict.startLongMatch(index) # 머리
                minsize = 4 # 합쳐진 데이터의 오분석을 최소화 하기위해 minsize 글자보다 커야한다.
                if  toLen(use)>=minsize:
#                     print "buf: use > minsize..." , use
                    yield self.createToken(use)
                    break
                
                if toLen(tail)>0 and toLen(head)<=0:
                    use  = self.use_dict.exactMatch(self.to_index_key(rightCut(index, tail)))
#                     print "buf: tail cut ... " , use
                    if toLen(use)>=minsize: 
                        yield self.createToken(use)
                        break
                
                if toLen(tail)<=0 and toLen(head)>0:
                    use  = self.use_dict.exactMatch(self.to_index_key(leftCut(index, head)))
#                     print "buf: head cut..." , use
                    if toLen(use)>=minsize : 
                        yield self.createToken(use)
                        break
                
                if toLen(tail)>0 and toLen(head)>0:
                    use  = self.use_dict.exactMatch(leftCut(rightCut(index, tail),head))
#                     print "buf: head + tail cut ... " , use
                    if toLen(use)>=minsize : 
                        yield self.createToken(use)
                        break                    
                    
                    
    

    def split(self, text):
        text = toUnicode(text)
        if not text: 
            yield ""
            return
         
        for first_word in text.split():
            if Tokenizer.isUrlPattern(first_word) or Tokenizer.isTwitterId(first_word):
                continue
            
            temp = ""
            for ch in first_word:
                if self.has_delemter(ch):  # 토큰으로 리턴될값.
                    if len(temp) > 0:
                        yield temp
                        temp = ""
                else:
                    temp += ch    
            if len(temp) > 0: #마지막 토큰을 의미한다
                yield temp     

    def createToken(self, word):
        token = Token(word)
        token.index = self.to_index_key(word)
        token.alive  = token.alive+1 if self.use_dict.exactMatch(token.index) else token.alive
        return token
    
    @staticmethod
    def isUrlPattern(word): #URL은 지운다
        return word and (word.startswith("http://") or word.startswith("https://"))
    
    @staticmethod
    def isTwitterId(word):  #트윗ID형태도 지운다.
        return word and word.startswith("@") and bool(re.match("@[a-zA-Z][a-zA-Z0-9_]+", word))
    
    
if __name__ == "__main__":
    pass