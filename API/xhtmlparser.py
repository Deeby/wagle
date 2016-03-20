# -*- coding: utf-8 -*-
import re
import urllib2
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

#HTML 파싱을 담당. 
class XHtmlParser:

    soup = None
    raw = None
    content = None
 
    def parse(self,url=None, type=None):
        self.raw = urllib2.urlopen(url)
        self.content = self.raw.read()
        
        if type == None:
            self.soup = BeautifulSoup(self.content)
        else:
            self.soup = BeautifulSoup(self.content, type)

        return self.soup

    def clear(self):
        self.raw = None
        self.html = None
        self.soup = None




