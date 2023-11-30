class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numOfPairs = 0
        counter = Counter(nums)

        for key,value in counter.items():
            numOfPairs+= (value*(value-1))//2
        return numOfPairs
        