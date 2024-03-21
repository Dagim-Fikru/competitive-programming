class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxElem = max(piles)
        ans = float("inf")
        left = 1
        right = maxElem
        while right>=left:
            currTime = 0
            mid = (right+left)//2

            for i in range(len(piles)):
                currTime  = currTime + ceil(piles[i]/mid)
            if currTime>h:
                left = mid+1
            else:
                right = mid-1
                ans = min(ans,mid)
        return ans