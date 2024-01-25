class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        runningSum = 0
        for i in nums:
            runningSum+=i
            ans.append(runningSum)
        return ans