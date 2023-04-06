class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=None
        listOfS = list(s)
        listOfT = list(t)
        listOfS.sort()
        listOfT.sort()
        if len(listOfS)!=len(listOfT):
            return False
        else:
            for i in range(len(listOfS)):
                if listOfS[i]!=listOfT[i]:
                    x=False
                    break
                else:
                    x=True
        return x
                    
        # for i in s:
        #     if i not in t or len(t)!=len(s):
        #         # continue
        #         return False
        # return True
        