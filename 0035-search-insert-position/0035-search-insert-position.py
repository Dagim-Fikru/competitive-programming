class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,u = 0, len(nums)-1
        while l<=u:
            mid = (l+u)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                u=mid-1
            else:
                l=mid+1
        return l
        # for i in nums:
        #     if target in nums:
        #         return nums.index(target)
        #     else:
        #         if i<target:
        #             if nums.index(i)==len(nums)-1:
        #                 return len(nums)
        #             continue
        #         else:
        #                 return nums.index(i)
            
        