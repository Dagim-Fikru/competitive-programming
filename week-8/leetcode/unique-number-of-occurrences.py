class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        newHash = Counter(arr)
        x = set()
        for key,value in newHash.items():
            if value not in x:
                x.add(value)
            else:
                return False
        return True
            
        