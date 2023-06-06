class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        countOfNums = Counter(nums)
        for i in set(nums):
            if countOfNums[i]==len(nums)/2:
                return i