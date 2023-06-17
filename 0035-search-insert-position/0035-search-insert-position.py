class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if target in nums:
                return nums.index(target)
            else:
                if i<target:
                    if nums.index(i)==len(nums)-1:
                        return len(nums)
                    continue
                else:
                        return nums.index(i)
            
        