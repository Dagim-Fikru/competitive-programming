class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        # arr=[]
        # if nums.count(0)==0:
        #     return nums
        # else:
        #     for i in nums:
        #         if i==0:
        #             arr.append(nums.pop(nums.index(i)))
        #     nums.sort()
        # for i in arr:
            # nums.append(i)
        # i=0
        # j=len(nums)-1
        # while i<j:
        #     if nums[i]!=0:
        #         i+=1
        #     else:
        #         if nums[j]==0:
        #             j-=1
        #         nums[i],nums[]
        