class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        cur_sum = 0
        for num in nums:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)

        return max_sum