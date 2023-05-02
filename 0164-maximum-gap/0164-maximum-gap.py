class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        diff=0
        i=0
        j=i+1
        while i<=len(nums)-2:
            result= nums[j]-nums[i]
            diff = max(result,diff)
            i+=1
            j+=1
        if len(nums)<2:
            return 0
        return diff
        