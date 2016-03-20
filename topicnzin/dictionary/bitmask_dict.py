#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
	메모리를 절약하기 위해 dict를 공유해서 사용한다.
	bitmast로 구분되지만, 내부적으로 관리될 뿐 사용자가 느끼기에는 일반 dict를 쓰는것과 큰 차이를 못느낄것이다.
	데이터의 구분은 처음 생성할때 bitmask값으로 구분된다.

"""
from topicnzin.common.utils import toStr
class BitmaskDict(object):
	def __init__(self, bitmask=0, user_dict={}):
		self._bitmask  = bitmask
		self._dict     = user_dict
		
	@staticmethod
	def convertBitMaskDict(use_dict, bit_mask):
		ret = BitmaskDict(bit_mask)
		for key in use_dict:
			ret[key] = use_dict[key]
		return ret
	
	
	@property
	def source(self):
		return self._dict
	
	@source.setter
	def source(self, value):
		self._dict = value
		
	
	def merge(self, source_dict):		
		if isinstance(source_dict, BitmaskDict):
			source_dict = source_dict.source
			for key in source_dict:
				bitset, value = source_dict[key]
				self._dict[key] = (bitset | self.bitmask(), value)
			return self
		
		raise TypeError
		
	def __merge__(self, key, item, bitmask):
		if key in self._dict:
			bit, val = self._dict[key]
			val = item if item else val
			bit = bit | bitmask
			self._dict[key] = (bit, val)
		else:
			self._dict[key] = (bitmask, item)

	def __get_filter__(self, key, bitmask):
		if key in self._dict:
			bit, val = self._dict[key]
			if bit & bitmask > 0:
				return val
		return None

	def __getitem__(self, key):
		return self.__get_filter__(key, self._bitmask)
	
	def __setitem__(self, key, item):
		self.__merge__(key, item, self._bitmask)

	def __contains__(self, key):
		if key in self._dict:
			bit = self._dict[key][0]
			if bit & self._bitmask > 0:
				return True
		return False
		


	"""
		해당 bitmask와 key가 만족하는것이 있는지 알려준다.
	"""
	def has_key(self, key):
		return self.__contains__(key)
	

	"""
		사용자가 정의한 최초 bitmask를 의미한다.
	"""
	def bitmask(self):
		return self._bitmask

	"""
		bitmask로 걸러낸 데이터의 keys만 리턴한다.
	"""
	def keys(self):
		return filter(lambda key: self.__contains__(key) ,self._dict.keys() )

	"""
		bitmask를 걸러낸 데이터의 values만 리턴한다
	"""
	def values(self):
		return map(lambda x: x[1] ,filter(lambda x: x[0] & self._bitmask ,self._dict.values()) )

	"""
		bitmask를 걸러낸 데이터의 갯수를 의미한다.
	"""
	def __len__(self):
		return len(self.keys())


	def __repr__(self):
		ret = "{"
		for key in self._dict:
			if self.__contains__(key):
				ret += ("'%s':%s, ") % (toStr(key),  toStr(self[key]))

		if len(ret) > 3:
			ret = ret[0:len(ret)-2]

		return ret + "}"

	def __iter__(self):
		for key in self.keys():
			yield key


if __name__ == "__main__":

	mydict = {}
	bit1 = BitmaskDict(1, mydict)
	bit1["key"] = "aaa"
	bit1["key2"] = "bbb"
	bit1["key3"] = "bbb"

	bit2 = BitmaskDict(2, mydict)
	bit2["key00"] = "ccc"

	bit3 = BitmaskDict(4, mydict)
	
	print "key00" in bit2 
	print "key00" in bit1
	print "key" in bit1
	
	bit2["key2"] = "dd"
	
	print "--"
	print bit1.has_key("key2")
	print bit2.has_key("key2")
	print bit1["key2"]
	print bit2["key2"]
	print bit3["key2"]
	
	print len(bit1)
	print len(bit2)
	print len(bit3)
	
	
	sample = BitmaskDict(8)
	sample["aaaaaaa"] = True
	sample["key2"] = True
	
	print ""
	print sample.source
	print bit2.source
	print sample.merge(bit3)
	print sample.source
	
	

	# # print bit1
	# # print bit2

	# print bit1.values()
	# print bit2.values()
	# print mydict.values()

	# print len(bit1)
	# print len(bit2)
	# print len(mydict)

	# print "loop test"
	
	# for item in bit2:
	# 	print item