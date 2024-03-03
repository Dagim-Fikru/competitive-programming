class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        max_sum = 0

        for i in range(1,row-1):
            currSum = 0
            for j in range(1,col-1):
                currSum = sum(grid[i-1][j-1:j+2]) + grid[i][j] + sum(grid[i+1][j-1:j+2])
                max_sum = max(max_sum,currSum)
        return max_sum
