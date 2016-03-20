# -*- coding: utf-8 -*-
'''
Created on 2013. 8. 14.

@author: deajang
'''
# from topicnzin.dictionary.submatch_key_finder import SubMatchKeyFinder
# from topicnzin.common.utils import toUnicode


'''
     대표단어가 있으면 대치해준다.
     단순 replace해주는기능을 담당한다.
     오타교정을 하거나 축약어를 보정하기위해 사용한다고 보면된다.
     
     {"기본단어" : "오타교정단어"} 로 구성된다.
'''
class TitleWord:
    def __init__(self, data_dict={}):
        self._finddict = data_dict

    
    def __call__(self, word):
        if word in self._finddict:
            return self._finddict[word]
        else:
            return word
        

if __name__ == "__main__":
    title_word = TitleWord({u"캉고국":u"한국"})
    
    print title_word(u"캉고국")
    print title_word(u"기본값")
