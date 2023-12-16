class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        maxLen = max(len(word) for word in words)
        ans = []
        for i in range(maxLen):
            arr= []
            for word in words:
                if i < len(word):
                    arr.append(word[i])
                else:
                    arr.append(" ")
            ans.append(''.join(arr).rstrip())
        return ans