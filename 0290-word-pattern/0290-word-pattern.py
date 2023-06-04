class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        x = list(map(str,s.split()))
        newDict = {}
        if len(x)!=len(pattern):
            return False
        for i in range(len(x)):
            if x[i] not in newDict.keys():
                if pattern[i] in newDict.values():
                    return False
                newDict[x[i]]=pattern[i]
            else:
                if newDict[x[i]]== pattern[i]:
                    continue
                else:
                    return False
        return True
        
        