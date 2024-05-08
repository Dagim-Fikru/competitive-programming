class Solution:
    def longestDecomposition(self, text: str) -> int:
        l = ""
        r = ""
        i=0
        j=len(text)-1
        ans = 0
        compare = 0
        while i<j:
            l+=text[i]
            r+=text[j]
            if l[::-1]==r:
                ans+=2
                compare+= 2*len(r)
                l=""
                r=""
            i+=1
            j-=1
        if compare!=len(text):
            ans+=1
        return ans