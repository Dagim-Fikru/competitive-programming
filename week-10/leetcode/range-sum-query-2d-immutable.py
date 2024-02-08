class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.presum = [[0 for _ in range(len(self.matrix[0])+1)] for _ in range(len(self.matrix)+1)]
        for i in range(len( self.matrix)):
            for j in range(len( self.matrix[i])):
                if i==0 and j==0:
                    self.presum[i][j]=self.matrix[i][j]
                elif i>0 and j==0:
                    self.presum[i][j]=self.presum[i-1][j]+ self.matrix[i][j]
                elif i==0 and j>0:
                    self.presum[i][j]=self.presum[i][j-1]+ self.matrix[i][j]
                else:
                     self.presum[i][j]=self.presum[i-1][j]+self.presum[i][j-1]-self.presum[i-1][j-1]+ self.matrix[i][j]        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return  self.presum[row2][col2] - self.presum[row2][col1 - 1] - self.presum[row1 - 1][col2 ] + self.presum[row1 - 1][col1 - 1]
        # print (self.presum)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)