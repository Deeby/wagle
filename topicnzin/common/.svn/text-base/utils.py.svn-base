# *-* coding: UTF-8 -*-
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")  # @UndefinedVariable

def leftCut(src, slice_word):    
    if not src or not slice_word:   return None
        
    slice_word  = toUnicode(slice_word)
    src         = toUnicode(src)
    
    if not src.startswith(slice_word):
        return src
            
    start       = len(slice_word)    
    return src[start:len(src)]

def rightCut(src, slice_word):
    if not src or not slice_word:   return None
    
    slice_word  = toUnicode(slice_word)
    src         = toUnicode(src)    
    if not src.endswith(slice_word):
        return src
    
    end       = len(slice_word)    
    return src[0:len(src)-end]    

def toUnicode(word,default=None):
    if not word:
        return default
    if isinstance(word, unicode):
        return word
    elif isinstance(word, list) or isinstance(word, tuple):
        return map(lambda x: toUnicode(x) ,word)
    elif isinstance(word, dict):
        raise AttributeError("sorry!!! toUnicode() is unsupport 'dict' type.")
    else:
        return unicode(word)

def toLens(list_str):
    tmp_sum = 0
    for item_str in list_str:
        tmp_sum += toLen(item_str)
    return tmp_sum
        
def toLen(obj):
    if obj:
        return len(obj)
    else:
        return 0
    
def toStr(word, default=None):
    if not word:
        return default
    if isinstance(word, str):
        return word
    elif isinstance(word, list):
        return "[" +  ", ".join(map(lambda x: toStr(x) ,word)) + "]"
    elif isinstance(word, tuple):
        return "(" +  ", ".join(map(lambda x: toStr(x) ,word)) + ")"
    elif isinstance(word, dict):
        return "{" +  ", ".join(map(lambda k:toStr(k)+":"+toStr(word[k]), word)) + "}"
    else:
        return str(word)
    
""" 
    공백을 제거하고, 소문자로 통일한다
"""
def normalize_key(word):
    word = toUnicode(word)
    word = word.strip()
    word = word.lower()
    return word.replace(" ","")

"""
    싱글턴 관리를 위한 함수이다
"""
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

'''
    파일을 읽는 generator
'''
def fileToData(filepath, func=lambda x:x):
    with codecs.open(filepath,"r",encoding='utf-8') as fp:
        for line in fp:
            if len(line)<=0:
                continue            
            yield func(line.strip())

'''
공백/소문자/구분자를 제외한다 (사전뒤지기위한용도)
'''
def to_index_key(value, key_dict):
    if not value:
        return None
    
    value = toUnicode(value)
    ret = ""
    for ch in value:
        if not key_dict.has_key(ch) and len(ch.strip())>0:
            ret += ch.lower()
         
    return ret
    
    
if __name__ == "__main__":
    print leftCut("한국인은밥","한국인")
    print rightCut("한국인은밥","은밥")
    print leftCut("한국인은밥","마국인")
    print rightCut("한국인은밥","은국")
    print leftCut("한국인은밥",None)
    print rightCut("한국인은밥",None)
    print leftCut("한국인은밥","한국인은밥입니다")
    print rightCut("한국인은밥","한국인은밥입니다")
    print leftCut(None,"한국인")
    print rightCut(None,"은밥")
    print leftCut("한국인","한국인")
    print rightCut("은밥","은밥")
    print leftCut("한국인","헐")
    print rightCut("은밥","후후")