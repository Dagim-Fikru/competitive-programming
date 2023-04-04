class Solution:
    def partitionString(self, s: str) -> int:
        x=""
        count=1
        # arr=[]
        for i in s:
            # if s[-1]==i:
            #     arr.append(i)
            if i in x:
                count+=1
                # arr.append(x)
                x=""
                x+=i
            else:
                x+=i
        # arr.append(x)
        return count
        
        