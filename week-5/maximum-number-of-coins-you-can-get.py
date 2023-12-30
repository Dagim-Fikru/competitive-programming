class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles)
        ans = 0
        for i in range(0, n // 3):
            ans += piles[2 * i + 1]
        return ans
#         def less(piles):
#             sum=0
#             x=1
#             while x<len(piles):
#                 sum+=piles[x]
#                 x+=3
#             return sum
        
#         def great(piles):
#             sum=0
#             x=len(piles)//3
#             while x<len(piles):
#                 sum+=piles[x]
#                 x+=2
#             return sum
#         # arr=piles.sort()
#         if len(piles)<=6:
#             return less(piles)
#         else:
            # return great(piles)