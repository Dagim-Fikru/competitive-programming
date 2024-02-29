class Solution:
    def maxScore(self, s: str) -> int:
        prefix = []
        total = 0
        for i in range(len(s)):
            total+=int(s[i])
            prefix.append(total)
        zeros = 0
        ones = prefix[-1]
        i=0
        j=len(prefix)-1
        ans = 0
        while i<len(s)-1 and j>0:
            if s[i]=="0":
                zeros+=1
            else:
                ones-=1
            ans = max(ans,ones+zeros)
            j-=1
            i+=1
        return ans
