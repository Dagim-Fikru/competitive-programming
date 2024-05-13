class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        check = set()
        for i in nums:
            if i in check:
                check.remove(i)
            else:
                check.add(i)
        return list(check)