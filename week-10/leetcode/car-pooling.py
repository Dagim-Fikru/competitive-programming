class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        destination = 0
        for i in range(len(trips)):
            destination = max(destination,trips[i][-1])
            if trips[i][0]>capacity:
                return False
        preSum = [0]*(destination+1)
        for i,j,k in trips:
            preSum[j-1]+=i
            preSum[k-1]-=i
        sum=0
        for i in range(len(preSum)):
            sum+=preSum[i]
            preSum[i]=sum
        for i in preSum:
            if i>capacity:
                return False
        return True
