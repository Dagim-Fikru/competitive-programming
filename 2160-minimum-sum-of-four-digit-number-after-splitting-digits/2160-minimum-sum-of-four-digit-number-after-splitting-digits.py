class Solution:
    def minimumSum(self, num: int) -> int:
        arr = list(str(num))
        arr.sort()
        sum1=0
        i=0
        j=len(arr)-1
        while i<j:
            num1=int(str(arr[i]+str(arr[j])))
            sum1+=num1
            i+=1
            j-=1
        return sum1
            
            