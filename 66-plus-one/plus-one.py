class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==9:
                nums[i]=0
            else:
                nums[i]+=1
                return nums
        return [1] + nums

        