class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        newList = list(set(arr))
        newList.sort()
        arr2=[]
        newDict = {}
        for i in range(len(newList)):
            newDict[newList[i]]=i+1
        for i in range(len(arr)):
            arr2.append(newDict[arr[i]])
        return arr2
        