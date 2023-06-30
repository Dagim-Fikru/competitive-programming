class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # for i in nums:
        #     while nums.count(i)>1:
        #         nums.remove(i)
        # return len(nums)
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1 
                nums[i] = nums[j]
        return i+1