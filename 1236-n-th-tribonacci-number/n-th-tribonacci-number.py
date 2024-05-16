class Solution:
    # def __init__(self):
    #     self.memo = {}
    def tribonacci(self, n: int) -> int:
        dp = [0] * (n+1)
        if n==1:
            dp[1]=1
        elif n>=2:
            dp[1]=1
            dp[2]=1
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]

        # if n==0:
        #     return n
        # elif n==1 or n==2:
        #     return 1
        # else:
        #     if n not in self.memo:
        #         self.memo[n]=self.tribonacci(n-3)+self.tribonacci(n-1) + self.tribonacci(n-2)
        #     return self.memo[n]
            