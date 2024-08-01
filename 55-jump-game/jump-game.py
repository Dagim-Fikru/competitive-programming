class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0]==0 and len(nums)!=1:
            return False
        maxDistance = 0
        for i in range(len(nums)-1):
            if i>maxDistance:
                return False
            if nums[i]!=0:
                maxDistance = max(maxDistance,i+nums[i])
        return maxDistance>=len(nums)-1