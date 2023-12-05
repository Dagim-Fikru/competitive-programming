class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        arr = [999,888,777,666,555,444,333,222,111,'000']
        for i in arr:
            if str(i) in nums:
                return str(i)
        return ""
        

