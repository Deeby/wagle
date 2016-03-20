'''
Created on 2013. 8. 14.

@author: deajang
'''
from topicnzin.dictionary.submatch_key_finder import SubMatchKeyFinder

class UseFilter:
    def __init__(self, data_dict={}):
        self._finddict = SubMatchKeyFinder(data_dict)
    
    def __call__(self, word):
        if not word:
            return None
        if self._finddict.exactMatch(word):
            return word
        else:
            return None