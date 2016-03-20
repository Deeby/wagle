'''
Created on 2013. 8. 15.

@author: deajang
'''
from sets import Set

class WordCounter(object):
    '''
    classdocs
    '''
    def __init__(self, group_count=False):
        self._counter = {}
        self._set = Set()
        self._groupcount = group_count
    
    def add(self, word):
        if word in self._counter:
            wc, dc = self._counter[word]
            wc += 1
            self._counter[word] = (wc, dc)
        else:
            self._counter[word] = (1,0)
        
        if self._groupcount: self._set.add(word)
            
    
    def groupEnd(self):
        for word in self._set:
            wc, dc = self._counter[word]
            dc += 1
            self._counter[word] = (wc, dc)
        self._set.clear()
        
    def keys(self):
        return self._counter.keys()
    
    def values(self):
        return self._counter.values()
    
    def count(self):
        return len(self._counter)
    
    def get(self, key):
        return self._counter[key]
    
    def toDict(self):
        return self._counter
    
    
    def __repr__(self):
        ret = ""
        for key in self.keys():
            ret += "word=%s count=%d group_count=%d\n" % (key, self.get(key)[0], self.get(key)[1])
        return ret

if __name__ == "__main__":
    counter = WordCounter(True)
    counter.add("word")
    counter.add("word")
    counter.groupEnd()
    
    counter.add("11")
    counter.add("112")
    counter.add("11")
    counter.add("112")
    counter.add("11")
    counter.add("word")
    counter.groupEnd()
    
    print counter