class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def check(s1,s2):
            mapping = {}
            for i in range(len(s1)):
                if s2[i] not in mapping:
                    mapping[s2[i]]=s1[i]
                else:
                    if mapping[s2[i]]!=s1[i]:
                        return False
            return True
        return check(t,s) and check(s,t)
