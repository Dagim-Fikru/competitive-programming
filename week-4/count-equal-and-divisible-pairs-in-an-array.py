class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        checkIndex = defaultdict(list)
        count = 0
        for indx,val in enumerate(nums):
            for num in checkIndex[val]:
                if (indx*num)%k==0:
                    count+=1
            checkIndex[val].append(indx)
        return count
