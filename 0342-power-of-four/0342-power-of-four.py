class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        else:
            while n>4:
                n/=4
        return n==4
        