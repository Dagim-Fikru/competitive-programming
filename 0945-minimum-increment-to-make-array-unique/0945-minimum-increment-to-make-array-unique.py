class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                differ = nums[i-1] + 1 - nums[i]
                nums[i]=nums[i-1]+1
                count+=differ
            # if nums.count(nums[i])>1:
            #     while nums.count(nums[i])>1:
            #         nums[i]+=1
            #         count+=1
        # count=0
        # def numOfOccurence(ele):
        #     return nums.count(ele)
        # for i in range(len(nums)):
        #     if numOfOccurence(nums[i])==1:
        #         continue
        #     else:
        #         while numOfOccurence(nums[i])>1:
        #             nums[i]+=1
        #             count+=1
        return count
                    