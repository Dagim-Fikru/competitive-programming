class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        word_counts = collections.Counter(words)
        sorted_words = sorted(words, key=lambda x: -word_counts[x])
        for i in sorted_words:
            while sorted_words.count(i)>1:
                sorted_words.pop(sorted_words.index(i))
        return sorted_words[:k]
