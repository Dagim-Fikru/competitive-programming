class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        countOfAllowed = Counter(allowed)
        count=0
        for word in words:
            for i in word:
                if i not in countOfAllowed:
                    break
            else:
                count+=1
        return count
        