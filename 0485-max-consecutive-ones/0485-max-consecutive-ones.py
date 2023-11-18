class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r,l=0,0
        maxLen=0
        
        while r<len(nums):
            if nums[r]==0:
                l=r+1
            maxLen = max(maxLen,r-l+1)
            r+=1
        return maxLen