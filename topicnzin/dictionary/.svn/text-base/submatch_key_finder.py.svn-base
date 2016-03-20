#!/usr/bin/python
# -*- coding: utf-8 -*-
from topicnzin.common.utils import toStr
class SubMatchKeyFinder:
	def __init__(self, user_dict={}):
		self.reload(user_dict)

	"""
		찾을 대상의 dict를 변경한다.
	"""
	def reload(self, user_dict):
		self._dict = user_dict

	"""
		key에서 일치되는 값이 있는지 확인한다.

		# true : 일치되는 key값 
		# false: None
	"""
	def exactMatch(self, key, detault=None):
		if key in self._dict :
			return key
		else:
			return detault

	"""
		사용자가 찾는 키워드안에서 key가 앞쪽에서 부분일치되는 값을 list 리턴한다.
		list 순서는 가장 길게 일치되는 값순서로 리턴된다.

		# true : 앞에서 부분일치되는값의 list
		# false: []

	"""
	def startMatch(self, key):
		ret = []
		length = len(key)
		for idx in range(length):
			if key[0:length-idx] in self._dict:
				ret.append(key[0:length-idx])
		return ret
	
	"""
		최장일치되는것 한건만 리턴한다.
	"""
	def startLongMatch(self, key, detault=None):
		length = len(key)
		for idx in range(length):
			if key[0:length-idx] in self._dict:
				return key[0:length-idx]
		return detault
		

	"""
	사용자가 찾는 키워드안에서 key가 뒤쪽에서 부분일치되는 값을 list 리턴한다.
	list 순서는 가장 길게 일치되는 값순서로 리턴된다.

	true : 뒤에서 부분일치되는값의 list
	false: []
	"""
	def endMatch(self, key):
		ret = []
		length = len(key)        
		for idx in range(length):         
			if key[idx:length] in self._dict:
				ret.append(key[idx:length])
		return ret
	
	"""
		최장일치되는값 
	"""
	def endLongMatch(self, key, detault=None):
		length = len(key)        
		for idx in range(length):         
			if key[idx:length] in self._dict:
				return key[idx:length]
		return detault


	def toDict(self):
		return self._dict

if __name__ == "__main__":
	dic = {u"완전":1 , u"배고프다헐랭":2, u"완전테스트":9, u"은":12}

	key = SubMatchKeyFinder(dic)
	print "1: " + toStr(key.exactMatch(u"완전테스트하기"),"")
	print "2: " + toStr(key.startMatch(u"완전테스트") ,"")
	print "3: " + toStr(key.startMatch(u"완전테스트하기"),"")
	print "3: " + toStr(key.startMatch(u"은정이는"),"")
	#print _str( dic )
	
	
