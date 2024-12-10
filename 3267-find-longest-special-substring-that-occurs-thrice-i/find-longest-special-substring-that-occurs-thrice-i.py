class Solution:
    def maximumLength(self, s: str) -> int:
        substring = defaultdict(int)
        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[i] != s[j]:
                    break
                substring[s[i:j+1]]+=1
        maxLen = -1
        print(substring)
        for key, value in substring.items():
            if value>=3 and len(key)!=0:
                maxLen = max(maxLen,len(key))
        return maxLen