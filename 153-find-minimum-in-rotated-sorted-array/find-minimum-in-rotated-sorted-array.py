class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        while right>left:
            mid = (right+left)//2
            if nums[mid+1]<nums[mid]:
                return nums[mid+1]
            elif nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[right]>nums[mid]:
                right = mid
            else:
                left = mid+1
        return nums[left]
        #return min(nums)
        # mini = nums[0]
        # i=0
        # j=len(nums)-1
        # while i<=j:
        #     if nums[i]<nums[j]:
        #         mini = min(nums[i],mini)
        #     elif nums[i]>nums[j]:
        #         mini = min(nums[j],mini)
        #     else:
        #         mini = min(nums[j],mini)
                
        #     i+=1
        #     j-=1
        # return mini