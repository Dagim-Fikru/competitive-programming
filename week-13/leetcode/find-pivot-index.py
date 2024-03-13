class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefixSum=[]
        sum1=0
        for i in nums:
            sum1+=i
            prefixSum.append(sum1)
        for i in range(len(prefixSum)):
            if prefixSum[i]== total-prefixSum[i]+nums[i]:
                return i
        return -1
            
            
            