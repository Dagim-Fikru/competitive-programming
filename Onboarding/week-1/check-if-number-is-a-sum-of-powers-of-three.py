class Solution:
    def checkPowersOfThree(self, num: int) -> bool:
        arr=[]
        arr.append(num%3)
        num = num//3
        while num>1:
            arr.append(num%3)
            num = num//3
        if num==1:
            arr.append(1)
        # print(*arr[::-1])
        return 2 not in arr
        
        
        