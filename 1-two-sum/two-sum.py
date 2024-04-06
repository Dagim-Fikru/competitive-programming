class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            check = target - nums[i]
            if check in mapping:
                return [mapping[check],i]
            else:
                mapping[nums[i]] = i