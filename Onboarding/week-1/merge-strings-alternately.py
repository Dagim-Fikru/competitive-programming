class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr=[]
        i=0
        j=0
        while i<len(word1) or j<len(word2):
            if i<=len(word1)-1:
                arr.append(word1[i])
                i+=1
            if j<=len(word2)-1:
                arr.append(word2[j])
                j+=1
        return "".join(arr)
            