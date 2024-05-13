class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        arr = [set(words[i]) for i in range(len(words))]
        for i in range(len(words)):
            for j in range(len(words)):
                if i==j:
                    continue
                else:
                    if not (arr[i] & arr[j]):
                        ans = max(ans,len(words[i])*len(words[j]))
        return ans