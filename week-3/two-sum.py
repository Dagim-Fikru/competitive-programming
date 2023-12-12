class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i in range(len(nums)):
            if target-nums[i] not in hashMap:
                hashMap[nums[i]]=i
            else:
                return [hashMap[target-nums[i]],i]
                  
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if i==j:
        #             continue
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
                    
        # return arr