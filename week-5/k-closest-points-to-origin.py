class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            distance = (points[i][0])**2 + (points[i][1])**2
            points[i].append(distance)
        points = sorted(points, key=lambda x: x[2])
        for i in range(len(points)):
            points[i].pop()
        return points[:k]