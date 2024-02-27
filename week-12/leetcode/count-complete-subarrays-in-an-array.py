class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))
        count=0
        for i in range(len(nums)):
            check = set()
            for j in range(i,len(nums)):
                check.add(nums[j])
                if len(check)==n:
                    count+=1
        return count
