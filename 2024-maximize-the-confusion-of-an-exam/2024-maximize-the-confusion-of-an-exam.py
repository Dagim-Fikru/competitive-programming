class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        F,T,i,j,ans = 0,0,0,0,0
        
        while j < len(answerKey):
            if answerKey[j] == 'F':
                F += 1
            else:
                T += 1
            
            while min(F, T) > k:
                if answerKey[i] == 'F':
                    F -= 1
                else:
                    T -= 1
                
                i += 1
            
            ans = max(ans, F + T)
            j += 1
        
        return ans
        