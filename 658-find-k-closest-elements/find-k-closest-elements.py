class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        sample = []
        indx = 0
        for i in range(k):
            sample.append(arr[i])
            indx+=1
        heapq.heapify(sample)
        # print(indx)
        for i in range(indx,len(arr)):
            curr = heapq.heappop(sample)
            # print(curr,arr[i])
            if abs(curr-x)<abs(arr[i]-x):
                heapq.heappush(sample,curr)
            elif abs(curr-x)>abs(arr[i]-x):
                heapq.heappush(sample,arr[i])
            else:
                if curr<arr[i]:
                    heapq.heappush(sample,curr)
                else:
                    heapq.heappush(sample,arr[i])
        # for i in range(len(sample)):
        #     sample[i]=abs(sample[i])
        return sorted(sample)
