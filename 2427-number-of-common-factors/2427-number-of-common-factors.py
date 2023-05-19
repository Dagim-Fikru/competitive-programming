class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        divide = min(a,b)
        while divide>=1:
            if a%divide ==0 and b%divide==0:
                count+=1
            divide-=1
        return count