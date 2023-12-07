class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def alien_sort_key(word):
            return [order.index(char) for char in word]
        sortedWords = sorted(words, key=alien_sort_key)
        return sortedWords==words