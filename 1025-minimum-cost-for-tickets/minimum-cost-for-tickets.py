class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = defaultdict(lambda: 0)
        for d in range(1, days[-1] + 1):
            if d in days:
                dp[d] = min(dp[d - 1] + costs[0],
                        dp[d - 7] + costs[1],
                        dp[d - 30] + costs[2],)
            else:
                dp[d]=dp[d - 1]
        return dp[days[-1]]