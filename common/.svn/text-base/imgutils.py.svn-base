# -*- coding: utf-8 -*- 

import urllib2
import base64 


def getBase64StringFromUrl(url=None):
    if url is None:
        return None; 
    
    u = urllib2.urlopen(url)
    raw_data = u.read()
    u.close()
    
    b64_data = base64.encodestring(raw_data) 
    return b64_data
    
    