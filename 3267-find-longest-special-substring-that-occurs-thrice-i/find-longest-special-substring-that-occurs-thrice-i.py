class Solution:
    def maximumLength(self, s: str) -> int:
        substring = defaultdict(int)
        for i in range(len(s)):
            for j in range(len(s)):
                if len(list(set(s[i:j+1])))==1:
                    substring[s[i:j+1]]+=1
        maxLen = -1
        for key, value in substring.items():
            if value>=3:
                maxLen = max(maxLen,len(key))
        return maxLen