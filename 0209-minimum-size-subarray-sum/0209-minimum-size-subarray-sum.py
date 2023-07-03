class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        total = 0
        res= len(nums)+1
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                res = min(r-i+1,res)
                total-=nums[i]
                i+=1
        if res>=len(nums)+1:
            return 0
        return res
            