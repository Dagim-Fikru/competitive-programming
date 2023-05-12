class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(map(str,s.split()))
        arr2 = arr[::-1]
        
        return " ".join(arr2)
        