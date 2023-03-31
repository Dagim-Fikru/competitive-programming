class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dicta={}
        for i in s:
            if i in dicta:
                return i
            else:
                dicta[i]=1
        
                
            
        
        