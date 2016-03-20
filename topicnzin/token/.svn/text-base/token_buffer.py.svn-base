#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    N개의 이전 토큰을 보관한다.
    그래서 N개의 조합된 값을 보여준다.
    기본 토큰 버퍼는 5개이다.
    
    TIP:
    "상냥한 눈빛의 떡볶이" 문제이다. 
    문장형태의 상호명의 경우 이미 토큰 단위로 분리되어 있어 추출을 할 수 없다.
    이러한 문제를 해결하기위해 도입된 버퍼 시스템기능이다.
    이 경우 N개의 조합에 의한 명사 추출이 가능해진다.
     
    @author: tost 정민철 (deajang@gmail.com)
"""        
class TokenBuffer:
    def __init__(self, buf_size=5):
        self.iter_index= 0
        self.buffer    = []
        for i in range(buf_size):  # @UnusedVariable
            self.buffer.append("")
            
        self.buf_size  = buf_size
        self.idx       = 0      
        
    # 버퍼에 토큰을 집어 넣는다.
    def add(self, token):
        word = token
        self.buffer[self.idx] = word
        self.idx += 1
        if self.idx >= self.buf_size:
            self.idx = 0    # rotate
        
    # 버퍼에서 조합가능한 텍스트를 만들어 낸다. 리턴은 배열로 리턴된다.     
    def createTokens(self):
        ret = []
        temp = ""
        for idx in reversed(map(lambda x: (x+self.idx)%self.buf_size, range(self.buf_size))):
            if len(temp) > 0 and len(self.buffer[idx])>0: 
                temp = self.buffer[idx] + temp
                ret.append(temp)
            else:
                temp = self.buffer[idx]
        
        return [word for word in reversed(ret)]
        
    
    def generator(self):
        for idx in map(lambda x: (x+self.idx)%self.buf_size, range(self.buf_size)):
            yield self.buffer[idx]
    

    def clear(self):
        del self.buffer
        self.__init__(self.buf_size) 

if __name__ == "__main__":
    test = TokenBuffer()
    test.add("this")
    test.add("IS")
    test.add("NAME")
    test.add("TTTT")
    test.add("yyyyy")
    test.add("nnn")
    print test.createTokens()

    for t in test.generator():
        print t