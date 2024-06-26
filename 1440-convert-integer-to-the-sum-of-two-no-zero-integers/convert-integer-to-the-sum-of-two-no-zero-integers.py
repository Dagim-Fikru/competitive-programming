class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            num1 = i
            num2 = n-i
            if "0" not in str(num1) and "0" not in str(num2):
                return [num1,num2]