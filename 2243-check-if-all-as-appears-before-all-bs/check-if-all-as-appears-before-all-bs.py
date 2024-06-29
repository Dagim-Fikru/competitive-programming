class Solution:
    def checkString(self, s: str) -> bool:
        arr = list(s)
        arr.sort()
        s2 = "".join(arr)
        return s==s2
            
        