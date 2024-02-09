class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightMlti = []
        leftMlti = []
        multi=1
        for i in nums:
            leftMlti.append(multi)
            multi*=i
        multi = 1
        nums = nums[::-1]
        for i in nums:
            rightMlti.append(multi)
            multi*=i
        rightMlti = rightMlti[::-1]
        for i in range(len(rightMlti)):
            rightMlti[i]=rightMlti[i]*leftMlti[i]
        return rightMlti


        # arr=[]
        # multi=1
        # for i in range(len(nums)):
        #     j=0
        #     while j<len(nums):
        #         if j==i:
        #             j+=1
        #         else:
        #             multi=nums[j]*multi
        #             j+=1
        #     arr.append(multi)
        #     multi = 1
        # return arr