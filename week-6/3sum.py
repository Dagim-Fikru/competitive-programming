class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k= len(nums)-1
            
            while j<k:
                threeSum = nums[i]+nums[j]+nums[k]
                if threeSum>0:
                    k-=1
                elif threeSum<0:
                    j+=1
                else:
                    arr.append([nums[i],nums[k],nums[j]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
        return arr
#         x=0
#         for i in range(len(nums)):
#             for j in range (len(nums)):
#                 if i==j and j==x and i==x:
#                     continue
#                 Elem = nums[x]
#                 if nums[i]+nums[j]== -Elem:
#                     arr.append([nums[i],nums[j],nums[x]])
#             x+=1
#         return arr
            
        # nums.sort()
        # k=0
        # if len(set(nums))==1:
        #     for i in set(nums):
        #         if i==0:
        #             arr.append([0,0,0])
        # else:
        #     while nums[k]<0:
        #         if nums[k]==nums[k+1]:
        #             k+=1
        #         i=k+1
        #         j=len(nums)-1
        #         while i<j:
        #             target = -nums[k]
        #             if nums[i] + nums[j]>target:
        #                 j-=1
        #             elif nums[i] + nums[j]<target:
        #                 i+=1
        #             else:
        #                 arr.append([nums[k], nums[i],nums[j]])
        #                 break
        #         k+=1
        # return arr
                
        