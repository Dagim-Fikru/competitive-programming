class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
#         rowMapping = {
#         1: ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
#         2: ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
#         3: ["z", "x", "c", "v", "b", "n", "m"]
# }
        ans=[]
        for word in words:
            arr= list(set(word.lower()))
            checkarr = []
            for i in arr:
                for j in range(len(rows)):
                    if i in rows[j]:
                        checkarr = list(rows[j])
                        break
                    else:
                        continue
            for i in arr:
                if i not in checkarr:
                    break
                if arr.index(i)==len(arr)-1 and i in checkarr:
                    ans.append(word)
        return ans