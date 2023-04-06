class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        x=0
        for i in range(len(nums)):
            if nums[i]== i:
                if nums[-1]!=len(nums)+1:
                    x=i+1 
            else:
                x=i
                break
        return x
            
        