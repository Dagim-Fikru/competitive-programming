class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        r,l=0,0
        zero_count = 0
        maxLen = 0
        while r<len(nums):
            if nums[r]==0:
                zero_count+=1
            while zero_count>k:
                if nums[l]==0:
                    zero_count-=1
                l+=1
            maxLen = max(maxLen,r-l+1)
            r+=1
        return maxLen
            