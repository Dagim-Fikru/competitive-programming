class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l= 0
        ans = float('inf')
        sum=0
        for r in range(len(nums)):
            sum+=nums[r]
            while sum>=target:
                ans = min(ans,r-l+1)
                sum-=nums[l]
                l+=1
        return ans if ans!=float('inf') else 0



            