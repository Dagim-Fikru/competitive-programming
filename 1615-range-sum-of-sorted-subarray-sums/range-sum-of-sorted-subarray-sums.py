class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        possibleSum = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                possibleSum.append(sum(nums[i:j+1]))
        possibleSum.sort()
        return sum(possibleSum[left-1:right])%((10**9)+7)