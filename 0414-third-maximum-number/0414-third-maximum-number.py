class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        # print(nums)
        if len(nums)<3:
            return(nums[-1])
        elif len(nums)==3:
            return(nums[0])
        else:
            i=len(nums)-1
            thirdMax = 0
            while i>len(nums)-3:
                if nums[i]>nums[i-1]:
                    thirdMax=nums[i-1]
                i-=1
            return thirdMax
        
#         elif len(nums)%2==0:
#                     return(nums[(len(nums)//2)-1])

#         return(nums[(len(nums)//2)-1])
        
        