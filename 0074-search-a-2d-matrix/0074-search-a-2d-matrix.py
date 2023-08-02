class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x=None
        for i in range(len(matrix)):
            if matrix[i][-1]<target:
                continue
            elif matrix[i][-1]==target:
                return True
            else:
                x=i
                break
        if x==None:
            return False
        l,u = 0 , len(matrix[x])
        while l<=u:
            mid = (l+u)//2
            if matrix[x][mid]==target:
                return True
            elif matrix[x][mid]<target:
                l=mid+1
            else:
                u=mid-1
        return False
        