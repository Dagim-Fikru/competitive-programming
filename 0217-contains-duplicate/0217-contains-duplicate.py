class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setOfNum = set(nums)
        if len(setOfNum)==len(nums):
            return False
        return True
        # freq = collections.Counter(nums)
        # key = freq.values()
        # isYes = False
        # for key in freq:
        #     if freq[key]>1:
        #         isYes=True
        #         break
        # # setOfList = set(nums)
        # # for i in setOfList:
        # #     if nums.count(i)>1:
        # #        isYes = True
        # #        break
        #     # else:
        #     #     return False
        # # for i in nums:
        # #     if nums.count(i)>1:
        # #         return True
        # #     else:
        # #         return False
        # return isYes