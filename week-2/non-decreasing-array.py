class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n=len(nums)
        count=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if i>=2 and nums[i-2]>nums[i]:
                    nums[i]=nums[i-1]
                count+=1
        return count<=1
        