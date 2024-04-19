class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        difference = []
        for i in range(len(heights)-1):
            diff = heights[i] - heights[i+1]
            if diff>0:
                difference.append(0)
            else:
                difference.append(abs(diff))
        print(difference)
        heap = []
        i=0
        while ladders>0 and i<len(difference):
            if difference[i]>0:
                heap.append(difference[i])
                ladders-=1
            i+=1
        # print(heap,i)
        heapq.heapify(heap)
        while bricks>0 and i<len(difference):
            if difference[i]!=0:
                if heap:
                    if heap[0]<difference[i]:
                        if bricks>= heap[0]:
                            bricks-= heap[0]
                            heapq.heappushpop(heap,difference[i])
        #                     print(heap)
                            
                        else:
                            return i
                    else:
                        if bricks>= difference[i]:
                            bricks-= difference[i]
                            # heapq.heappush(heap,difference[i])
        #                     print(heap)
                            
                        else:
                            return i
                else:
                    if bricks>= difference[i]:
                        bricks-= difference[i]
                    else:
                        return i
                i+=1
            else:
                i+=1
    
        while i<len(difference) and difference[i]==0:
            i+=1
        return i
            

               