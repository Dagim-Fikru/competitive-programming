class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total_sum = 0
        result = 0
        for i in range(len(nums)):
            total_sum += nums[i]
            result = max(result, (total_sum + i) // (i + 1))
        return result
        