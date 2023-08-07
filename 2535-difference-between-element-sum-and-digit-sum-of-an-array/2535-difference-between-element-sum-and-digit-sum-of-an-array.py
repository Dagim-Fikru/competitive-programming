class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        arr2 = []
        for i in nums:
            arr2.append(str(i))
        ele_sum = 0
        dig_sum = 0
        
        for i in nums:
            ele_sum+=i
        for j in arr2:
            for k in j:
                dig_sum = dig_sum +int(k)
        return abs(ele_sum-dig_sum)
        