class Solution:
    def search(self, nums: List[int], target: int) -> int:
        li,ui = 0 , len(nums)-1
        while li<=ui:
            mid = (li+ui)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                ui = mid-1
            else:
                li = mid+1
        return -1