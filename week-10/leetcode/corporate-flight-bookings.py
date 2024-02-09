class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        preSum = [0]*(n+1)
        for i,j,k in bookings:
            preSum[i-1]+=k
            preSum[j]-=k
        sum=0
        for i in range(len(preSum)):
            sum+=preSum[i]
            preSum[i]=sum
        preSum.pop()
        return preSum


        