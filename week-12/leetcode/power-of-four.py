class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n==1:
        #     return True
        # else:
        #     while n>4:
        #         n/=4
        # return n==4
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif n % 4 == 0:
            return self.isPowerOfFour(n / 4)
        # else:
        #     return False
