class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        check = set()
        i=0
        j=len(nums)-1
        nums.sort()
        while i<j:
            aver = (nums[i]+nums[j])/2
            check.add(aver)
            i+=1
            j-=1
        return len(check)