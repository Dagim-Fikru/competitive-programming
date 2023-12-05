class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        minTime = 0
        for i in range(len(points)-1):
            time1 = abs(points[i][0]-points[i+1][0]) 
            time2= abs(points[i][1]-points[i+1][1])
            minTime+=max(time1,time2)
        return minTime