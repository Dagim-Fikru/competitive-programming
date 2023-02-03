class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(sub_nums):
            if len(sub_nums) <= 2:
                return True
            diff = sub_nums[1] - sub_nums[0]
            for i in range(2, len(sub_nums)):
                if sub_nums[i] - sub_nums[i-1] != diff:
                    return False
            return True
        result = []
        for i in range(len(l)):
            sub_nums = sorted(nums[l[i]:r[i]+1])
            result.append(is_arithmetic(sub_nums))
        return result   
                    

            
        