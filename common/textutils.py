# -*- coding: utf-8 -*- 


def extractDong(address): 
    num=['0','1','2','3','4','5','6','7','8','9']
    
    units = address.split(" ")
    
    isDetailAddr = False;
    preAddr = "";
    for unit in units:
        if len(unit) >1:
            for n in num:
                
                if n == unit[0]:
                    isDetailAddr=True
                    break;
            
            if isDetailAddr == True:
                break
            
            preAddr = unit
        else:
            pass 
        
        
    #번지수 이전의 주소 단위를 동으로 추청한다. 
    return preAddr;


def removeText(originalText, fromStr, toStr):
    fromIndex = originalText.find(fromStr)
    toIndex = originalText.rfind(toStr)
    
    if fromIndex == -1 and toIndex == -1:
        return originalText; 
    
    beforeFromIndex = originalText[:fromIndex].strip() 
    afterToIndex = originalText[toIndex+1:].strip()
    
    return beforeFromIndex +" "+afterToIndex; 
    
    
 
        
if __name__ == '__main__':
    print extractDong("서울시 강동구 둔촌동 12-12")
    print removeText("이자까야(홍대점) 2호점", "(", ")")
        
            