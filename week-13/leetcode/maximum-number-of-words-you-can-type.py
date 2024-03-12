class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr = text.split(" ")
        freq = Counter(brokenLetters)
        count = 0
        for i in range(len(arr)):
            for j in arr[i]:
                if j in freq:
                    count+=1
                    break
        return len(arr) - count
