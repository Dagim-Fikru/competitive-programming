class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        words = list(word)
        if ch not in word:
            return word
        indx = words.index(ch[0])
        i=0
        j=indx

        while i<j:
            words[i],words[j] = words[j],words[i]
            i+=1
            j-=1
        return "".join(words)
