class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        dic = Counter(order)
        # dic = {}
        # for i in range(len(order)):
        #     dic[order[i]]=i
        ans = []
        for i in order:
            if i in freq:
                while freq[i]>0:
                    ans.append(i)
                    freq[i]-=1
        
        for i in s:
            if i not in dic:
                while freq[i]>0:
                    ans.append(i)
                    freq[i]-=1
        return "".join(ans)