class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums==sorted(nums) or nums==list(reversed(sorted(nums))):
            return True
        return False
        