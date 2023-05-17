class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        # if n==1:
        #     return n
        while n>0:
            n-=i
            i+=1
        if n==0:
            return i-1
        else:
            return i-2
        
            
        