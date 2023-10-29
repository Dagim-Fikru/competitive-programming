class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currSum = float('-inf'),0
        for i in range(len(nums)):
            currSum = max(nums[i],currSum+nums[i])
            maxSum = max(currSum,maxSum)
        return maxSum