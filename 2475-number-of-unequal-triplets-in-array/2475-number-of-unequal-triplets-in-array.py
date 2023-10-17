class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                for k in range(2,len(nums)):
                    if i<j and j<k:
                        if nums[i]!=nums[j] and nums[i] != nums[k]:
                            if nums[j] != nums[k]:
                                count+=1
                    else:
                        continue
        return count
        