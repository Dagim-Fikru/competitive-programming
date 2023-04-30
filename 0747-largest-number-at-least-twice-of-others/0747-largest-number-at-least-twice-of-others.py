class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        arr=[]
        for i in nums:
            arr.append(i)
        arr.sort()
        i=0
        j=len(nums)-1
        while i<j:
            if arr[j]>=2*arr[i]:
                i+=1
            else:
                return -1
        return nums.index(arr[-1])
        
        