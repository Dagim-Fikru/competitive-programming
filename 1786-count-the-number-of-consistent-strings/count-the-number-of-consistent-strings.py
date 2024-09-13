class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mapping = {}

        for i in range(len(allowed)):
            mapping[allowed[i]] = i 
        ans = 0
        
        for word in words:
            consistent =True
            for char in word:
                if char not in mapping:
                    consistent = False
                    break
            if consistent:
                ans+=1
        return ans 
