class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency = Counter(s)
        even = 0
        odd = 0
        flag = False
        for i in frequency:
            if frequency[i]%2:
                odd+= frequency[i]-1
                flag = True
            else:
                even+= frequency[i]
        if flag:
            return even+odd+1
        return even+odd
        
        