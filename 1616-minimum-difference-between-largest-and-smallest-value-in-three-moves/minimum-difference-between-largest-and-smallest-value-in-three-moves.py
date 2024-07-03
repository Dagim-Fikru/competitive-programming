class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 3:
            return 0
        n = len(nums)
        ans = float('inf')
        for i in range(4):
            ans = min(ans, nums[n-1-i] - nums[3-i])
        return ans