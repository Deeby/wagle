# -*- coding:utf-8 -*-
"""
    주제어 추출기 시스템의 필수 데이터를 로딩하는 작업이 필요하다.
"""
import os 
from topicnzin.common.utils import singleton, fileToData, toUnicode,\
    to_index_key
from topicnzin.dictionary.bitmask_dict import BitmaskDict
from topicnzin.engine.bit_mask import BitMask
@singleton
class SharedData:
    def __init__(self, rootpath=os.getcwd()):
        self._config = {
                            "VERSRION"      : "0.0.1", 
                            "AUTHOR"        : "deajang",
                            "root.path"     : rootpath,
                            "dict.delemeter": "token.txt",
                            "dict.stop"     : "stop.txt",
                            "dict.title"    : "title.txt",
                            "dict.use"      : [
                                                {"path":"food.txt" ,        "bit":BitMask.food()},
                                                {"path":"default.txt",      "bit":BitMask.default()},
                                                {"path":"head.txt",         "bit":BitMask.head()},
                                                {"path":"local.txt",        "bit":BitMask.local()},
                                                {"path":"shop.txt",         "bit":BitMask.shop()},
                                                {"path":"tail.txt",         "bit":BitMask.tail()},
                                                {"path":"mood.txt",         "bit":BitMask.mood()},
                                                {"path":"verb.txt",         "bit":BitMask.verb()},
                                                {"path":"who.txt",          "bit":BitMask.who()},
                                                {"path":"day.txt",          "bit":BitMask.day()},
                                                {"path":"sensitive_false.txt",  "bit":BitMask.false()},
                                                {"path":"sensitive_true.txt",   "bit":BitMask.true()},
                                                {"path":"name.txt",             "bit":BitMask.name()},
                                              ]
                        }
        self._token_delemeter = {}
        self._source_dict   = {}
        self._stop_dict     = {}
        self._title_dict    = {}
        self._bit_dict = BitmaskDict(0,self._source_dict)
    
    
    '''
    공백/소문자/구분자를 제외한다 (사전뒤지기위한용도)
    '''
    def to_index_key(self,value):
        if not value:
            return None
        
        value = toUnicode(value)
        ret = ""
        for ch in value:
            if not self._token_delemeter.has_key(ch) and len(ch.strip())>0:
                ret += ch.lower()
             
        return ret
    
    def load(self):
        self._source_dict.clear()
        
        print "[BOOT] START"
        print "[STEP1] delemeter loading..."
        self._token_delemeter = {toUnicode(key):True  for key in fileToData(self.__file_path__("dict_data",self["dict.delemeter"]))}
        print "[STEP1] delemeter end...(count=%d)\n" % len(self._token_delemeter)
        
        print "[STEP2] stop_dict loading..."
        self._stop_dict = {to_index_key(key, self._token_delemeter):True for key in fileToData(self.__file_path__("dict_data",self["dict.stop"]))}
        print "[STEP2] stop_dict end...(count=%d)\n" % len(self._stop_dict)
        
        print "[STEP3] title_dict loading..."
        def create_title_dict(loop):     
            ret = {}   
            for line in loop:
                token = line.strip().split("\t")
                for word in token[1:]:
                    ret[word] = token[0].strip()
            return ret
        self._title_dict = create_title_dict(fileToData(self.__file_path__("dict_data",self["dict.title"])))
        print "[STEP3] title_dict end...(count=%d)\n" % len(self._title_dict)
         
        print "[STEP4] use_dict loading..."
        for use_conf in self["dict.use"]:
            print ">>> " + use_conf["path"] 
            load_use_dict = BitmaskDict(use_conf["bit"],self._source_dict)
            for line in fileToData(self.__file_path__("dict_data",use_conf["path"])):
                load_use_dict[ to_index_key(line, self._token_delemeter)] = None
            print ">>> load count = %d\n" % len(load_use_dict)
        print "[STEP4] use_dict end... (total count=%d)\n" % len(self._source_dict)        
        print "[BOOT] END"
    
    
    def __file_path__(self, path, filename):
        if path:
            return "%s/%s/%s" % (self._config["root.path"], path, filename)
        else:
            return "%s/%s" % (self._config["root.path"], filename)
        
    
    def __getitem__(self, key):
        if key in self._config:
            return self._config[key]
        else:
            return None
    
    def __setitem__(self, key, item):
        self._config[key] = item

        
    
    def getfilteredDict(self, bitmask=0):
        tmp = BitmaskDict(bitmask)
        tmp.source = self._source_dict
        return tmp
    
    
    def token_delemeter(self):
        return self._token_delemeter
    
    def stop_dict(self):
        return self._stop_dict
    
    def title_dict(self):
        return self._title_dict



if __name__ == "__main__":
    print ""
    
    
#     dict_use     = {tokenSlice.to_index_key(key):True for key in fileToData(path+"/dict_data/food.txt")}
#     dict_use.merge({tokenSlice.to_index_key(key):True for key in fileToData(path+"/dict_data/default.txt")})
#     dict_use.merge({tokenSlice.to_index_key(key):True for key in fileToData(path+"/dict_data/verb.txt")})
#     dict_use.merge({tokenSlice.to_index_key(key):True for key in fileToData(path+"/dict_data/shop.txt")})
#     dict_use.merge({tokenSlice.to_index_key(key):True for key in fileToData(path+"/dict_data/local.txt")})
#     dict_stop    = {tokenSlice.to_index_key(key):True for key in fileToData(path+"/dict_data/stop.txt")}
#     dict_tail    = {tokenSlice.to_index_key(key):True for key in fileToData(path+"/dict_data/tail.txt")}
#     dict_head    = {tokenSlice.to_index_key(key):True for key in fileToData(path+"/dict_data/head.txt")}
    
    