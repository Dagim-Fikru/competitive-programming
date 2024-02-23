class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n==0:
            return 1
        if n>0 and n%2!=0:
            return x * self.myPow(x*x,n//2)
        elif n>0 and n%2==0:
            return self.myPow(x*x,n//2)
        elif n<0 and n%2!=0:
            n=abs(n)
            return 1/(x * self.myPow(x*x,n//2))
        elif n<0 and n%2==0:
            n=abs(n)
            return 1/(self.myPow(x*x,n//2))
            
            
            
            