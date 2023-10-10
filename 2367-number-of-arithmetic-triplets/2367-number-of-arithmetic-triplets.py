class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                for k in range(2,len(nums)):
                    if nums[j]-nums[i]==diff:
                        if nums[k]-nums[j]==diff:
                            count+=1
                    else:
                        continue
        return count
        