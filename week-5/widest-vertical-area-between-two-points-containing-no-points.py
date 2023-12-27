class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxGap = 0
        for i in range(len(points)-1):
            maxGap = max(maxGap,points[i+1][0]-points[i][0])
        return maxGap
