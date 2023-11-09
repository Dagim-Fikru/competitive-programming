class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mappin = {}
        l,r = 0,0
        maxSize = 0
        while r<len(s):
            if s[r] in mappin:
                mappin[s[r]]+=1
            else:
                mappin[s[r]]=1
            while (r-l+1)- max(mappin.values())>k:
                mappin[s[l]]-=1
                l+=1
            maxSize = max(maxSize,r-l+1)
            r+=1
        return maxSize