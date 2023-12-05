class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        distanceClock = sum(distance[min(start,destination):max(destination,start)])
        distanceAnti = sum(distance) - distanceClock
        return min(distanceClock,distanceAnti)