class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCount = Counter(s)
        tCount = Counter(t)
        for i in t:
            if sCount[i]==tCount[i]:
                continue
            else:
                return i
            