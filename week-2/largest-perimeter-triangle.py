class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        i = len(nums)-1
        maxPerimeter = 0
        while i>=2:
            if nums[i]<nums[i-1]+nums[i-2]:
                maxPerimeter = max(maxPerimeter,nums[i]+nums[i-1]+nums[i-2])
            i-=1
        return maxPerimeter

