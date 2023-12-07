class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = [i for i in range(left,right+1)]
        arr2=[]
        for i in range(len(ranges)):
            arr2.append([j for j in range(ranges[i][0],ranges[i][1]+1)])
        arr3 = []
        for i in range(len(arr2)):
            arr3 = arr3+arr2[i]
        arr3.sort()
        for i in arr:
            if i not in arr3:
                return False
        return True
