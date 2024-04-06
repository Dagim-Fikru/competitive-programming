class Solution:
    def largestOddNumber(self, num: str) -> str:
        arr = list(num)

        for i in range(len(arr)-1,-1,-1):
            if int(arr[i])%2:
                return "".join(arr)
            else:
                arr[i]=""
        return "".join(arr)