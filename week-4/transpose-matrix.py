class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        num_rows = len(matrix[0])
        num_columns = len(matrix)
        newMatrix =  [[0 for _ in range(num_columns)] for _ in range(num_rows)]
        for i in range(len(matrix)):
            for j in range(num_rows):
                newMatrix[j][i] = matrix[i][j]
        return newMatrix