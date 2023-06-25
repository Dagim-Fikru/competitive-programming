class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # countS = Counter(s)
        # countT = Counter(target)
        # result = 500
        # for i,j in countT.items():
        #     result = min(result,countS[i]//j)
        # return result
        result = 1000
        for i in target:
            result = min(result,(s.count(i)//target.count(i)))
        return result
            
        
        
        
        # counter_s = Counter(s)        
        # return min(counter_s[c] // count for c,count in Counter(target).items())
        
        
        
        