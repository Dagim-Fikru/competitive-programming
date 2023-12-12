class Solution:
    def isHappy(self, n: int) -> bool:
        while n>9:
            strOfn = str(n)
            n=0
            for i in strOfn:
                n+= int(i)**2
        if n==1 or n==7:
            return True
        else:
            return False 
        


        