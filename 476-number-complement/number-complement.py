class Solution:
    def findComplement(self, num: int) -> int:
        ans = bin(num)
        arr = list(ans)
        for i in range(2,len(arr)):
            if arr[i]=="1":
                arr[i]="0"
            else:
                arr[i]="1"
        return(int("".join(arr),2))
        # print(type(ans))