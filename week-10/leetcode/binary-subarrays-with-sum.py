class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        atmostk=0
        atmostk_1 = 0
        l=0
        total=0
        for r in range(len(nums)):
            total+=nums[r]
            while total>goal:
                total-=nums[l]
                l+=1
            atmostk+=r-l+1
        l=0
        total=0
        for r in range(len(nums)):
            total+=nums[r]
            while total>goal-1 and l<len(nums):
                total-=nums[l]
                l+=1
            atmostk_1+=r-l+1
        return atmostk-atmostk_1 if atmostk_1>0 else atmostk


        