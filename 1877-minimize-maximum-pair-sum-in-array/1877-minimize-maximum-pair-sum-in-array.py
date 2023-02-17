class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        i=0
        j=len(nums)-1
        while i<j:
            pairSum=nums[i]+nums[j]
            if pairSum>result:
                result=pairSum
            i+=1
            j-=1
        return result
        