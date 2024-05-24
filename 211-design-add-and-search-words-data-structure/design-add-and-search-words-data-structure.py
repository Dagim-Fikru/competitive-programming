class WordDictionary:

    def __init__(self):
        self.dic = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.dic[len(word)].add(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.dic[len(word)]
        for l in self.dic[len(word)]:
            for i, ind in enumerate(word):
                if ind != l[i] and ind != '.':
                    break
            else:
                return True
        return False
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)