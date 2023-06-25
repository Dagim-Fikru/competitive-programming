class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        result = 1000
        for i in target:
            result = min(result,(s.count(i)//target.count(i)))
        return result
        
        
        
        