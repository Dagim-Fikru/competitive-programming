class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = Counter('balloon')
        
        textC = Counter(text)
        result = 1500
        for i,j in word.items():
            result = min(result, textC[i]//j)
        return result
            
        