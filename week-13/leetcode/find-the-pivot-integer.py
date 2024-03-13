class Solution:
    def pivotInteger(self, n: int) -> int:
        arr = [i for i in range(1,n+1)]
        total2 = sum(arr)
        prefixSum = []
        total = 0
        i = 1
        while i<=n:
            total+=i
            i+=1
            prefixSum.append(total)
        for i in range(len(prefixSum)):
            if prefixSum[i]== total2-prefixSum[i]+arr[i]:
                return arr[i]
        return -1