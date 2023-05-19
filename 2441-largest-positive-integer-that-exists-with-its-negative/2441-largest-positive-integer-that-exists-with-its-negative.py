class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        while i<j:
            if nums[i]<0:
                if abs(nums[i])>nums[j]:
                    i+=1
                elif abs(nums[i])<nums[j]:
                    j-=1
                else:
                    return nums[j]
            else:
                break
        return -1