class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr2=[]
        arr.sort()
        absoutDiff = abs(arr[1]-arr[0])
        for i in range(len(arr)-1):
            absoutDiff1=arr[i+1]-arr[i]
            absoutDiff = min(absoutDiff1,absoutDiff)
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<=absoutDiff:
                arr2.append([arr[i],arr[i+1]])
        
        return arr2
        
        