class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while right>=left:
            mid = (right+left)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left = mid+1
        return -1
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        # else:
        #     return -1