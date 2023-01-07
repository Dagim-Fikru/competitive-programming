class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        count = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(0,len(nums)):
                if nums[i]==nums[j]:
                    continue
                elif nums[i]>nums[j]:
                    count[i]+=1
        return count
