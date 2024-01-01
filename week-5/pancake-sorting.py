class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n=len(arr)
        outArr=[]
        for i in range(n):
            maxElement= max(arr[:n-i])
            maxElemIndx = arr.index(maxElement) + 1
            arr[:maxElemIndx]= reversed(arr[:maxElemIndx])
            outArr.append(maxElemIndx)
            arr[:n-i]=reversed( arr[:n-i])
            outArr.append(n-i)
        return outArr
            
            
        