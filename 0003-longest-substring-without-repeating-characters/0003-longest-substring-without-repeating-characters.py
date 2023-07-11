class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        while i < len(s) and j < len(s):
            x = s[i:j + 1]
            if len(set(x)) == len(x):
                j += 1
                ans = max(ans, len(s[i:j]))
            else:

                i += 1
                j = i
        return ans