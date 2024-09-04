class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            check = {}
            found = True
            for i in range(len(pattern)):
                if pattern[i] in check:
                    if check[pattern[i]]!=word[i]:
                        found=False
                        break
                elif word[i] in check.values():
                    if pattern[i] in check:
                        if check[pattern[i]]!=word[i]:
                            found=False
                            break
                    else:
                        found=False
                        break
                else:
                    check[pattern[i]]=word[i]
            if found:
                ans.append(word)
        return ans