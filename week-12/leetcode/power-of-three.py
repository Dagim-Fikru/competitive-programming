class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n==1:
        #     return True
        # else:
        #     while n>3:
        #         n/=3
        # return n==3
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif n % 3 == 0:
            return self.isPowerOfThree(n / 3)
        