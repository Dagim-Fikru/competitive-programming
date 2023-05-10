class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        longest = 1
        if len(nums)==0:
            return len(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            if nums[i] == nums[i+1]-1:
                count+=1
                longest = max(count , longest)
            else:
                count = 1
        return longest
        
        