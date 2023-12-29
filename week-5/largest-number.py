from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            return int(str(b) + str(a)) - int(str(a) + str(b))
        nums = sorted(nums, key=cmp_to_key(compare))
        listostring = ""
        for n in nums:
            listostring = listostring + str(n)
        return str(int(listostring))