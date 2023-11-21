class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = Counter(nums)
        
        for key,value in check.items():
            if value==1:
                return key
        