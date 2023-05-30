class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        newDict = {}
        for i in range(len(s)):
            if s[i] not in newDict.keys() and t[i] not in newDict.values():
                newDict[s[i]]=t[i]
            else:
                if s[i] not in newDict.keys():
                    return False
                elif newDict[s[i]]==t[i]:
                    continue
                else:
                    return False
        return True
        # for i in range(len(s)):
        #     if counter1[s[i]]==counter2[t[i]]:
        #         continue
        #     else:
        #         return False
        # return True