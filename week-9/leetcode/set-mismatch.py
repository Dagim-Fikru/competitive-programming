class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        countFreq = Counter(nums)
        ans = []
        n=len(nums)
        numsSum = sum(nums)
        duplicatedNum = 0
        expectSum = (n*(n+1))//2
        for i in countFreq:
            if countFreq[i]==2:
                duplicatedNum= i
        ans.append(duplicatedNum)
        ans.append(expectSum-(numsSum-duplicatedNum))
        return ans

