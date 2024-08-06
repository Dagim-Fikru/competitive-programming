class Solution:
    def minimumPushes(self, word: str) -> int:
        lst = list(word)
        counts = Counter(lst)
        arr = sorted(lst, key=lambda x: (counts[x], x), reverse=True)
        Newcounts = Counter(arr)
        newArr = []
        for i in Newcounts:
            newArr.append(i)
        numOfTypes = 0
        for j in range(len(newArr)):
            if j+1<=8:
                numOfTypes+= Newcounts[newArr[j]]
            elif j+1>8 and j+1<=16:
                 numOfTypes+= Newcounts[newArr[j]]*2
            elif j+1>16 and j+1<=24:
                numOfTypes+= Newcounts[newArr[j]]*3
            else:
                numOfTypes+= Newcounts[newArr[j]]*4
        # print(newArr)
        return numOfTypes
