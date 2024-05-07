class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        maxLen = max(len(x),len(y))
        x = x.zfill(maxLen)
        y = y.zfill(maxLen)
        # print(x)
        # print(y)
        left, right = len(x)-1, len(y)-1
        res = 0
        while left >=0 and right >=0:
            if x[left] != y[right]:
                res+=1
            left-=1
            right-=1

        return res