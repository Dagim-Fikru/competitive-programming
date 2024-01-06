class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        k = len(p)
        ans = []
        for i in range(len(s)+1-k):
            anagram = Counter(s[i:i+k])
            if target==anagram:
                ans.append(i)
        return ans