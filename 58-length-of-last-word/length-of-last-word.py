class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = list(map(str,s.split()))
        return len(arr[-1])
        