# *-* coding: UTF-8 -*-
'''
Created on 2013. 8. 12.

@author: deajang
'''
import unittest
from token import Token
from topicnzin.token.tokenizer import Tokenizer
class TokenizerTestCase(unittest.TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer([",","'","\",",".","ㅋ","ㅎ"])
        
    def runTest(self):
        list = []  # @ReservedAssignment
        for word in self.tokenizer("사과ㅋ바나나 키위"):
            list.append(word)
        assert len(list) == 3
        assert list[0] == "사과"
        assert list[1] == "바나나"
        assert list[2] == "키위"
        
class TokenTestCase(unittest.TestCase):
    def setup(self):
        self.token = Token("Bana na과일")   
        
    def runTest(self):
        assert self.token.index== u"banana과일"
        assert self.token.word == u"Bana na과일"
        
        