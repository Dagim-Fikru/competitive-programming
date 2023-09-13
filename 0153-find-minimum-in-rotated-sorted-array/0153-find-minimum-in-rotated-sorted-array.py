class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i]<nums[j]:
                mini = min(nums[i],mini)
            elif nums[i]>nums[j]:
                mini = min(nums[j],mini)
            else:
                mini = min(nums[j],mini)
                
            i+=1
            j-=1
        return mini