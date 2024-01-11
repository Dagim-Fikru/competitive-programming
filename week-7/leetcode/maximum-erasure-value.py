class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        check=set()
        sum = 0
        maxSum = 0
        for r in range(len(nums)):
            while nums[r] in check:
                sum-=nums[l]
                check.remove(nums[l])
                l+=1
            check.add(nums[r])
            sum+=nums[r]
            maxSum = max(sum,maxSum)
        return maxSum