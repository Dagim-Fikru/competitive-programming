class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        freq = Counter(words)
        arr = sorted(words, key=lambda x: -freq[x])
        ans = []
        count=1
        ans.append(arr[0])
        for i in range(1,len(arr)):
            if count<k:
                if ans[-1]!=arr[i]:
                    ans.append(arr[i])
                    count+=1
        return ans


        