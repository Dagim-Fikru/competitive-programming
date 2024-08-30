class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        freq = Counter(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                return [i,i+freq[nums[i]]-1]
        else:
            return [-1,-1]