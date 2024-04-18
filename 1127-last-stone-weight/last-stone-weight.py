class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        newArr = [-i for i in stones]
        heapq.heapify(newArr)
        while newArr:
            if len(newArr)==1:
                return -newArr[0]
            curr = heapq.heappop(newArr)
            curr2 = heapq.heappop(newArr)
            if curr==curr2:
                continue
            else:
                heapq.heappush(newArr,-abs((abs(curr)-abs(curr2))))
        return 0


                
                
