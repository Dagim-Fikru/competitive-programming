class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        start = 0
        maxSize = 0
        for end in range(len(s)):
            while s[end] in check:
                check.remove(s[start])
                start+=1
            check.add(s[end])
            maxSize = max(maxSize,end-start+1)
        return maxSize
                
        
        