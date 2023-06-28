class Solution:
    def reverse(self, x: int) -> int:
        y=str(x)
        y=y[::-1]
        arr=[]
        for i in y:
            arr.append(i)
        if arr[-1]=='-':
            arr.insert(0,arr.pop())
        y=int(''.join(arr))
        if y<=-2**31 or y>=(2**31)-1:
            return 0
        else:
            return y
        # arr=y.split(' ')
        # if y[-1]=='-':
        # y[-1]=y[0]
        # print(int(y))
        
        