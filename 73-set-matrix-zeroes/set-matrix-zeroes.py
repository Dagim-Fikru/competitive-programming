class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        posOfZero = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    posOfZero.append([i,j])
        # print(posOfZero)
        for i,j in posOfZero:
            for r in range(len(matrix[i])):
                matrix[i][r]=0
            for c in range(len(matrix)):
                matrix[c][j]=0

