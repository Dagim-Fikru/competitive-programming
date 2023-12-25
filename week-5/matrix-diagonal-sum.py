class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumOfDiagnolas = 0
        l=len(mat)
        for i in range(l):
            sumOfDiagnolas += mat[i][i]
            sumOfDiagnolas += mat[i][l-1-i]
        if l%2==0:
            return sumOfDiagnolas
        return sumOfDiagnolas - mat[l//2][l//2]
            
        