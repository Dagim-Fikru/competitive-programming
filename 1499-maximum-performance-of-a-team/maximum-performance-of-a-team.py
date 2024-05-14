class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        engineers = sorted(zip(efficiency, speed), reverse=True)
        speed_heap = []
        total_speed = 0
        max_performance = 0

        for eff, spd in engineers:
            heapq.heappush(speed_heap, spd)
            total_speed += spd

            if len(speed_heap) > k:
                total_speed -= heapq.heappop(speed_heap)

            max_performance = max(max_performance, total_speed * eff)

        return max_performance % (10 ** 9 + 7)
