class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        arr=[]
        for i in range(len(s)-1,-1,-1):
            if s[i] in lastIndex:
                continue
            else:
                lastIndex[s[i]]= i
        size , end = 0,0
        for i,c in enumerate(s):
            size+=1
            if lastIndex[c]>end:
                end = lastIndex[c]
            if i==end:
                arr.append(size)
                size=0
        return arr
        