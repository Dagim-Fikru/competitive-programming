class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        arr=[]
        for i,j in enumerate(nums):
            if target==j:
                arr.append(i)
        if len(arr)==0:
            return [-1,-1]
        return [arr[0],arr[-1]]
        