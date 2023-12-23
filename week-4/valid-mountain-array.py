class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                continue
            elif arr[i]==arr[i+1]:
                return False
            else:
                break
        if i==len(arr)-1 or i==0:
            return False
        for j in range(i,len(arr)-1):
            if arr[j]>arr[j+1]:
                continue
            else:
                return False
        return True
