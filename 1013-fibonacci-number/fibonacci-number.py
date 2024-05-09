class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            if n not in memo:
                memo[n]=self.fib(n-1) + self.fib(n-2)
            return memo[n]
        