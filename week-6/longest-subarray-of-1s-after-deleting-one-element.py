class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        r,l = 0,0
        count=0
        maxLen = 0
        while r<len(nums):
            if nums[r]==0:
                count+=1
            while count>1:
                if nums[l]==0:
                    count-=1
                l+=1
            maxLen = max(maxLen,r-l+1)
            r+=1
        print(r,l)
        return maxLen-1
            
        