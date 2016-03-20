# *-* coding: UTF-8 -*-
'''
Created on 2013. 8. 12.

@author: deajang
'''
from topicnzin.common.utils import toStr

class Token:
    
    def __init__(self, p_word):
        self.word = p_word
        self.index= False
        self.alive = 0
        
#         self.stop = False
#         self.use  = False
    
    @property
    def word(self):
        return self._word
    @word.setter
    def word(self, value):
        self._word = value
    
    @property
    def index(self):
        return self._index
    @index.setter
    def index(self, value):        
        self._index = value
    
    '''
    단어가 의미있는지를 판단하는 숫자이다.
    단계를 건널때마다 의미있는 단어로 판단되면 +1 을 해서 탈락유무를 결정할때 사용한다.
    '''
    @property
    def alive(self):
        return self._alive
    
    @alive.setter
    def alive(self, value):
        self._alive = value
        
#     
#     @property
#     def stop(self):
#         return self._stop
#     
#     @stop.setter
#     def stop(self, value):
#         self._stop = value
#     
#     @property
#     def use(self):
#         return self._use
#     
#     @use.setter
#     def use(self, value):
#         self._use = value
    
    def __repr__(self):
        return "word=%s, index=%s, alive=%d" % (toStr(self.word), toStr(self.index), self.alive) 
    

            