class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            indx = ord(word[i]) - ord("a")
            if not curr.children[indx]:
                curr.children[indx] = TrieNode()
            curr = curr.children[indx] 
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            indx = ord(word[i]) - ord("a")
            if not curr.children[indx]:
                return False
            curr = curr.children[indx] 
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            indx = ord(prefix[i]) - ord("a")
            if not curr.children[indx]:
                return False
            curr = curr.children[indx] 
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)