class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l=0
        maxSum = 0
        currSum = 0
        check = set()
        for r in range(len(nums)):
            while r-l+1>k:
                check.remove(nums[l])
                currSum-=nums[l]
                l+=1
            while nums[r] in check:
                check.remove(nums[l])
                currSum-=nums[l]
                l+=1
            check.add(nums[r])
            currSum+=nums[r]
            if r-l+1==k:
                maxSum = max(maxSum,currSum)
        return maxSum
            