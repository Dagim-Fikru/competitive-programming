class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        res = [[float('inf')] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if i > 0:
                        res[i][j] = min(res[i][j], res[i-1][j] + 1)
                    if j > 0:
                        res[i][j] = min(res[i][j], res[i][j-1] + 1)

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if mat[i][j] == 1:
                    if i < m-1:
                        res[i][j] = min(res[i][j], res[i+1][j] + 1)
                    if j < n-1:
                        res[i][j] = min(res[i][j], res[i][j+1] + 1)
        return res