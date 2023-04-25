class Solution:
    def secondHighest(self, s: str) -> int:
        setOfS= set(s)
        arr=[]
        x=["0",'1','2','3','4','5','6','7','8','9']
        for i in setOfS:
            if i in x:
                arr.append(int(i))
            else:
                continue
        arr.sort()
        if len(arr)==1 or len(arr)==0:
            return -1
        return arr[-2]