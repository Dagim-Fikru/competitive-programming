class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = nums[0]
        for num in nums[1:]:
            result = result ^ num
        result = result ^ k
        return result.bit_count()