class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal = defaultdict(list)
        ans =[]
        for row in range(len(mat)):
            for column in range(len(mat[0])):
                diagonal[row + column].append(mat[row][column])
        for i,j in diagonal.items():
            if i%2 ==0:
                j =j[::-1]
            ans.extend(j)
        return ans