class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        Profit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)
        for _ in range(k + 1):
            if Profit:
                w += (-heapq.heappop(Profit)[0])
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(Profit, (-p, c))
        return w