class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        ans = 0
        difference = sum(cardPoints[:n-k])
        for i in range(k):
            ans = max(ans,total-difference)
            difference = difference - cardPoints[i]+ cardPoints[n-k+i]
        ans = max(ans,total-difference)
        return ans


