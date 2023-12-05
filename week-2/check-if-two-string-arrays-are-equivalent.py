class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        newWord1 = "".join(word1)
        newWord2 = "".join(word2)
        return newWord1==newWord2