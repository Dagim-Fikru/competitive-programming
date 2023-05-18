class Solution:
    def sum(self, num1: int, num2: int) -> int:
        if num1>0:
            while num1>0:
                num2+=1
                num1-=1
        else:
            while num1<0:
                num2-=1
                num1+=1
        return num2
        