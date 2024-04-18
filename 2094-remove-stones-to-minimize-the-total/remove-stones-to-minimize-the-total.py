class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-i for i in piles]
        heapq.heapify(heap)
        while k:
            val = -heapq.heappop(heap)
            heapq.heappush(heap,-(abs(val)-(abs(val)//2)))
            k-=1
        ans = 0

        for i in heap:
            ans+=abs(i)
        return ans