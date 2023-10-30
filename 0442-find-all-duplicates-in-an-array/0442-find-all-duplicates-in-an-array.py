class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        check = set()
        arr= []
        for num in nums:
            if num in check:
                arr.append(num)
            else:
                check.add(num)
        return arr