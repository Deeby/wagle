# -*- coding: utf-8 -*-
import re
import urllib2
try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup

#HTML 파싱을 담당. 
class HtmlParser:

    soup = None
    raw = None
    html = None
 
    def parse(self,url=None): 
        self.raw = urllib2.urlopen(url)
        self.html = self.raw.read() 
        print self.html
        self.soup = BeautifulSoup(self.html)

        return self.soup

    def clear(self):
        self.raw = None
        self.html = None
        self.soup = None




