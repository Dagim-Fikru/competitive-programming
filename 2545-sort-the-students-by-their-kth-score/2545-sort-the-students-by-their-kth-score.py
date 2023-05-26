class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        n=len(score)
        for i in range(n):
            for j in range(n-i-1):
                if score[j][k]<score[j+1][k]:
                    score[j],score[j+1]=score[j+1],score[j]
        return score
                    