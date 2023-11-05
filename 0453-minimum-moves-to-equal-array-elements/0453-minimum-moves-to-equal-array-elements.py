class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minEl = min(nums)
        numOfMoves = 0
        for num in nums:
            numOfMoves+=num-minEl
        return numOfMoves
        