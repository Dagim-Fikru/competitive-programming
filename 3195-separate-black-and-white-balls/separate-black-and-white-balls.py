class Solution:
    def minimumSteps(self, s: str) -> int:
        swap = 0
        numOfZero = 0
        i=len(s)-1
        while i>=0:
            if s[i]=='1':
                swap+=numOfZero
            else:
                numOfZero+=1
            i-=1
        return swap
            