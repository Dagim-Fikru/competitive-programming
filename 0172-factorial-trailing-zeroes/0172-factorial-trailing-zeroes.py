class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fac(x):
            if x==1 or x==0:
                return 1
            else:
                return x * fac(x-1)
        nFac = str(fac(n))
        arr=[]
        count=0
        for i in nFac:
            arr.append(int(i))
        while arr[-1]==0:
            count+=1
            arr.pop()
        return count
        
        