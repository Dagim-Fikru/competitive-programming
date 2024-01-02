class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pal=True
        s = ''.join(filter(str.isalnum, s))
        s=s.lower()
        i=0
        j=len(s)-1
        while i<j:
            # if len(s)==0:
            #     return True
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
                
                
        