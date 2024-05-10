class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        div = []
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                div.append([[arr[i]/arr[j]],[arr[i],arr[j]]])
        div.sort()
        return div[k-1][1]