class Solution:
    def partitionString(self, s: str) -> int:
        x=""
        arr=[]
        for i in s:
            # if s[-1]==i:
            #     arr.append(i)
            if i in x:
                arr.append(x)
                x=""
                x+=i
            else:
                x+=i
        arr.append(x)
        return len(arr)
        
        