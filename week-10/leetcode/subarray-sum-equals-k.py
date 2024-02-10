class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        currSum = 0
        check = {0:1}
        
        for i in range(len(nums)):
            currSum+=nums[i]
            if currSum-k in check:
                ans+=check[currSum-k]
            check[currSum]= 1 + check.get(currSum,0)
        return ans
                
            
        # count = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum+=nums[j]
        #         if sum==k:
        #             count+=1
        # return count
        