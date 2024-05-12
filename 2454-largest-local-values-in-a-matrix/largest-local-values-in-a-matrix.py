class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        size = len(grid)-2
        ans = [[0]*size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        ans[i][j] = max(ans[i][j],grid[row][col])
        return ans