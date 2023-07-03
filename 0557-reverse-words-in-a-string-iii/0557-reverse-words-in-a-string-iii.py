class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s)
        i=0
        for j in range(len(arr)):
            if arr[j]==' ':
                arr[i:j] = reversed(arr[i:j])
                i=j+1
            if j==len(arr)-1:
                arr[i:j+1] = reversed(arr[i:j+1])
        return "".join(arr)