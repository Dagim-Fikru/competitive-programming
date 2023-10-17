class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        # for i in range(len(nums)-1):
        #     j=i+1
        #     k= len(nums)-1
        #     while j<k:
        #         if nums[j]-nums[i]==diff:
        #             if nums[k]-nums[j]>diff:
        #                 k-=1
        #             elif nums[k]-nums[j]<diff:
        #                 j+=1
        #             else:
        #                 count+=1
        #         else:
        #             i+=1
        # return count
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                for k in range(2,len(nums)):
                    if nums[j]-nums[i]==diff:
                        if nums[k]-nums[j]==diff:
                            count+=1
                    else:
                        continue
        return count
        