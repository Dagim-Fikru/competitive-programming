class Solution:
    def alternateDigitSum(self, n: int) -> int:
        arr = list(str(n))
        sum1 = 0
        for i in range(len(arr)):
            if i%2==0:
                sum1+=int(arr[i])
            else:
                sum1-=int(arr[i])
        return sum1