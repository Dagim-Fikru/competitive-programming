class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        arr=[]
        strs.sort()
        x=strs[0]
        y=strs[-1]
        if not strs:
            return ""
        for i in range(len(x)):
            if i<len(y) and x[i]==y[i]:
                arr.append(x[i])
            else:
                break
        return "".join(arr)

        
        

        