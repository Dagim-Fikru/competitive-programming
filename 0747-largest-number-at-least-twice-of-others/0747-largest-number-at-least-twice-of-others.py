class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # arr=[]
        # for i in nums:
        #     arr.append(i)
        # arr.sort()
        # i=0
        # j=len(nums)-1
        # while i<j:
        #     if arr[j]>=2*arr[i]:
        #         i+=1
        #     else:
        #         return -1
        # return nums.index(arr[-1])
        maxElement = max(nums)
        for i in nums:
            if i==maxElement:
                continue
            else:
                if maxElement>=2*i:
                    continue
                else:
                    return -1
        return nums.index(maxElement)
        
        