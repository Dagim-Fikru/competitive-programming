class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opening = 0 
        closing = 0 
        arr = list(s)
        for i in range(len(s)):
            if s[i]=="(":
                opening+=1
            elif s[i]==")":
                if opening>0:
                    opening-=1
                else:
                    arr[i] = ""
        for i in range(len(s)-1,-1,-1):
            if s[i]==")":
                closing+=1
            elif s[i]=="(":
                if closing>0:
                    closing-=1
                else:
                    arr[i] = ""
        return "".join(arr)
