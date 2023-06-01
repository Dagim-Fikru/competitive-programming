class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = 0
        newDict = Counter(nums)
        nums.sort()
        for i in range(len(nums)-1):
            result=0
            if nums[i]==nums[i+1]-1:
                result+= newDict[nums[i]]+newDict[nums[i+1]]
                count=max(count,result)
            else:
                continue
        return count
        