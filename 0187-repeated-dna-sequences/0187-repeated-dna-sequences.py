class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        check, ans = set(), []
        for i in range(len(s)-9):
            if s[i:i+10] in check:
                ans.append(s[i:i+10])
            check.add(s[i:i+10])
        return list(set(ans))
                