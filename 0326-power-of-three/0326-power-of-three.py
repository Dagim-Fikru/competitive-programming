class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        else:
            while n>3:
                n/=3
        return n==3
        