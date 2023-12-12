class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(map(str,s.split()))
        arr = arr[::-1]
        return " ".join(arr)
        